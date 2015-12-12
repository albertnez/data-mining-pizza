#! /usr/bin/env python3
import numpy as np
import pandas as pd
import math
import random
from sklearn.naive_bayes import BernoulliNB

PIZZA_FIELD = '@@requester_received_pizza@@'

df = pd.read_csv('output.csv', delim_whitespace=True)

# Divide data frame to features and targets
features = df.ix[:,1:len(df.columns)].values
targets = df.ix[:,-1].values

# Total number of entries
N = len(targets)

# Divide data to learning and testing set, where the learning has 2/3 of the data.
# learning/testing contain the indices of elements that are part of the learning/testing set.
learning = random.sample(range(N),math.floor(2*N/3))
testing = list(set(range(N))-set(learning))

nlearning = len(learning)
ntesting = len(testing)
