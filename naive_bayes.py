#! /usr/bin/env python3
from classifier import classifier_report
from sklearn.naive_bayes import BernoulliNB

classifier_report(BernoulliNB())
