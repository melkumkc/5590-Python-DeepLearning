from sklearn import datasets
from sklearn.naive_bayes import MultinomialNB # importing class from naive bayes model
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn import datasets, metrics


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



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
y_pred = model.predict(X_test)
print ("Using another model of training size 80%: ")
print(metrics.accuracy_score(y_test, y_pred))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
y_pred = model.predict(X_test)
print ("Using another model of training size 70%: ")
print(metrics.accuracy_score(y_test, y_pred))

""" 
Remark: Using cross_val_score gives a better prediction because the accuracy of the prediciton is more accurate than the the train_test_split method, since it divides
the data into diffrent folds and uses diffrent train and test folds to come up with model accuracy prdiction. while the train_test_split method the result of the prediction
depends on the random samples chosen to do the training and testing this will result in less accurate prediction
"""