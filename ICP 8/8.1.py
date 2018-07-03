import tensorflow as tf


""" Inputing values to construct the metrices """

x = int (input ("Enter the size of the square matrix: "))
y = int (input ("Range of values for the metrices, from 0 to .... "))


"""Creating tensor objects; array of dimension x *x; having random elements of range 0 to y; type int """

a = tf.random_uniform((x,x),0,y,tf.int32)
b = tf.random_uniform((x,x),0,y,tf.int32)
c = tf.random_uniform((x,x),0,y,tf.int32)


""" Assigning variables for tensorflow operations"""

power = tf.pow(a,2) # square a^2
mat_add = tf.add (b,power) # addition a^2 + b
mat_multi = tf.matmul (mat_add, c) # multiplication (a^2 + b) *c; matrix multipcation
mat_multi2 = tf.multiply (mat_add, c) # multiplication (a^2 + b) *c; normal multipication


# creating tensorflow session (executing the graph)

with tf.Session() as sess:
     m,add,result,result2 = sess.run ([power,mat_add,mat_multi,mat_multi2])


print ("a^2 = \n", m)
print ("a^2 + b = \n", add)
print ("(a^2 + b)* c = \n", result) # result using matrix multipication
print (result2) # rsult by using normal multipication





