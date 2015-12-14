#! /usr/bin/env python3
from classifier import classifier_report
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

# Decission tree
print('Decision tree:')
classifier_report(BaggingClassifier(base_estimator=DecisionTreeClassifier()))

# Decission stumps
print('Decision stump:')
classifier_report(BaggingClassifier(base_estimator=DecisionTreeClassifier(max_depth=1),n_estimators=100))
