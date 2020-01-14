import numpy as np


S0 = 10
K = 9.3
s = 0.3
r = 0.025
T = 1
M = 10000

S_t = np.zeros((M, 1))
S_t[0] = S0
epsilon = np.random.normal(size=(M, 1))

for i in range(M):
    S_t[i] = S0 * np.exp((r - 0.5 * s ** 2) * T  + s * epsilon[i] * np.sqrt(T))

Cs = S_t - K
Ps = K - S_t
Cs[Cs < 0] = 0
Ps[Ps < 0] = 0
# Ps = np.max(K - S_t, 0)

C = np.mean(Cs)
P = np.mean(Ps)

print(C, P)
