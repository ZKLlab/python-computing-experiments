import csv
import os
import string
from collections import Counter

if __name__ == '__main__':

    for file_name in os.listdir('p4_cases'):
        if file_name.endswith('.txt'):
            with open(os.path.join('p4_cases', file_name)) as fp:
                text = fp.read()

            words = list(map(lambda w: w.strip(string.punctuation).lower(), text.split()))
            counter_words = Counter(words)
            most_common = counter_words.most_common()

            # (1)

            with open(os.path.join('p4_q1_results', f'{file_name}.csv'), 'w') as fp:
                writer = csv.writer(fp)
                writer.writerows(most_common)

            # (2)

            words = ['the', 'star', 'is', 'in', 'my', 'computer']
            words_count = list(map(lambda word: (word, counter_words.get(word, 0)), words))

            with open(os.path.join('p4_q2_results', f'{file_name}.csv'), 'w') as fp:
                writer = csv.writer(fp)
                writer.writerows(words_count)
