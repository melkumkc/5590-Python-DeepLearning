import numpy as np
import matplotlib.pyplot as plt


arr1 = np.array([[0,1],[1,3],[2,2],[3,5],[4,7],[5,8],[6,8],[7,9],[8,10],[9,12]]) #inputing data as an array

print (arr1) # to check if the data input is correct
x_sum = 0 # To find the mean of the first column
for i in  arr1 [:,0]:
    x_sum += i
x_mean = x_sum / len(arr1) # mean of the first column
y_sum = 0 # TO find the mean of the second column
for i in arr1 [:,1]:
    y_sum += i
y_mean = y_sum/len(arr1) # To find the mean of the second column


lis2 = []
lis3 = []


for i in range (len(arr1)):

    lis2.append( arr1[i][0]- x_mean) # To find (xi - X)
    lis3.append( arr1[i][1]- y_mean) # TO find  (yi -y)

arr2 = np.array (lis2)
arr3 = np.array(lis3)
arr4 = arr2 * arr3 # to find  (xi -x) (yi -y)
arr5 = arr2 * arr2 # to find  (xi-x)**2

Numerator = 0
Dumnetor = 0
for i in range (0, 10):
    Numerator += arr4[i] # to find summation
    Dumnetor += arr5[i] # to find summation
B1 = Numerator/Dumnetor
B0 = y_mean - B1*x_mean
print ("The value of the means are x_mean : {} and y_mean : {}".format (x_mean,y_mean))
print ( "The vale of B0 is : {} and the value of B1 is : {}".format (B0,B1))

x = np.linspace (0,15,1000)
y = B0 + B1 *x
plt.scatter(arr1[:,0], arr1[:,1])
plt.plot (x,y)
plt.show ()

