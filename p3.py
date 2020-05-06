import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import perm


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
    if input('跳过统计分析？(y/N) ').lower() != 'y':
        for _j, _m in enumerate((1000, 2000, 5000, 10000)):
            # 每班人数 1 ~ 100 进行统计分析
            n_p = np.zeros((100, 3))
            for _i in range(100):
                print('\r{:.0f}% ({}/4)'.format((_i / 10) ** 2, _j + 1), end='')  # 进度
                n_p[_i, :] = (
                    _i + 1,
                    sum([get_p(_m, _i + 1) for _ in range(5)]) / 5,  # 五次取平均
                    1 - perm(365, _i, exact=True) / 365 ** _i,  # 1-P(365,N)/365^N
                )
            print('\r', end='')
            plt.plot(n_p[:, 0], n_p[:, 1])
            plt.plot(n_p[:, 0], n_p[:, 2])
            plt.savefig('p3_figures/m={}.png'.format(_m))
            plt.show()

    # 用户输入
    while True:
        try:
            _m, _n = [int(x) for x in input('请输入M和N的值(如 1000 30): ').split()]
            print(get_p(_m, _n))
        except ValueError:
            break
