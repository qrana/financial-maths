import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def calc_d1(St, K, r, s, T, t=0, q=0):
    return (np.log(St / K) + (r - q + 0.5 * s ** 2) * (T - t)) \
           / (s * np.sqrt(T - t))


def calc_d2(d1, s, T, t=0):
    return d1 - s * np.sqrt(T - t)

def problem2a():
    T_final = 5
    Ts = np.arange(dt, T_final, dt)

    mus_c = []
    sgs_c = []
    for T in Ts:
        d1 = calc_d1(St, K, r, sg, T, q=q)
        d2 = calc_d2(d1, sg, T)
        delta = np.exp(-q * T) * norm.cdf(d1)
        gamma = norm.pdf(d1) * np.exp(-q * T) / (St * sg * np.sqrt(T))
        theta = -(St * norm.pdf(d1) * sg * np.exp(-q * T)) / (2 * np.sqrt(T)) \
                + q * St * norm.cdf(d1) * np.exp(-q * T) \
                - r * K * np.exp(-r * T) * norm.cdf(d2)
        Ct = St * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        mu_call = (1. / Ct) * (theta + mu * St * delta + 0.5 * sg ** 2 * St ** 2 * gamma)
        sg_call = (1. / Ct) * sg  * St * delta
        mus_c.append(mu_call)
        sgs_c.append(sg_call)
    plt.figure()
    plt.plot(Ts, mus_c)
    plt.ylabel('Price')
    plt.xlabel('Time to maturity')
    plt.figure()
    plt.plot(Ts, sgs_c)
    plt.ylabel('Price')
    plt.xlabel('Time to maturity')
    plt.show()

def problem2b():
    T = 1
    Sts = np.arange(0.01, 100, 0.1)
    mus_c = []
    sgs_c = []
    for St in Sts:
        d1 = calc_d1(St, K, r, sg, T, q=q)
        d2 = calc_d2(d1, sg, T)
        delta = np.exp(-q * T) * norm.cdf(d1)
        gamma = norm.pdf(d1) * np.exp(-q * T) / (St * sg * np.sqrt(T))
        theta = -(St * norm.pdf(d1) * sg * np.exp(-q * T)) / (2 * np.sqrt(T)) \
                + q * St * norm.cdf(d1) * np.exp(-q * T) \
                - r * K * np.exp(-r * T) * norm.cdf(d2)
        Ct = St * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        mu_call = (1. / Ct) * (theta + mu * St * delta + 0.5 * sg ** 2 * St ** 2 * gamma)
        sg_call = (1. / Ct) * sg  * St * delta
        mus_c.append(mu_call)
        sgs_c.append(sg_call)
    plt.figure()
    plt.plot(Sts, mus_c)
    plt.ylabel('Price')
    plt.xlabel('Stock Price')
    plt.figure()
    plt.plot(Sts, sgs_c)
    plt.ylabel('Price')
    plt.xlabel('Stock Price')
    plt.show()

if __name__ == '__main__':

    K = 50
    sg = 0.5
    mu = 0.15
    q = 0.08
    r = 0.13
    St = 50
    dt = 1 / 252.

    # problem2a()
    problem2b()
