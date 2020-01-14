#include "stockdynamics.hh"
#include <cmath>
#include <iostream>


StockDynamics::StockDynamics()
{
    this->mu = 0;
    this->sigma = 1;
    this->epsilon = std::normal_distribution<>(0, 1);
}

StockDynamics::StockDynamics(double mu, double sigma)
{
    this->mu = mu;
    this->sigma = sigma;
    this->epsilon = std::normal_distribution<>(0, 1);
}

std::pair<TimeData, TimeData> StockDynamics::simulate_path(
        double S0, int T, double dt, int seed)
{
    std::random_device rd(std::to_string(seed));
    std::mt19937 gen{rd()};
    std::vector<double> path = {S0};
    std::vector<double> time = {0};
    int num_steps = int(T / dt);
    for (int i = 1; i < num_steps; ++i)
    {
        double e = this->epsilon(gen);
        double s = path.at(i - 1)
                * std::exp((this->mu - 0.5 * std::pow(this->sigma, 2))
                           * dt + this->sigma * e * std::sqrt(dt));
        path.push_back(s);
        time.push_back((double)i);
    }
    return std::pair<TimeData, TimeData>({time, path});
}

std::vector<TimeData> StockDynamics::simulate_multiple_paths(
        double S0, int T, double dt, int seed, int num_simulations)
{
    auto result = this->simulate_path(S0, T, dt, seed);
    std::vector<TimeData> paths = {result.first, result.second};
    for (int i = seed + 1; i < seed + num_simulations; ++i)
    {
        result = simulate_path(S0, T, dt, i);
        paths.push_back(result.second);
    }
    return paths;
}

TimeData StockDynamics::simulate_terminal_prices(
        double S0, int T, int seed, int num_simulations)
{
    std::random_device rd(std::to_string(seed));
    std::mt19937 gen{rd()};
    TimeData prices = {};
    for (int i = 0; i < num_simulations; ++i)
    {
        double e = this->epsilon(gen);
        double s = S0 * std::exp((this->mu - 0.5 * std::pow(this->sigma, 2))
                           * T + this->sigma * e * std::sqrt(T));
        prices.push_back(s);
    }
    return prices;
}
