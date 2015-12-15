#! /usr/bin/env python3
from classifier import classifier_report
from sklearn.svm import SVC

# Polykernel
print('Testing Polykernel')
for d in range(1, 4):
    for c in range(-2, 3):
        cost = 10**c
        print('starting: degree = {0}, cost = {1}'.format(d, cost))
        classifier_report(SVC(kernel='poly', degree=d, C=cost))
        print('finished: degree = {0}, cost = {1}'.format(d, cost))


# Gaussian RBF Kernel
print('Testing RBF')
for g in range(-2, 3):
    for c in range(-2, 3):
        cost = 10**c
        gamma = 10**g
        print('starting: gamma = {0}, cost = {1}'.format(gamma, cost))
        classifier_report(SVC(kernel='rbf', gamma=gamma, C=cost))
        print('finished: gamma = {0}, cost = {1}'.format(gamma, cost))
