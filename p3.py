import time

if __name__ == '__main__':

    with open('words.txt') as fp:
        word_list = fp.readlines()

    result = []

    t1 = time.time()

    word_list = list(map(lambda w: w.strip(), word_list))
    word_set = set(word_list)

    for word in word_list:
        reversed_word = word[::-1]
        if reversed_word != word and reversed_word in word_set:
            result.append((word, reversed_word))

    t2 = time.time()

    for row in result:
        print(*row)
    print('\n', t2 - t1, 's')
