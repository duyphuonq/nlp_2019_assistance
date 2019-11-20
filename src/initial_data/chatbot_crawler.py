# -*- coding: utf-8 -*

import requests
import time
import random

specials = [',', '.', '?', '!', '~', '`', '#', '@', '%', '^', '&', '*', '(', ')', ':', ';', '\'', '\"', '/', '-', '_', '+', '=']

def normalize(sentence):
    ans = ""
    for i in range(len(sentence)):
        cur = sentence[i]
        if cur not in specials:
            if cur.isupper():
                cur = cur.lower()
            ans += cur
    return ans


def random_string():
    lim = random.randint(1, 10)
    res = str(time.time()) + str(random.randint(1, 1000))
    for i in range(lim):
        res += str(chr(random.randint(0, 25) + ord('a')))
    return res


def remove_duplicated():
    fn = "crawl_bka.txt"
    myDict = {}
    with open(fn, 'r') as read_file:
        with open('final.txt', 'w') as write_file:
            for row in read_file:
                sentence = row.split(',')[0]
                if sentence not in myDict:
                    myDict[sentence] = 1
            print(len(myDict))
            for key, value in myDict.items():
                write_file.write(key)
                write_file.write(',')
                write_file.write('2')
                write_file.write('\n')


def do_crawl():
    URL = "http://undertheseanlp.com:8000/chatbot"

    myDict = {}
    limit = 10000

    with open('crawl_bka.txt', 'a') as write_file:
        while limit > 0:
            limit -= 1
            current_sentence = random_string()
            user = random_string()
            ok = True

            while ok:

                _data = '{\"text\": \"%s\", \"user\": \"%s\"}' % (current_sentence, user)
                #print(_data)

                r = requests.post(url = URL, data = _data.encode('utf-8'), headers={'Content-type': 'application/json; charset=utf-8'})

                #print(r.status_code, r.reason)
                #print(r)
                resp = r.json()
                if 'output' in resp: 
                    initial_output = resp['output']
                    #print(initial_output)
                    res = normalize(initial_output)

                    if res in myDict:
                        ok = False
                    else:
                        myDict[res] = 1
                        current_sentence = resp['output']
                        print(res)
                else:
                    ok = False

        print(len(myDict))
        for key, value in myDict.items():
            write_file.write(key)
            write_file.write(',')
            write_file.write('2')
            write_file.write('\n')


do_crawl()
remove_duplicated()
            
