#! /usr/bin/env python3
from classifier import classifier_report
from sklearn.svm import SVC

classifier_report(SVC())
