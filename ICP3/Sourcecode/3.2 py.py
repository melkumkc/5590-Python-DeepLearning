x = input ("Please enter a sentence: ")

my_set2 = {"a", "e", "i", "o", "u"}
count = 0
for i in x:
    if i in my_set2:
        count = count + 1



print("Count of vowels is: {} ".format (count))
