#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

t0 = time()

gnb = GaussianNB()

gnb.fit(features_train, labels_train)

t1 = time()
print("Training time: ", t1-t0)


pred = gnb.predict(features_test)
t2 = time()

print("Prediction time: ", t2-t1)

acc = accuracy_score(labels_test, pred)

print("Accuracy = ", acc)




#########################################################


