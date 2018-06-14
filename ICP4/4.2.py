import numpy as np
arr = np.random.randint (0,100,(10,10)) # creating an array of random int values
print (arr)
for i in range (0,10):
    print ("Row {} max value is {}".format (i,arr[i,:].max())) # finding max value for each row
    print("Row {} min value is {}".format(i, arr[i].min()))  # finding min value for each row
