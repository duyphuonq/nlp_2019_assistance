# -*- coding: utf-8 -*
import csv


def get_count(word):
    with open('dataCount.csv', mode='r', encoding="utf8") as csv_file:
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
    with open('dataCount.csv', mode='r', encoding="utf8") as csv_file:
        csv_store_reader = csv.DictReader(csv_file)
        arr = []
        for row_dict in csv_store_reader:
            arr.append([row_dict["word"], row_dict["count"], row_dict["index"]])
        for row in arr:
            if row[0] == word:
                return row[2]
        return 0
    return 0


def get_dict_size():
    with open('dataCount.csv', mode='r', encoding="utf8") as csv_file:
        csv_store_reader = csv.DictReader(csv_file)
        arr = []
        ans = 0
        for row_dict in csv_store_reader:
            ans = max(ans, int(row_dict["index"]))
        return ans + 1
    return 0


if __name__ == '__main__':
    print(get_dict_size())
    print(get_count("mở"))
    print(get_index("mở"))
    exit(0)
    with open('dataCount.csv', mode='r', encoding="utf8") as csv_file:
        with open('data.csv', mode='r', encoding="utf8", newline='\n') as raw_file:
            csv_store_reader = csv.DictReader(csv_file)
            arr = []
            for row_dict in csv_store_reader:
                arr.append([row_dict["word"], row_dict["count"], row_dict["index"]])
            arr_sentences = []
            csv_raw_reader = csv.DictReader(raw_file)
            for row in csv_raw_reader:
                arr_sentences.append([row["sentence"], row["label"]])
            with open('data_test.txt', mode='w', encoding="utf8") as write_file:
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
                                            write_file.write(str(cnt))
                                            write_file.write(" ")
                                            write_file.write(row_dict[2])
                                            write_file.write(" ")
                                            write_file.write(row_dict[1])
                                            write_file.write("\n")
                                            break
                                break
            with open('data_train.txt', mode='w', encoding="utf8") as write_file:
                cnt = 0
                for row in arr_sentences:
                    cnt += 1
                    target = row[0]
                    for word in target.split():
                        for row_dict in arr:
                            if word == row_dict[0]:
                                write_file.write(str(cnt))
                                write_file.write(" ")
                                write_file.write(row_dict[2])
                                write_file.write(" ")
                                write_file.write(row_dict[1])
                                write_file.write("\n")
                                break
                    
