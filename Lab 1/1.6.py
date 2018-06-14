import numpy as np
ar = np.random.randint (0,20,15) # creting a vector of size 15, with random int elements
print (ar)
li = list (ar) # converting the array into list
max_count = 0 # intializing variables to get the most frequent element
index = 0

for i in range (0,len(li)):
    if li.count(li[i])> max_count: # checks the frequency of each element with the max_count
        max_count = li.count(li[i])
        index = i


print ("The most frequent item in the list is: {} and it's frequency is: {}".format (li[index],max_count))




