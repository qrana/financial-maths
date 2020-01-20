import numpy as np

from scipy import stats

def european_call(x, rb, T, d1, K, rq, d2):
    return x * np.exp(-rb * T) * stats.norm.cdf(d1) - K * np.exp(-rq * T) * stats.norm.cdf(d2)


def calc_d1(x, K, rq, sg, T, rb):
    return (np.log(x / K) + (rq - rb + 0.5 * sg ** 2) * T) / (sg * np.sqrt(T))


def calc_d2(x, K, rq, sg, T, rb):
    return (np.log(x / K) + (rq - rb - 0.5 * sg ** 2) * T) / (sg * np.sqrt(T))


def main():
    T = 8./12
    K = 0.5
    X0 = 0.52
    sg = 0.12
    rq = 0.04
    rb = 0.08

    d1 = calc_d1(X0, K, rq, sg, T, rb)
    d2 = calc_d1(X0, K, rq, sg, T, rb)
    price = european_call(X0, rb, T, d1, K, rq, d2)
    print(price)


if __name__ == '__main__':
    main()
