web_class = {"mike", "andru", "kate"} # list of students taking web class, stored in sets
pyt_class = {"jhon", "andru", "jesse"} # list of students taking python class, stored in sets
both_class = web_class & pyt_class # the intersection of the above two sets will give a list of students taking both classes
one_class = (web_class - both_class) | (pyt_class-both_class)
""" 
web_class - both_class ......will give students taking only web class
pyt_class - both_class ...... will give students taking only python class
The union of the above two will give list of students taking only one class
"""
print ("List of students taking both classes: {}".format (both_class))
print ("List of students taking only one class: {}".format (one_class))
