"""Solution for up-and-in option with antithetic Monte-Carlo"""
import numpy as np

################################################################################
# Simulation parameters
M = 10000
r = 0.02
sg = 0.3
dt = 1 / 252
T = 1
n = int(T / dt)
S0 = 1
H = 1.1
K = 0.9
################################################################################


if __name__ == '__main__':
    # Generate random numbers from a normal distribution for the MC simulation
    eps = np.random.normal(size=(n, M))

    # Initialize empty vectors
    V = np.zeros((M))
    V_ = np.zeros((M))
    W = np.zeros((M))
    # Iterate through M iterations
    for i in range(M):
        S1 = np.zeros((n))
        S2 = np.zeros((n))
        S1[0] = S0
        S2[0] = S0
        # Iterate through n - 1 time steps (first time step is known)
        for j in range(n - 1):
            # normal pricing is stored in S1
            S1[j + 1] = S1[j] * np.exp((r - 0.5 * sg ** 2) * dt \
                 + sg * eps[j, i] * np.sqrt(dt))
            # antitetic variate pricing is stored in S2
            S2[j + 1] = S2[j] * np.exp((r - 0.5 * sg ** 2) * dt \
                - sg * eps[j, i] * np.sqrt(dt))
        # Find the maximum value of the realized stock price path
        S_tmax = np.max(S1)
        S_amax = np.max(S2)

        # Test if the price path exceeded the barrier H
        # if so, the option is exercisable
        # then the pay off is max(S(T) - K, 0)
        if S_tmax > H:
            # normal pricing
            V[i] = np.exp(-r * T) * np.max(S1[-1] - K, 0)
        if S_amax > H:
            # for use in antithetic pricing
            V_[i] = np.exp(-r * T) * np.max(S2[-1] - K, 0)
        # antithetic pricing
        W[i] = 0.5 * (V[i] + V_[i])

    # Print the results
    print('Price (mean), normal pricing:', np.mean(V))
    print('Price (mean), antithetic pricing:', np.mean(W))
    print('Std, normal pricing:', np.std(V))
    print('Std, antithetic pricing:', np.std(W))

    # It can be seen that antithetic pricing has a lower standard deviation.
    # This is because of the use of antithetic variates.

    # It can be shown analytically that the variance of the antithetic pricing
    # is less than or equal to half of the variance of normal pricing.
    # This is verified below.
    print('Test if Var(W) <= 0.5 * Var(V):', np.var(W) <= 0.5 * np.var(V))
