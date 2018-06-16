class Person(): # base class for Student, GeneralStaff and Librarian class

    count = 0 # To count the number of people who are in the system

    def __init__(self, name, family, date_birth,id):  # constructor

        self.name = name
        self.family = family
        self.date_birth = date_birth
        self.id = id
        Person.count += 1 # increments the total people in the system whenever a new person is created

    def age (self): # To calculate age
        return (2018 - int (self.date_birth))


class Student (Person):

    def __init__(self, name,family,date_birth, id, major, year): # constructor for student class
        Person.__init__(self,name,family,date_birth,id)
        self.major = major
        self.year = year

    def is_student (self):
        return True

class GeneralStaf (Person):

    def __init__(self, name,family,date_birth, id, department): # constructor for GeneralStaf
        Person.__init__(self,name,family,date_birth,id)
        self.department = department

    def is_student (self):
        return False



class Books():

    book_count = 0 # to count the number of books the library has
    __in_library = True # private variable to check whether the book is in library store or issued
    issued_to = " "
    recived_by = " "

    def __init__(self, title, date_purchased, serial_no):  # constructor

        self.title = title
        self.date_purchased = date_purchased
        self.serial_no = serial_no
        Books.book_count += 1

    def issued_to (self,id,date): # To track to whom & when the book is issued to
        self.issued_to = id
        self.issued()
        self.date = date

    def returned_by (self, id,date): # To track by whom and when the book is returned
        Person.id = id
        self.returned()
        self.date = date

    def issued(self): # To update the book status when issued
        self.__in_library = False

    def returned (self): # To update the book status when returned
        self.__in_library = True

    def stored_by(self, id): # To keep track of which librarian stored the book
        self.received_by = id


    def status (self): # To show the activities of the book i.e issued to, returned by, stored by

        print ("The name of the book is : {}".format (self.title))
        if self.__in_library == True:
            print ("  In library")
            print ("  Was last issued to: {}".format (self.issued_to))
            print("  Was stored by Librarian {}".format(self.received_by))
        elif self.__in_library == False:
            print ("  Not in Library")
            print ("  Is issued to: {} on {}".format (self.issued_to,self.date))


class Librarian (Person, Books):

    def __init__(self, name,family,date_birth, id,shift):
        Person.__init__(self,name,family,date_birth,id)
        self.shift = shift
    def is_student (self):
        return False




melkam = Student ("melkam", "get", 2000, "s1", "computer science", "senior") # creatint student objects
abe = Student ("abe", "mark",1998,"S2","Computer science", "Graduate")

""" To show attribute of the student object"""
print ("The people in the system so far are: {} ". format (Person.count))
print ("Name of student: {} {}; age: {}; id : {}; major {}, status {}".format (abe.name,abe.family,abe.age(),abe.id,abe.major,abe.year))
print("Is {} a student =  {}" .format (melkam.name,melkam.is_student()))# checking if a person is student or not

get = GeneralStaf("get","kkkk",1999,"G2", "General service") # creating general staff object
print ("The people in the system so far are: {} ". format (Person.count))
print("Is {} a student =  {}" .format (get.name,get.is_student()))# checking if a person is student or not

bob = Librarian ("bob","jack",1998,"LL1",1) # creating a librarian object
print("Is {} a student =  {}" .format (bob.name,bob.is_student()))# checking if a person is student or not
print ("{} is a librarian who works in the {} shift".format (bob.name, bob.shift))

pyt = Books("Python", 2000, "b12") # creating a book object
dep_learn = Books ("Deep Learning", 2010,"b100")
print ("The total number of books the library has is: {} ".format (Books.book_count))

pyt.issued_to("s1","Nov,2017") # issuing python book to stundent
dep_learn.issued_to ("s2", "Jan,2018")
pyt.returned_by("s1","Jan 2018")
pyt.stored_by("LL1")
"""Checking status of a book"""

print ("\n The status of books:\n ")
pyt.status()
print ("\n")
dep_learn.status()






