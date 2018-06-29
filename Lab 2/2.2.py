import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
#from sklearn.datasets import load_breast_cancer
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC

cancer = datasets.load_breast_cancer() # importing data set

X = cancer.data # storing feature matrix
y = cancer.target # storing response(target) vector

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2) # spliting the data into training and testing sets
model = SVC (kernel="linear") #  creating object of the model (instantiating) linear kernel
model.fit (X_train,y_train) # fitting the training data into the model
y_pred = model.predict(X_test) # predicting the dependent variable from the test data
print ("The accuracy of using linear kernel with test size of 20%: ")
print(metrics.accuracy_score(y_test, y_pred))


model = SVC (kernel= "rbf" ) # creating object of the model rbf kernel
model.fit (X_train,y_train) # fitting the training data into the set
y_pred = model.predict(X_test) # predicting the dependent variable from the test data
print ("The accuracy of using RBF kernel with test size of 20%: ")
print(metrics.accuracy_score(y_test, y_pred))

""" 
Support vector machines are supervised learning models. The associated algorithms of SVM analyze data and recognize patterns.
This patterns are used for classification and regression analysis. For some data that are represented in two dimensions. The
data can be separated into two classes by a single linear line. The line can be chosen so that it can maximize the margin between the
classes. This approach of classification is known as linear kernel algorithm. Sometimes it might be better to classify the data by 
using a single point and computing the distance between this point and the centroids of the cluster, this approach is called radial
base function kernel.
In this data set a better result was obtained by using linear kernel.
"""