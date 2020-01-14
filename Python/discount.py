import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def discount(A, T, r, n):
    if n == float('inf'):
        return A * np.exp(r*T)
    else:
        return A * (1 + float(r) / n) ** (n * T)


def continuous_saving(A, r, n, T, a, r_var=0.02):
    y = []
    curr_A = A
    y.append(curr_A)
    for i in range(n * T):
        curr_A += a
        curr_r = np.random.normal(r, np.sqrt(r_var))
        curr_A = discount(curr_A, 1.0 / n, curr_r, float('inf'))
        if i % n == 0:
            y.append(curr_A)
    return y


def main():
    A = 0
    r = 0.10
    n = 12
    T = 30
    a = 1
    x = np.arange(0, T + 1)
    # y1 = [discount(A, t, r, n) for t in x]
    # y2 = [discount(A, t, r, float('inf')) for t in x]
    # plt.plot(x, y1, label=f'{n} periods')
    # plt.plot(x, y2, label='Continuous')
    y = continuous_saving(A, r, n, T, a)
    plt.plot(x, y, label=f'Saving {a} per period')
    plt.xlabel('Time')
    plt.ylabel('Value / k€')
    plt.grid(True, which='major')
    plt.title(f'Investment A={A} r={r}')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
