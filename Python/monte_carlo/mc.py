import numpy as np
import matplotlib.pyplot as plt


N = 10000


def main():
    eps1 = np.random.normal(size=(N))
    e12 = np.random.normal(size=(N))
    corr = np.corrcoef(eps1, e12)
    print(corr)
    rho12 = 0.75
    eps2 = rho12 * eps1 + np.sqrt(1 - rho12 ** 2) * e12
    corr2 = np.corrcoef(eps1, eps2)
    print(corr2)

    mu1 = 0.1
    mu2 = 0.5
    sg1 = 0.05
    sg2 = 0.50
    dt = 1 / 252
    T = 1
    L = int(T / dt)
    rho = 1
    S0 = 1
    S1 = [S0]
    S2 = [S0]
    eps1 = np.random.normal(size=(L))
    e12 = np.random.normal(size=(L))
    eps2 = rho * eps1 + np.sqrt(1 - rho ** 2) * e12

    for i in range(L):
        S1.append(S1[0] * np.exp((mu1 - 0.5 * sg1 ** 2) * T + sg1 * eps1[i] * np.sqrt(T)))
        S2.append(S2[0] * np.exp((mu2 - 0.5 * sg2 ** 2) * T + sg2 * eps2[i] * np.sqrt(T)))
    plt.plot(S1)
    plt.plot(S2)
    plt.show()


if __name__ == '__main__':
    main()
