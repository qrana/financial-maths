#ifndef STOCKDYNAMICS_HH
#define STOCKDYNAMICS_HH

#include <random>
#include <utility>
#include <string>
#include <vector>


using TimeData = std::vector<double>;


class StockDynamics
{
private:
    double mu;
    double sigma;
    std::normal_distribution<> epsilon;

public:
    // Default constructor
    StockDynamics();

    // Alternative constructor
    StockDynamics(double mu, double sigma);

    std::pair<TimeData, TimeData> simulate_path(
            double S0, int T, double dt = 1.0/252, int seed=0);

    std::vector<TimeData> simulate_multiple_paths(
            double S0, int T, double dt = 1.0/252, int seed=0,
            int num_simulations=10);

    TimeData simulate_terminal_prices(
            double S0, int T, int seed=0, int num_simulations=10);
};

#endif // STOCKDYNAMICS_HH
