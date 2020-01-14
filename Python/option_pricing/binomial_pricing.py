"""Binomial pricing of options"""
import numpy as np
# pylint: disable=invalid-name


def call_option(S, K):
    return max(S - K, 0)


def put_option(S, K):
    return max(K - S, 0)


def risk_neutral_prob(r, U, D, d_t=0):
    return (np.exp(r * d_t) - D) / (U - D)


def option_price(p, C_u, C_d, r, d_t):
    return (p * C_u + (1 - p) * C_d) * np.exp(-r * d_t)


def main():
    S0 = 100
    K = 105
    r = 0.03
    U = 1.07
    D = 1 / U
    d_t = 1 / 12.0
    M = 6
    p = risk_neutral_prob(r, U, D, d_t)
    print(f'p={p}')
    C_u = put_option(S0*U, K)
    C_d = put_option(S0*D, K)
    C0 = option_price(p, C_u, C_d, r, d_t)

    # Stock price lattice
    S = []
    for i in range(M, 0, -1):
        Ss = []
        for j in range(i + 1):
            Ss.append(S0 * U ** (i - j) * D ** j)
        print(Ss)
        S.append(Ss)
    print([S0])
    S.append([S0])

    # EUR option lattice
    C = []
    C.append(put_option(S0 * U ** (M - j) * D ** j, K) for j in range(M))
    for i in range(M, 0, -1):
        Cs = []
        for j in range(i + 1):
            C0 = put_option(S0 * U ** (i - j) * D ** j, K)
            C1 = option_price(
                p,
                C[-1][j],
                C[-1][j],
                r, (M - i) * d_t)
            Cs.append(C0)
        print(Cs)
        C.append(Cs)
    print([option_price(p, put_option(U * S0, K), put_option(D * S0, K), r, M * d_t)])


if __name__ == '__main__':
    main()

"""
# init vars
r = 0.02
d_t = 1.0 / 12
S0 = 10.0
K = 9.0
U = 13 / S0
D = 7.5 / S0
p = risk_neutral_prob(r, U, D, d_t)
MODE = 'call'


if MODE == 'call':
    # Call option
    C_u = call_option(13, K)
    C_d = call_option(7.5, K)
elif MODE == 'put':
    # Put option
    C_u = put_option(13, K)
    C_d = put_option(7.5, K)
else:
    raise ValueError(f'Unknown MODE {MODE}')

C0 = (p * C_u + (1 - p) * C_d) * np.exp(-r * d_t)
print(f'U={U}')
print(f'D={D}')
print(f'p={p}')
print(f'C0={C0}')
"""
