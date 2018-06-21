from sklearn import datasets
from sklearn.naive_bayes import MultinomialNB # importing class from naive bayes model
from sklearn.cross_validation import cross_val_score


iris = datasets.load_iris() # importing iris data set

X = iris.data # storing feature matrix
y = iris.target # storing response(target) vector


model = MultinomialNB() # creating object
model.fit(X,y) # Fitting the data set into the model
scores = cross_val_score (model,X,y,cv =10,scoring="accuracy") # calculating accuracy scores by creating testing and learning parts
""" 
Finding the accuracy score using the cross validation score, the data is split into equal 10 folds, from which one will be testing set and the other 9 will be
training sets. Ten scores will be found since we are iterating 10 times by changing the training and testing set.
"""
a = scores.mean()* 100
print ("The accuracy of each itteration is: {}".format (scores))
print ("The mean accuracy is : {} %".format (a))


