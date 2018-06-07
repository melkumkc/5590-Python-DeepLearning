fr = open ("input1.txt", "r")
text = fr.read()

li = list(text.splitlines())

for i in range (0, len(li)):
    print (li[i],",",len(li[i]))

wr = open ("output.txt", "w")
for i in range (0, len(li)):
    wr.write (li[i])
    wr.write (", ")
    wr.write (str(len(li[i])))
    wr.write ("\n")