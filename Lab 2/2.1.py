import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
#from sklearn.datasets import load_breast_cancer
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


iris = datasets.load_iris() # importing iris data set

X = iris.data # storing feature matrix
y = iris.target # storing response(target) vector

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2) # spliting the data into training and testing sets

model = LinearDiscriminantAnalysis(n_components=4) # choosing the number of components for the classification
model.fit(X_train, y_train) # fitting the trining data into the model

y_pred = model.predict(X_test) # predicting the value of the dependent variable using the testing data
print ("The accuracy of using linear discriminant analysis with test size of 20%: ")
print(metrics.accuracy_score(y_test, y_pred))