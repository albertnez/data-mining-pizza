#! /usr/bin/env python3
from classifier import classifier_report
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

# Decission tree
print('Decision tree:')
classifier_report(BaggingClassifier(DecisionTreeClassifier()))

# Decission stumps
print('Decision stump:')
classifier_report(BaggingClassifier(DecisionTreeClassifier(max_depth=2)))
