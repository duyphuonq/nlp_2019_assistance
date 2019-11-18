
from __future__ import division, print_function, unicode_literals
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score
from src.constants import path_data, ROOT_DIR
from src.utils.data_utils import get_dict_size
from sklearn.model_selection import train_test_split

# data path and file name
# import os
# os.system('pwd')
# exit(0)
train_data_fn = ROOT_DIR + path_data + 'data_train.txt'
train_label_fn = ROOT_DIR + path_data + 'label_train.txt'


def read_data(data_fn, label_fn=None):

    nwords = get_dict_size()
    label = [1]
    if label_fn is not None:
        with open(label_fn) as f:
            content = f.readlines()
        label = [int(x.strip()) for x in content]

    with open(data_fn) as f:
        content = f.readlines()

    content = [x.strip() for x in content] 

    dat = np.zeros((len(content), 3), dtype = int)
    for i, line in enumerate(content): 
        a = line.split(' ')
        a[2] = str(int(a[2]) + 1)
        dat[i, :] = np.array([int(a[0]), int(a[1]), int(a[2])])
    data = coo_matrix((dat[:, 2], (dat[:, 0] - 1, dat[:, 1] - 1)), shape=(len(label), nwords))
    if label_fn is not None:
        return data, label
    return data


def trained_model(x, y):
    clf = BernoulliNB()
    clf.fit(x, y)
    print("train done")
    return clf


def test_accuracy():
    mean_result = 0
    limit = 100
    for i in range(limit):
        (train_data, train_label) = read_data(train_data_fn, train_label_fn)
        x, x_test, y, y_test = train_test_split(train_data, train_label, test_size=0.1, train_size=0.9)
        clf = trained_model(x, y)
        y_pred = clf.predict(x_test)
        local_result = accuracy_score(y_test, y_pred) * 100
        print("Times: {} ({}%)".format(i + 1, local_result))
        mean_result += local_result
    print('Average Accuracy = {:.2f}%'.format(mean_result / limit))


test_accuracy()
