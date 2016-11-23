# -*- coding: utf-8 -*-
# author: jun ma
from libsvm.python.svmutil import *
import numpy as np


class SvmClassifier(object):
    def __init__(self):
        """
        """

    def parse(self, X, Y):
        """
        parser array data into libsvm style
        """
        prob_y = []
        prob_x = []
        for i in range(len(X)):
            xi = {}
            for j in range(len(X[0])):
                xi[int(j + 1)] = float(X[i][j])
            prob_y += [float(Y[i])]
            prob_x += [xi]
        return (prob_x, prob_y)

    def train(self, X, Y, options=None):
        """
        X, Y is the the input
        """
        m = svm_train(Y, X, options);
        return m;

    def predict(self, Xte, Yte, m):
        p_label, p_acc, p_val = svm_predict(Yte, Xte, m)
        res = {}
        res['acc'] = 0.1
        res['auc'] = 0.2
        res['err'] = 0
        return res;

    def roc(self):
        pass

    def auc(self):
        pass

    def err(self):
        pass


svm = SvmClassifier()

Y = [0, 1, 0, 1]
X = [[1, 2, 3, 4], [2, 3, 4, 5], [1, 2, 4, 5], [1, 2, 6, 5]]
prob_x, prob_y = svm.transform(X, Y)
print isinstance(prob_x, (list, tuple))
m = svm.train(prob_y[:3], prob_x[:3], '-c 4')
# print prob_x[3:]
# predict = svm.predict(prob_y, prob_x, m)

# print predict
# y, x = svm_read_problem('data/iris.scale.txt')
# m = svm_train(y[:140], x[:140], '-c 4')
# print x[140:]
# p_label, p_acc, p_val = svm_predict(y[140:], x[140:], m)
# print p_acc
