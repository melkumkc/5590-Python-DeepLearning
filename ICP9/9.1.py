import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# Reading data
df = pd.read_csv ('house.csv', header=0, delimiter=",")
arr = np.array(df) # converting the input data into numpy array



# Assigning variables to input data

x_age = (arr[:50,1])/10
x_rooms = (arr[:50,2])/10

price = arr [:50,5]


# creating random slope and y-intercept

m_age = tf.Variable(0.7)
m_rooms = tf.Variable(0.9)

b_r = tf.Variable(0.6)
b_a = tf.Variable (0.4)

e_r = 0
e_a = 0
for x_r,p in zip (x_rooms,price):
    p_hat = m_rooms * x_r + b_r
    e_r += (p-p_hat)**2
for x_a,p in zip (x_age,price):
    p_hat = m_rooms * x_a + b_a
    e_a += (p-p_hat)**2

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train1 = optimizer.minimize (e_r)
train2 = optimizer.minimize(e_a)

init = tf.global_variables_initializer()

with tf.Session () as sess:
    sess.run(init)
    training_steps = 10000
    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)
    for i in range (training_steps):
        sess.run (train1)
        sess.run (train2)
    m_a,m_r,ba,br = sess.run([m_age,m_rooms,b_a,b_r])

    writer.close()




x_test = np.linspace (-2,100,1000)
y_a = m_a * x_test + br
plt.plot (x_age,price, ".")
plt.xlabel("Age")
plt.ylabel("Price")
plt.title ("Age vs Price")
plt.plot (x_test,y_a,"b")
plt.show()

plt.plot (x_rooms,price, "x")
y_r = m_r * x_test + br
plt.plot (x_test,y_r, "r")
plt.xlabel("Room Area")
plt.ylabel("Price")
plt.title ("Room Area vs Price")
plt.show()

print ("weight of age: {}".format (m_a))
print ("Bias for age: {}".format (ba))
print ("weihgt of room: {}".format (m_r))
print ("Bias for room: {}".format (br))


