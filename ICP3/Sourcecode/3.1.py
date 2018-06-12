x = input ("Please enter a sentecne: ")
di = {}

li = x.split()



for i in range (0, len(li)):
    if li[i] in di:
        z = di[li[i]]
        y = z +1
        di[li[i]] = y
    else:
        di[li[i]] = 1


hh = list (di.items())
hh.sort()
from collections import OrderedDict
o_dic = OrderedDict (hh)
print (o_dic)
