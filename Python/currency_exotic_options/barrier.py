"""Pricing a barrier option"""
import numpy as np

################################################################################
# Simulation parameters
M = 100
r = 0.05
sg = 0.3
dt = 1 / 252
T = 1
n = int(T / dt)
S0 = 50
H = 45
K = 50
################################################################################


if __name__ == '__main__':
    # Generate random numbers from a normal distribution for the MC simulation
    eps = np.random.normal(size=(n, M))

    # Initialize empty vectors
    V = np.zeros((M))
    # Iterate through M iterations
    for i in range(M):
        S1 = np.zeros((n))
        S1[0] = S0
        # Iterate through n - 1 time steps (first time step is known)
        for j in range(n - 1):
            # normal pricing is stored in S1
            S1[j + 1] = S1[j] * np.exp((r - 0.5 * sg ** 2) * dt \
                 + sg * eps[j, i] * np.sqrt(dt))
        # Find the maximum value of the realized stock price path
        S_tmin = np.min(S1)

        # Test if the price path exceeded the barrier H
        # if so, the option is exercisable
        # then the pay off is max(S(T) - K, 0)
        if S_tmin > H:
            # normal pricing
            V[i] = np.exp(-r * T) * np.max(S1[-1] - K, 0)

    # Print the results
    print('Price (mean), normal pricing:', np.mean(V))
    print('Std, normal pricing:', np.std(V))
