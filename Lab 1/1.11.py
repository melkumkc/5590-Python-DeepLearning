# Initialize the password, valid boolean, numbers, and special characters
password = ""
valid = False
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['$', '@', '!', '*']

# Continue to loop until a valid password is given
while valid is False:

    # Set the correct length, number, special character, lower, and upper booleans
    contain_length = False
    contain_number = False
    contain_special = False
    contain_lower = False
    contain_upper = False

    password = input("\nEnter a password: ")

    # Check if the password is the correct length
    if (len(password) < 6) or (len(password) > 16):
        print("The password length should be in range 6-16 characters")
    else:
        contain_length = True

    # Check if the password has at least one number
    for i in range(0, len(password)):
        if password[i] in number:
            contain_number = True
    if contain_number is False:
        print("The password must have at least one number")

    # Check if the password has at least one special character
    for i in range(0, len(password)):
        if password[i] in special:
            contain_special = True
    if contain_special is False:
        print("The password must have at least one special character($,@,!,*)")

    # Check if the password has at least one lowercase character
    for i in range(0, len(password)):
        if password[i].islower() is True:
            contain_lower = True
    if contain_lower is False:
        print("The password must have at least one lowercase character")

    # Check if the password has at least one uppercase character
    for i in range(0, len(password)):
        if password[i].isupper() is True:
            contain_upper = True
    if contain_upper is False:
        print("The password must have at least one uppercase character")

    if contain_number is True and contain_special is True and \
            contain_upper is True and contain_lower is True and contain_length is True:
        valid = True

# Print the valid password
print(password, "is a valid password")
