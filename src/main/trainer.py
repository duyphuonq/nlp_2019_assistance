
from __future__ import division, print_function, unicode_literals
import numpy as np
import time
from scipy.sparse import coo_matrix
from sklearn.metrics import accuracy_score
from src.constants import path_data, ROOT_DIR
from src.utils.data_utils import get_dict_size
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

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


models = {
    "svm": SGDClassifier(tol = 1e-3, max_iter = 100),
    "naive-bayes-0": BernoulliNB(),
    "naive-bayes-1": MultinomialNB(),
    "knn": KNeighborsClassifier(n_neighbors=1),
    "svc": LinearSVC(),
    "logistic-regression": LogisticRegression(random_state = 0, multi_class='auto', solver='lbfgs'),
    "random-forest": RandomForestClassifier(n_estimators = 100, max_depth = 3, random_state = 0)
}

models_name = {
    "svm": "SVM",
    "naive-bayes-0": "Bernoulli NB",
    "naive-bayes-1": "Multinomial NB",
    "knn": "KNN",
    "svc": "Linear SVC",
    "logistic-regression": "Logistic Regression",
    "random-forest": "Random Forest"
}


def trained_model(name, x, y):
    clf = models[name]
    clf.fit(x, y)
    # print("train done")
    return clf


def test_accuracy(name):
    mean_result = 0
    limit = 100
    average_time = 0
    for i in range(limit):
        start_time = time.time()

        (train_data, train_label) = read_data(train_data_fn, train_label_fn)
        x, x_test, y, y_test = train_test_split(train_data, train_label, test_size=0.1, train_size=0.9)
        clf = trained_model(name, x, y)
        y_pred = clf.predict(x_test)
        local_result = accuracy_score(y_test, y_pred) * 100
        # print("Times: {} ({}%)".format(i + 1, local_result))
        mean_result += local_result

        elapsed_time = time.time() - start_time
        average_time += elapsed_time

    average_time /= limit
    print(
        'Average results after {} iterations of {}:\nAverage Accuracy: {:.2f}%.\nAverage time elapsed: {:.2f}ms\n'
            .format(
            limit,
            models_name[name],
            mean_result / limit,
            average_time
        )
    )


test_accuracy("naive-bayes-0")
test_accuracy("naive-bayes-1")
test_accuracy("svm")
test_accuracy("knn")
test_accuracy("svc")
test_accuracy("logistic-regression")
test_accuracy("random-forest")

# Average results after 100 iterations of Bernoulli NB:
# Average Accuracy: 90.74%.
# Average time elapsed: 0.02ms
#
# Average results after 100 iterations of Multinomial NB:
# Average Accuracy: 90.68%.
# Average time elapsed: 0.02ms
#
# Average results after 100 iterations of SVM:
# Average Accuracy: 94.56%.
# Average time elapsed: 0.03ms
#
# Average results after 100 iterations of KNN:
# Average Accuracy: 88.82%.
# Average time elapsed: 0.03ms
#
# Average results after 100 iterations of Linear SVC:
# Average Accuracy: 95.94%.
# Average time elapsed: 0.04ms
#
# Average results after 100 iterations of Logistic Regression:
# Average Accuracy: 97.36%.
# Average time elapsed: 0.08ms
#
# Average results after 100 iterations of Random Forest:
# Average Accuracy: 63.82%.
# Average time elapsed: 0.36ms
