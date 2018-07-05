import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import xlrd

# Reading data
DATA_FILE = 'smoking.xls'
book = xlrd.open_workbook(DATA_FILE,encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray ([sheet.row_values(i) for i in range (1,sheet.nrows)])

""" lists to identify smokers and none smokers"""
smoker = []
none_smoker = []
""" Identifying and appending smokers and none smokers to the appropriate list"""
i = 0
while i < len(data):
    if data[i,0]==1:
        smoker.append(data[i])
    else:
        none_smoker.append(data[i])
    i+= 1

""" Changing the list into a numpy array"""
a_smoker = np.array(smoker)
a_none_smoker = np.array (none_smoker)


smoker_survival = [] # smokers who survived
smoker_dead = []
none_smoker_survival = [] # none smokers who survived
none_smoker_dead = []

""" from the smokers list identifying those who survived and died"""
i= 0
while i < len(a_smoker):
    if a_smoker[i,2] == 0:
        smoker_survival.append (smoker[i])
    else:
        smoker_dead.append(smoker[i])
    i += 1
a_smoker_survival = np.array (smoker_survival) # array of smokers

""" from the none smokers list identifying those who survived and died"""
while i < len(a_none_smoker):
    if a_none_smoker[i,2] == 0:
        none_smoker_survival.append (smoker[i])
    else:
        none_smoker_dead.append(smoker[i])
    i += 1

a_none_smoker_survival = np.array (none_smoker_survival) # none smokers array

"""  
smoke_dead = m1* x_somk + m2* x_age + b1
smoke_survival = m3 * x_smoke + m4 * x_age + b2
number_smoker = smoke_dead + smoke_survival
number_smoker = (m1+m3)*x_smok + (m2 + m4) * x_age + b
number_smoker = m_s + m_a * age + b

"""
# Assigning values to the variables and biase
m_s = tf.Variable(0.7) # weight for smoking
m_a = tf.Variable (0.6) # weight for age
m_n_s = tf.Variable(0.7)# weight for non smoking
b = tf.Variable (0.5) # bias for smokers
b1 = tf.Variable(0.3) # bias for non smokers
error = 0
error1 = 0

# calculating error for the smokers model
for x_a,n_s, in zip (a_smoker[:,1],a_smoker[:,3]): # x_a = age values
    y = m_s + m_a *x_a + b
    error += (y - n_s)**2

# calculating error for non smokers model
for x_a,n_n_s, in zip (a_none_smoker[:,1],a_none_smoker[:,3]): # x_a = age values
    y = m_s + m_a *x_a + b1
    error1 += (y - n_n_s)**2

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize (error)
train1 = optimizer.minimize (error1)

init = tf.global_variables_initializer() # intializing global variables

with tf.Session() as sess:
    sess.run(init)
    training_steps = 10000

    for i in range(training_steps):
        sess.run(train1)
        sess.run(train)
    w_s, w_a, bi = sess.run([m_s,m_a,b])
    w_n_s, bi1 = sess.run ([m_n_s,b1])



x_test = np.linspace (-2,50,10)
y_s = w_s +  x_test*w_a + bi # smokers regression model
y_n = w_n_s + x_test*w_n_s + bi1 # none smokers regression model
y = w_s +  x_test*w_a + bi + w_n_s + x_test*w_n_s + bi1

plt.plot (data [:,1],data[:,3], ".")
plt.plot (x_test,y_s,"b")
plt.plot (x_test,y_n,"r")
plt.plot (x_test, y, "b--")
plt.xlabel("Age")
plt.ylabel("Survival")
plt.title ("Age vs Survival \n       Blue line = smokers survival with age, Red line = none smokers survival with age")
plt.show()


