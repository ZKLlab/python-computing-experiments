import math
import random

import matplotlib.pyplot as plt
import numpy as np


def get_p(m: int, n: int):
    q = 0
    for i in range(m):
        s = [False] * 365
        for j in range(n):
            day = random.randint(1, 365)
            if s[day - 1]:
                q += 1
                break
            else:
                s[day - 1] = True
    return q / m


if __name__ == '__main__':
    f365 = math.factorial(365)
    if input('跳过统计分析？(y/N) ').lower() != 'y':
        # 1000个班级，每班人数 1 ~ 365 进行统计分析
        _m = 1000
        n_p = np.zeros((365, 3))
        for _i in range(365):
            print('\r{:.0f}%'.format((_i / 36.5) ** 2), end='')  # 进度
            # N = _i + 1
            n_p[_i, :] = (
                _i + 1,
                sum([get_p(_m, _i + 1) for _ in range(3)]) / 3,  # 三次取平均
                1 - f365 / (365 ** (_i + 1) * math.factorial(364 - _i)),  # 理论值
            )
        print('\r', end='')
        plt.figure(figsize=(12, 4))
        plt.plot((1, 365), (0.5, 0.5), c='#9E9E9E', linestyle=':')
        plt.plot((23, 23), (0, 1), c='#9E9E9E', linestyle=':')
        plt.plot(n_p[:, 0], n_p[:, 2], c='#FF9800', label='Calculated result')
        plt.scatter(n_p[:, 0], n_p[:, 1], c='#3F51B5', marker='x', label='Experimental result')
        plt.annotate('(23, 0.5)', xy=(23, 0.5), xytext=(25, 0.44))
        plt.xlabel('N')
        plt.ylabel('P')
        plt.legend()
        plt.savefig('p3_figures/m={}.png'.format(_m))
        plt.show()

    # 用户输入
    while True:
        try:
            _m, _n = [int(x) for x in input('请输入M和N的值(如 1000 30): ').split()]
            print(get_p(_m, _n))
        except ValueError:
            break
