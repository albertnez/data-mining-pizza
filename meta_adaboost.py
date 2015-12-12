#! /usr/bin/env python3
from classifier import classifier_report
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Decission tree
print('Decision tree:')
classifier_report(AdaBoostClassifier(DecisionTreeClassifier()))

# Decission stumps
print('Decision stump:')
classifier_report(AdaBoostClassifier(DecisionTreeClassifier(max_depth=1)))
