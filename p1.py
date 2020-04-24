import math
from itertools import count

if __name__ == '__main__':
    xs = 2 * 2 ** 0.5 / 9801  # 系数
    _sum = 0.0  # 倒数和
    for k in count():
        fz = math.factorial(4 * k) * (1103 + 26390 * k)  # 分子
        fm = math.factorial(k) ** 4 * 396 ** (4 * k)  # 分母
        diff = xs * fz / fm  # 项
        _sum += diff
        if diff < 1e-15:
            break
    print('my result : {:.16f}'.format(1 / _sum))
    print(' math.pi  : {:.16f}'.format(math.pi))
    print('  error   : {:.16f}'.format(abs(1 / _sum - math.pi)))
