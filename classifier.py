#! /usr/bin/env python3
import pandas as pd
from sklearn import metrics
from sklearn import cross_validation

data = pd.read_csv('output.csv', delim_whitespace=True)
# Divide data frame to feature and target
feature = data.ix[:,0:len(data.columns)-1].values
target = data.ix[:,-1].values

def classifier_report(classifier, cv=10):
    # Total number of entries
    N = len(target)

    #Simple K-Fold cross validation. 10 folds.
    results = cross_validation.cross_val_predict(classifier, feature, target, cv=cv)

    # print classification report and confusion matrix
    print(metrics.classification_report(target, results))
    print(metrics.confusion_matrix(target, results))
