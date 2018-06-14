my_list = [1, 3, 6, 2, -1, 2, 8, -2, 9] # Given list to find triplets which sum to zero
result = set() # to avoid duplicate sets were used to store the triplets
for i in my_list:
    for j in my_list:
        for k in my_list:
            if (i + j + k == 0) and i != j and i != k and j != k:
                result.add(i)
                result.add(j)
                result.add(k)
print(result)
