li = ["PHP", "exercises", "backend"]
count = []
l_final = []
x = len (li)

for i in range (0,x):
    count.append (len(li[i]))

for i in range (0,x):
    l_final.append((count[i],li[i]))

l_final.sort()
print (l_final[x-1])