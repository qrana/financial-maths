#ifndef PLOT_HH
#define PLOT_HH

#include <vector>
#include <string>


using DataVector = std::vector<double>;
using DataMatrix = std::vector<DataVector>;


class Plot
{

public:
    Plot();

    void sleep(int i);

    void linepointsplot(DataVector x, DataVector y, std::string label);

    void linepointsplot(DataMatrix xy, std::string label);

    void histogram(DataVector x, std::string label, int num_bins=10);
};

#endif // PLOT_HH
