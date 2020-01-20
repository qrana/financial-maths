"""Pricing a structured barrier option"""
import numpy as np

################################################################################
# Simulation parameters
M = 100
r = 0.03
sg = 0.3
dt = 1 / 252
T = 5
n = int(T / dt)
S0 = 100
K = 110
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

        for tau in range(T):
            # Find the maximum value of the realized stock price path
            tau_max_idx = int(n / float(tau + 1)) - 1
            S_tmax = np.max(S1[:tau_max_idx])
            # normal pricing
            V[i] = np.exp(-r * tau) * np.max(S_tmax - K, 0)
            if S_tmax < 0.7 * S0:
                break

    # Print the results
    print('Price (mean), normal pricing:', np.mean(V))
    print('Std, normal pricing:', np.std(V))
