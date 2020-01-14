"""Solution for up-and-in option with control Monte-Carlo"""
import numpy as np
from scipy import stats

################################################################################
# Simulation parameters
M = 10000
r = 0.02
sg = 0.3
dt = 1 / 252
T = 1
n = int(T / dt)
S0 = 1
K = 0.9
################################################################################


# Generate random numbers from a normal distribution for the MC simulation
eps = np.random.normal(size=(n, M))
f_avg = np.zeros((M))
f_geom = np.zeros((M))
sgg = sg / np.sqrt(3)
a = 0.5 * (r - 0.5 * sgg ** 2)
d1 = (np.log(S0 / K) + (a + 0.5 * sgg ** 2) * T) / (sgg * np.sqrt(T))
d2 = d1 - sgg * np.sqrt(T)
c_geom = S0 * np.exp((a - r) * T) * stats.norm.cdf(d1) - \
    K * np.exp(-r * T) * stats.norm.cdf(d2)

# Iterate through M iterations
for i in range(M):
    S = np.zeros((n))
    S[0] = S0
    # Iterate through n - 1 time steps (first time step is known)
    for j in range(n - 1):
        # normal pricing is stored in S
        S[j + 1] = S[j] * np.exp((r - 0.5 * sg ** 2) * dt \
             + sg * eps[j, i] * np.sqrt(dt))
    # Find the average value of the realized stock price path
    S_avg = np.mean(S)
    # Find also the MC geometric average
    S_geom = stats.mstats.gmean(S)

    # Discounted payoffs
    f_avg[i] = np.exp(-r * n * dt) * max(S_avg - K, 0)
    f_geom[i] = np.exp(-r * n * dt) * max(S_geom - K, 0)

# Calculate the optimal step size
b = np.cov(f_geom, f_avg)[0, 1] / np.var(f_geom)

# Calculate the optimal option price
c_avg = np.mean(f_avg) - b * (np.mean(f_geom) - c_geom)

# Print the results
print('Price, (c_geom)', c_geom)
print('Price (mean), control pricing:', np.mean(c_avg))
print('Price (mean), normal pricing:', np.mean(f_avg))
print('STD, control pricing:', np.std(f_avg))
print('STD, norm pricing:', np.std(f_avg))

# It can be seen that antithetic pricing has a lower standard deviation.
# This is because of the use of antithetic variates.
