import csv
from SED import get_SED, get_str_phoneme_len
from HeapTree import HeapTree

input_file_name = '59words.csv'
output_file_name = '59words_output.csv'
SED_count = 20

input_file = open(input_file_name, 'r', encoding = 'euc-kr')
csv_reader = csv.reader(input_file, delimiter=',')

line_count = 0
word_list = []
for row in csv_reader:
    if line_count == 0:
        line_count += 1
    else:
        word_list.append(row[0])
        line_count += 1
print(f'Loaded {line_count} lines.')
input_file.close()

output_file = open(output_file_name, 'w', encoding = 'euc-kr')
csv_writer = csv.writer(output_file, delimiter=',')

# write header
row = ['단어', '음소 개수', '평균 편집거리', '짧은 편집거리 ' + str(SED_count) + '개 평균']
for i in range(SED_count):
    row.append(i+1)

for word in word_list:
    row.append(word)
csv_writer.writerow(row)

line_count = 0

# write contents
for i, word1 in enumerate(word_list):
    # process for 1 word
    row_front = [word1]
    row_back = []

    heap_tree = HeapTree(SED_count)
    sum = 0
    min_sum = 0

    for j, word2 in enumerate(word_list):
        sed = get_SED(word1, word2)
        row_back.append(sed)
        sum += sed
        if i!=j:
            heap_tree.insert([sed,j])

    min_list = heap_tree.tree
    min_list = sorted(min_list, key=lambda x : x[0])

    for tuple in min_list:
        row_front.append(word_list[tuple[1]] + ' ' + str(tuple[0]))
        min_sum += tuple[0]

    row_front.insert(1, get_str_phoneme_len(word1))
    row_front.insert(2, sum/len(word_list))
    row_front.insert(3, min_sum/len(min_list))
    csv_writer.writerow(row_front + row_back)
    print(f' {line_count} lines done.')
    line_count += 1


output_file.close()
