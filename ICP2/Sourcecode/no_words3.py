

filename = open ("input2.txt", "r")

lines = " "
while lines != "":
    lines = filename.readline().strip()
    if lines == "":
        continue
    my_list = lines.split (" ")
    print (lines, " ", len (my_list))