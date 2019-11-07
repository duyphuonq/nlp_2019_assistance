# -*- coding: utf-8 -*
import csv

myDict = {

}

myArr = []

if __name__ == '__main__':
    with open('data.csv', mode='r', encoding="utf8") as csv_file:
        with open('dataCount.csv', mode='w', encoding="utf8", newline='\n') as write_file:
            csv_reader = csv.DictReader(csv_file)
            fieldnames = ['word', 'count', "index"]
            csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
            for row in csv_reader:
                target = row["sentence"]
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
