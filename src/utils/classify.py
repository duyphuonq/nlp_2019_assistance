# -*- coding: utf-8 -*
import csv
from src.constants import ROOT_DIR, path_data, path_new_data, data_name

path = ROOT_DIR + path_data

myDict = {

}

myArr = []

if __name__ == '__main__':
    with open(path + data_name, mode='r', encoding="utf8") as csv_file:
        with open(path + 'dataCount.csv', mode='w', encoding="utf8", newline='\n') as write_file:
            csv_reader = csv.DictReader(csv_file)
            fieldnames = ['word', 'count', "index"]
            csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
            with open(path + 'label_train.txt', mode='w') as label_file:
                for row in csv_reader:
                    target = row["sentence"]
                    label_file.write(row['label'])
                    label_file.write('\n')
                    for word in target.split():
                        if not (word in myDict):
                            myDict[word] = 1
                            myArr.append(word)
                        else:
                            myDict[word] += 1
                myArr.sort()
                cur=0
                csv_writer.writeheader()
                for word in myArr:
                    csv_writer.writerow({'word': word, 'count': myDict[word], 'index': cur})
                    cur+=1
