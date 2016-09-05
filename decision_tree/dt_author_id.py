#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("/Users/Vickykiki/Desktop/ud120-projects-master/decision_tree/tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree
clf1 = tree.DecisionTreeClassifier(min_samples_split=40)
clf1 = clf1.fit(features_train, labels_train)
pred1 = clf1.predict(features_test)

acc_min_samples_split_40 = float((pred1==labels_test).sum())/len(labels_test)
print acc_min_samples_split_40
#########################################################


