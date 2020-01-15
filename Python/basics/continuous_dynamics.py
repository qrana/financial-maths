import numpy as np
import matplotlib.pyplot as plt


m = 0.15
s = 0.3
d_t = 1.0 / 252
all_S = []
num_sim = 1000

for j in range(num_sim):
    Ss = [1]

    for i in range(252):
        S_prev = Ss[-1]
        S_curr = S_prev * (1 + m * d_t + \
            s * np.sqrt(d_t) * np.random.standard_normal())
        Ss.append(S_curr) 

    all_S.append(Ss)

S = np.array(all_S).T
t = np.arange(0, 253)
final_S = S[-1]
avg_perf = np.average(final_S)
plt.title(f'Average performance {avg_perf}')
plt.plot(t, S)
# plt.show()

S_u = np.sum([final_S > 1])
print(S_u / num_sim)
