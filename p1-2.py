import random


def distinct(seq, key=None):
    appeared = set()
    for k in seq:
        v = k if key is None else key(k)
        if v not in appeared:
            appeared.add(v)
            yield v


def verify(seq: list):
    return len(set(seq)) == len(seq)


def case_list():
    seq = [random.randint(1, 10) for _ in range(20)]
    print('去重前', seq)
    print('去重后', list(distinct(seq)))
#
#
# def case_dict():
#     seq = {i: random.randint(1, 10) for i in range(20)}
#     print('去重前', seq)
#     print('去重后', list(distinct(seq, key=lambda x: seq[x])))


if __name__ == '__main__':
    case_list()
    # case_dict()
