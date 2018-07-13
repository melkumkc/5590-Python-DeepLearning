import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("census_data.csv") # importing data

""" convert the Lavel column to 0s and 1s instead of strings"""
def label_fix (label):
    if label == " <=50K":
        return 0
    else:
        return 1
data["income_bracket"]= data["income_bracket"].apply(label_fix)

""" Perform a train test split on the data"""
x_data = data.drop("income_bracket",axis=1)
y_labels = data["income_bracket"]
x_train, x_test, y_train, y_test = train_test_split(x_data,y_labels,test_size=0.3)

""" Create the Features columns for tf.estimator"""
gender = tf.feature_column.categorical_column_with_vocabulary_list("gender",["Female","Male"])
occupation = tf.feature_column.categorical_column_with_hash_bucket("occupation",hash_bucket_size=1000)
marital_status = tf.feature_column.categorical_column_with_hash_bucket("marital_status",hash_bucket_size=1000)
relationship= tf.feature_column.categorical_column_with_hash_bucket("relationship",hash_bucket_size=10)
education = tf.feature_column.categorical_column_with_hash_bucket("education",hash_bucket_size=1000)
workclass = tf.feature_column.categorical_column_with_hash_bucket("workclass",hash_bucket_size=1000)
native_country =tf.feature_column.categorical_column_with_hash_bucket("native_country",hash_bucket_size=1000)

age = tf.feature_column.numeric_column("age")
education_num = tf.feature_column.numeric_column("education_num")
capital_gain = tf.feature_column.numeric_column("capital_gain")
capital_loss = tf.feature_column.numeric_column("capital_loss")
hours_per_week = tf.feature_column.numeric_column("hours_per_week")
feat_cols = [gender,occupation,marital_status,relationship,education,workclass,native_country,age,education_num,capital_gain,capital_loss,hours_per_week]

""" Create input function"""
input_func = tf.estimator.inputs.pandas_input_fn(x=x_train,y=y_train,batch_size=100,num_epochs=None,shuffle=True)
# Create model with tf.estimator

model = tf.estimator.LinearClassifier(feature_columns=feat_cols)
model.train (input_fn=input_func,steps=100)


"""create prdiction input funcion"""

pred_fn = tf.estimator.inputs.pandas_input_fn(x=x_test,batch_size=len(x_test),shuffle=False)
pred_gen = model.predict(input_fn=pred_fn)
prediction= list(pred_gen)
final_preds = [pred['class_ids'][0] for pred in prediction]


print (classification_report (y_test,final_preds))

