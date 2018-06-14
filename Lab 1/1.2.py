def func(x):
    my_list = x.split() # convert the input string into a list and stores it in variable my_list
    y = len(my_list)

    """
    If the length of the input string is even there will be two middle values
    If the length of the input string is odd there will be only one middle value
    """

    if y % 2 == 0: # for the even case
        print("The middle words are:  {} {}".format(my_list[y // 2 - 1], my_list[y // 2]))

    elif y % 2 != 0: # for the odd case
        print("The middle workd is: {}".format(my_list[y // 2]))

    max = 0 # variables to find the longest element
    index = 0

    for i in range(0, y):
        if len(my_list[i]) > max:
            max = len(my_list[i])
            index = i

    print("The longest word is: {}".format(my_list[index]))

    reverse = []
    for i in my_list:
        x = i[len(i)::-1]
        reverse.append(x)

    print("Sentence with reverse order is : {}".format(reverse))


x = input("please enter a sentence: ")
func(x)
