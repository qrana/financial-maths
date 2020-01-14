#include <algorithm>
#include <iostream>
#include "stockdynamics.hh"
#include "plot.hh"


void example1()
{
    auto s = StockDynamics(0.1, 0.3);
    std::pair<TimeData, TimeData> result = s.simulate_path(10, 1);
    auto p1 = Plot();
    p1.linepointsplot(result.first, result.second, "Stock price");
}


void example2()
{
    auto s = StockDynamics(0.1, 0.3);
    DataMatrix result2 = s.simulate_multiple_paths(10, 1);
    auto p2 = Plot();
    p2.linepointsplot(result2, "Stock price");
}


void example3()
{
    auto s = StockDynamics(0.1, 0.3);
    DataVector result3 = s.simulate_terminal_prices(50, 1, 0, 10000);
    auto p3 = Plot();
    p3.histogram(result3, "Price distribution");
}


void example4()
{
    auto s = StockDynamics(0.1, 0.3);
    DataVector result3 = s.simulate_terminal_prices(50, 1, 0, 10000);
    DataVector log_result3;
    std::transform(result3.begin(), result3.end(),
                   std::back_inserter(log_result3),
                   [](double s) ->double {return std::log(s);});
    auto p = Plot();
    p.histogram(log_result3, "Log-price distribution");
}


int main()
{
    std::cout << "Hello World!" << std::endl;
    example4();
    return 0;
}
