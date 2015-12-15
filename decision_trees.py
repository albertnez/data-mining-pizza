#! /usr/bin/env python3
from classifier import classifier_report
from sklearn.tree import DecisionTreeClassifier

classifier_report(DecisionTreeClassifier(max_depth=10))


