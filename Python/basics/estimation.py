import numpy as np
import pandas as pd

datafile = './data/IBM.csv'

data = pd.read_csv(datafile, sep=',')
# print(data['Adj Close'])

S = data['Adj Close']
N = len(S) - 1
d_t = 1
v_hat = np.log(S[N] / S[0]) / N
print('v_hat (daily return):', v_hat)
print('N * v_hat (annual return):', N * v_hat)
s_2 = 0
for i in range(1, len(S)):
    s_2 += np.power(np.log(S[i] / S[i - 1]) - v_hat, 2)
s_2 /= (N - 1)
print('s (daily volatility):', np.sqrt(s_2))
print('s (annual volatility):', np.sqrt(s_2 * N))

q = 0.5 + 0.5 * (1 / np.sqrt(s_2 / (v_hat ** 2 * d_t) + 1))
q_aprx = 0.5 * 0.5 * v_hat / np.sqrt(s_2) * np.sqrt(d_t)
print('q:', q, 'q approximated:', q_aprx)

U = np.exp(np.sqrt(s_2 * d_t + (v_hat * d_t) ** 2))
D = np.exp(-np.sqrt(s_2 * d_t + (v_hat * d_t) ** 2))
print('U:', U, 'D:', D)

U_aprx = np.exp(np.sqrt(s_2 * d_t))
D_aprx = np.exp(-np.sqrt(s_2 * d_t))
print('U approximated:', U_aprx, 'D approximated:', D_aprx)
