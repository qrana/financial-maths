import numpy as np
from scipy.stats import norm


S0 = 10
K = 9.3
r = 0.025
s = 0.3
T = 1

def calc_d1(St, K, r, s, T, t=0, q=0):
    return (np.log(St / K) + (r - q + 0.5 * s ** 2) * (T - t)) \
           / (s * np.sqrt(T - t))


def calc_d2(d1, s, T, t=0):
    return d1 - s * np.sqrt(T - t)

def price_call_option(S0, d1, d2, r, K, T):
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

d1 = calc_d1(S0, K, r, s, T)
d2 = calc_d2(d1, s, T)
C = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
print(C)

F = S0 - K * np.exp(-r * T)
P = C - F
print(P)
