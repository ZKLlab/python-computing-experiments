import math
from itertools import count

if __name__ == '__main__':
    print('+{:-^5}+{:-^22}+{:-^22}+{:-^22}+'.format('', '', '', ''))
    print('|{:^5}|{:^22}|{:^22}|{:^22}|'.format('k', 'Ramanujan', 'math.pi', 'error'))
    print('+{:-^5}+{:-^22}+{:-^22}+{:-^22}+'.format('', '', '', ''))
    xs = 2 * 2 ** 0.5 / 9801  # 系数
    _sum = 0.0  # 倒数和
    for k in count():
        fz = math.factorial(4 * k) * (1103 + 26390 * k)  # 分子
        fm = math.factorial(k) ** 4 * 396 ** (4 * k)  # 分母
        diff = xs * fz / fm  # 项
        _sum += diff
        print('|{:^5d}|{:^22.16f}|{:^22.16f}|{:^22.16f}|'.format(k, 1 / _sum, math.pi, abs(1 / _sum - math.pi)))
        if diff < 1e-15:
            break
    print('+{:-^5}+{:-^22}+{:-^22}+{:-^22}+'.format('', '', '', ''))
