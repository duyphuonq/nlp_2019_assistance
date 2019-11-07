# -*- coding: utf-8 -*
import csv
import random
import time
from src.constants import ROOT_DIR, path_data, path_new_data

path = ROOT_DIR + path_data
#os.system("pwd")
#exit(0)


def get_count(word):
    with open(path + 'dataCount.csv', mode='r', encoding="utf8") as csv_file:
        csv_store_reader = csv.DictReader(csv_file)
        arr = []
        for row_dict in csv_store_reader:
            arr.append([row_dict["word"], row_dict["count"], row_dict["index"]])
        for row in arr:
            if row[0] == word:
                return row[1]
        return 0
    return 0


def get_index(word):
    with open(path + 'dataCount.csv', mode='r', encoding="utf8") as csv_file:
        csv_store_reader = csv.DictReader(csv_file)
        arr = []
        for row_dict in csv_store_reader:
            arr.append([row_dict["word"], row_dict["count"], row_dict["index"]])
        for row in arr:
            if row[0] == word:
                return int(row[2])
        return 0
    return 0


def get_dict_size():
    with open(path + 'dataCount.csv', mode='r', encoding="utf8") as csv_file:
        csv_store_reader = csv.DictReader(csv_file)
        ans = 0
        for row_dict in csv_store_reader:
            ans = max(ans, int(row_dict["index"]))
        return ans + 1
    return 0


def file_writing(_file, _data):
    n = len(_data)
    for i in range(n):
        _file.write(str(_data[i]))
        if i == n - 1:
            _file.write('\n')
        else:
            _file.write(' ')


def data_in_file(sequence):
    words = sequence.split()
    name = str(time.time()) + str(random.randint(1, 1000)) + ".txt"
    with open(path + '../new_data/' + name, 'w') as out_file:
        for word in words:
            if get_index(word) != 0:
                file_writing(out_file, [1, get_index(word) + 1, get_count(word)])
    return name


if __name__ == '__main__':
    print(get_dict_size())
    print(get_count("mở"))
    print(get_index("mở"))
    print(data_in_file("tui muốn mở pinta"))
    # exit(0)
    with open(path + 'dataCount.csv', mode='r', encoding="utf8") as csv_file:
        with open(path + 'data.csv', mode='r', encoding="utf8", newline='\n') as raw_file:
            csv_store_reader = csv.DictReader(csv_file)
            arr = []
            for row_dict in csv_store_reader:
                arr.append([row_dict["word"], row_dict["count"], row_dict["index"]])
            arr_sentences = []
            csv_raw_reader = csv.DictReader(raw_file)
            for row in csv_raw_reader:
                arr_sentences.append([row["sentence"], row["label"]])
            with open(path + 'data_test.txt', mode='w', encoding="utf8") as write_file:
                lim = 20
                cnter = [0] * 4
                for i in range(4):
                    if cnter[i] < lim:
                        cnt = 0
                        for row in arr_sentences:
                            cnt += 1
                            if int(row[1]) == i:
                                target = row[0]
                                cnter[i] += 1
                                #arr_sentences.remove(row)
                                for word in target.split():
                                    for row_dict in arr:
                                        if word == row_dict[0]:
                                            file_writing(write_file, [cnt, int(row_dict[2]) + 1, row_dict[1]])
                                            write_file.write(str(cnt))
                                            write_file.write(" ")
                                            write_file.write(row_dict[2])
                                            write_file.write(" ")
                                            write_file.write(row_dict[1])
                                            write_file.write("\n")
                                            break
                                break
            with open(path + 'data_train.txt', mode='w', encoding="utf8") as write_file:
                cnt = 0
                for row in arr_sentences:
                    cnt += 1
                    target = row[0]
                    for word in target.split():
                        for row_dict in arr:
                            if word == row_dict[0]:
                                file_writing(write_file, [cnt, int(row_dict[2]) + 1, row_dict[1]])
                                break
                    
