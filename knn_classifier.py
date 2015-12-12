#! /usr/bin/env python3

from classifier import classifier_report
from sklearn.neighbors import KNeighborsClassifier

neighbors = range(1,8)
for n in neighbors:
	print('----------' + str(n) + ' neighbors ----------')
	classifier_report(KNeighborsClassifier(n_neighbors=n))