#include "plot.hh"
#include <algorithm>
#include <numeric>
#include <windows.h>
#include <conio.h>
#include <iostream>
#include <sstream>
#include "gnuplot-cpp/gnuplot-cpp/gnuplot_i.hpp"


Plot::Plot()
{
}

void Plot::sleep(int i)
{
    Sleep(i*1000);
}


void Plot::linepointsplot(DataVector x, DataVector y, std::string label)
{
    Gnuplot g("linespoints");

    g.set_grid();
    g.plot_xy(x, y, label);

    this->sleep(1);
    g.remove_tmpfiles();

    std::cout << std::endl << "Press any key to continue..." << std::endl;
    FlushConsoleInputBuffer(GetStdHandle(STD_INPUT_HANDLE));
    _getch();
}

void Plot::linepointsplot(DataMatrix xy, std::string label)
{
    Gnuplot g("linespoints");

    g.set_grid();
    DataVector time = xy.at(0);
    int N = xy.size();
    std::cout << "Plotting " << N - 1 << " series" << std::endl;
    for (auto i = 1; i < N; ++i)
    {
        g.plot_xy(time, xy.at(i), label + " " + std::to_string(i));
    }

    this->sleep(1);
    std::cout << std::endl << "Press any key to continue..." << std::endl;
    FlushConsoleInputBuffer(GetStdHandle(STD_INPUT_HANDLE));
    _getch();

    g.remove_tmpfiles();
}

void Plot::histogram(DataVector x, std::string label, int num_bins)
{
    int smallest_bin = *std::min_element(x.begin(), x.end());
    int largest_bin = *std::max_element(x.begin(), x.end());
    int N = num_bins;
    double range = largest_bin - smallest_bin;
    double step = range / N;
    DataVector hist(N, 0);
    std::cout << "Smallest: " << smallest_bin
              << ", Largest: " << largest_bin
              << std::endl;
    DataVector bins(N);
    for (int i = 0; i < N; ++i)
    {
        bins[i] = smallest_bin + i * step;
    }

    std::sort(x.begin(), x.end());
    for (double data : x)
    {
        auto closest = std::lower_bound(bins.begin(), bins.end(), data);
        auto pos = std::distance(bins.begin(), closest);
        ++hist[pos];
    }

    Gnuplot g("boxes");
    g.set_grid();
    g.cmd("set boxwidth	" + std::to_string(step * 0.9));
    g.plot_xy(bins, hist, label);

    this->sleep(1);
    g.remove_tmpfiles();

    std::cout << std::endl << "Press any key to continue..." << std::endl;
    FlushConsoleInputBuffer(GetStdHandle(STD_INPUT_HANDLE));
    _getch();
}
