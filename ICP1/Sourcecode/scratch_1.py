import random
x = random.randint(0,10)
guess = input (" Please enter a number 0-9: ")

while x != int (guess):

    if  int (guess) < x:
         print ("your answer is lower than required")
         guess = input(" Please enter a number 0-9: ")
    else :
         print ("your answer is greater than required")
         guess = input(" Please enter a number 0-9: ")
print ("your answer is perfect congratulations !!!")