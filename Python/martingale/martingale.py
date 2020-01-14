import numpy as np
import matplotlib.pyplot as plt


N = 10000


def martingale_call(S0, S_q, S_n, K, T, r):
    """Martingale call option pricing"""
    q = np.sum([S_n > K]) / len(S_n)
    qs = np.sum([S_q > K]) / len(S_q)
    return S0 * qs - K * np.exp(-r * T) * q


def mc_call_rn(S_n, K, T, r):
    """Monte-Carlo call option pricing with risk-neutral probabilities"""
    return np.exp(-r * T) * np.mean(call_payoff(S_n, K))


def mc_call_martingale(S0, S_q, K):
    return S0 * np.mean(np.maximum(1 - K * S_q ** (-1), 0))


def call_payoff(S_n, K):
    return np.maximum(S_n - K, 0)


def problem1():
    S0 = 10
    K = 9.3
    r = 0.025
    sg = 0.3
    T = 1
    eps = np.random.normal(size=(N))

    S_n = np.zeros(N)  # risk neutral
    S_q = np.zeros(N)  # prob measure s
    for i in range(N):
        # S_t[i] = S0 * np.exp((r - 0.5 * s ** 2) * T  + s * epsilon[i] * np.sqrt(T))
        S_n[i] = S0 * np.exp((r - 0.5 * sg ** 2) * T + sg * eps[i] * np.sqrt(T))
        S_q[i] = S0 * np.exp((r + sg ** 2 - 0.5 * sg ** 2) * T + sg * eps[i] * np.sqrt(T))

    # plt.hist(S_n)
    # plt.hist(S_q)
    # plt.show()

    print('Martingale price:', martingale_call(S0, S_q, S_n, K, T, r))
    print('MC price:', mc_call_rn(S_n, K, T, r))


def problem2():
    S0 = 10
    K = 9.3
    r = 0.025
    sg = 0.3
    T = 1
    eps = np.random.normal(size=(N))

    S_n = np.zeros(N)  # risk neutral
    S_q = np.zeros(N)  # prob measure s
    for i in range(N):
        # S_t[i] = S0 * np.exp((r - 0.5 * s ** 2) * T  + s * epsilon[i] * np.sqrt(T))
        S_n[i] = S0 * np.exp((r - 0.5 * sg ** 2) * T + sg * eps[i] * np.sqrt(T))
        S_q[i] = S0 * np.exp((r + sg ** 2 - 0.5 * sg ** 2) * T + sg * eps[i] * np.sqrt(T))

    # plt.hist(S_n)
    # plt.hist(S_q)
    # plt.show()

    print('MC price risk-neutral:', mc_call_rn(S_n, K, T, r))
    print('MC price stock:', mc_call_martingale(S0, S_q, K))




if __name__ == '__main__':
    problem2()
