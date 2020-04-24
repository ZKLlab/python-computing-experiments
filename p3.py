import math
import random

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


def get_p(m: int, n: int):
    q = 0
    for i in range(m):
        s = set()
        for j in range(n):
            day = random.randint(1, 365)
            if day in s:
                q += 1
                break
            else:
                s.add(day)
    return q / m


if __name__ == '__main__':
    # 每班人数 1 ~ 100 进行统计分析
    n_p = np.zeros((100, 2))
    for _i in range(100):
        print('\r{}%'.format(_i), end='')
        n_p[_i, :] = (_i + 1, sum([get_p(1000, _i + 1) for _ in range(5)]) / 5)
    print('\r', end='')
    plt.plot(n_p[:, 0], n_p[:, 1])

    # 拟合正态分布的分布函数
    n_p_mean = (n_p[1:100, 1] - n_p[0:99, 1]) * n_p[0:99, 0]
    mean = n_p_mean.sum()
    n_p_var = (n_p[0:99, 0] - mean) ** 2 * (n_p[1:100, 1] - n_p[0:99, 1])
    std = math.sqrt(n_p_var.sum())
    print('N({}, {})'.format(mean, std))
    cdf = np.zeros((100, 2))
    for _i in range(100):
        cdf[_i, :] = (_i, st.norm.cdf(_i, mean, std))
    plt.plot(cdf[:, 0], cdf[:, 1])
    plt.show()

    while True:
        try:
            _m, _n = [int(x) for x in input().split()]
            print(get_p(_m, _n))
        except ValueError:
            break
