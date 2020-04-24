import time


# 递归查找
def find(w: str):
    global max_len, words_set, succeed_words_set, failed_words_set
    if len(w) > 1:
        for i in range(len(w)):
            nw = w[:i] + w[i + 1:]
            if nw in succeed_words_set or (nw in words_set and nw not in failed_words_set and find(nw) is not None):
                break
        else:
            failed_words_set.add(w)
            return None
    succeed_words_set.add(w)
    max_len = max(max_len, len(w))
    return w


if __name__ == '__main__':
    # 制作词表
    with open('words.txt') as fp:
        words_list = [x.strip() for x in fp]
    words_list = [x for x in words_list if 'a' in x or 'i' in x]
    words_list.append('a')
    words_list.append('i')
    words_list.sort()

    start = time.time()

    words_set = set(words_list)  # 全部词集
    succeed_words_set = set()  # 成功词集
    failed_words_set = set()  # 失败词集
    max_len = 1
    result = 'a'
    for word in words_list:
        if len(word) > max_len:
            sub_result = find(word)
            if sub_result is not None:
                result = sub_result

    end = time.time()

    print(result)
    print(end - start, 's')
