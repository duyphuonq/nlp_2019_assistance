
from __future__ import division, print_function, unicode_literals
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score
from src.constants import path_data, ROOT_DIR
from src.utils.data_utils import get_dict_size

# data path and file name
# import os
# os.system('pwd')
# exit(0)
train_data_fn = ROOT_DIR + path_data + 'data_train_bka.txt'
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


def trained_model():
    (train_data, train_label)  = read_data(train_data_fn, train_label_fn)
    # (test_data, test_label)  = read_data(test_data_fn, test_label_fn)
    clf = MultinomialNB()
    clf.fit(train_data, train_label)
    print("train done")
    return clf
    #y_pred = clf.predict(test_data)
    #print('Training size = %d, accuracy = %.2f%%' % (train_data.shape[0],accuracy_score(test_label, y_pred)*100))


	
