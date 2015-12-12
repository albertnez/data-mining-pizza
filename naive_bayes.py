#! /usr/bin/env python3
import numpy as np
import pandas as pd
import math
import random
from sklearn.naive_bayes import BernoulliNB
from sklearn import cross_validation

df = pd.read_csv('output.csv', delim_whitespace=True)

# Divide data frame to feature and target
feature = df.ix[:,0:len(df.columns)-1].values
target = df.ix[:,-1].values

# Total number of entries
N = len(target)

clf = BernoulliNB()

#Simple K-Fold cross validation. 10 folds.
cv = cross_validation.KFold(N, n_folds=10)
results = []
for traincv, testcv in cv:
    model = clf.fit(feature[traincv], target[traincv])
    prediction = model.predict(feature[testcv])

    # Count the number of errors.
    diff = target[testcv] != prediction
    nerrors = sum(diff)
    percError = nerrors/len(prediction)
    results.append(percError)

print ("Results:", str(np.array(results).mean()))
