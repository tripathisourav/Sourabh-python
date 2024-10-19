# Lists in Python

# A built-in data type that stores a set of values
# it can store elements of diffrent types(integers,float,string,etc)

# marks1 = 94.4
# marks2 = 87.5
# marks3 = 97.2
# marks4 = 68.4
# marks5 = 45.1

# marks = [94.4, 87.5, 97.2, 68.4, 45.1]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])

# student = ["Sourav", 95.4, 17, "Delhi"] 

#lists are mutable in python. we can change value at aparticular index
# strings are immutable in python

# str = "hello"
# str[2] = "o"
# error occurs

# student[0] = "Arjun"
# print(student)

# print(student[5])
# error index ke andar hi access kar sakte hai

# List Slicing
# similar to string Slicing

# print(student[1:3])

# print(student[:3])
#similar to [0:3]

# print(student[1:])
# similar to [1:len(student)]

# print(student[-3:-1])

# List Methods

# list = [2,1,3]

# print(list.append(4))
#returns none but append value in list

# list.append(4)

# print(list.sort())
#returns none but sorts the list

# list.sort()
#sorts in ascending order
# print(list)

# list.sort(reverse=True)
# print(list)
# sorts list in reverse order

# fruits["lichi","apple","banana"]
# fruits.sort()
# print(fruits)
# sorting happens on the basis of character coming first

# list.reverse()
# print(list)
# reverses the complete list

# list.insert(2,6)
# print(list)

# list.remove(6)
# print(list)
# removes first occurence of the element

# list.pop(3)
# print(list)

#Tuples in Python
# A built in data type that lets us create immutable sequences of values

# tup = (2,1,3,1)
# print(type(tup))

# print(tup[0])
# print(tup[1])

# tup[1] = 4
#not possible because tuples are immutable

# tupl = ()
#empty tuple
# print(tupl)
# print(type(tupl))

# tupl = (1,)
#single value tuple

# tupl = (1)
#python thinks that it is an integer
# print(type(tupl))

# tupl = (1,2,3,4,)
#writting , after last value in tuple is just optional

# Tuple Methods

# tup = (2,1,3,1)

# print(tup.index(1))
# returns index of first occurence

# print(tup.count(1))
# counts total occurences

# WAP to ask the user to enter names of their three favourite movies and store them in a list

# movies = []

# movie1 = input("enter first movie ")
# movie2 = input("enter second movie ")
# movie3 = input("enter third movie ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)


#WAP ro check if a list contains a palindrome of elements

# list = [1,2,3]
# list.copy()
#returns the shallow copy of the list

# list1 = [1,2,1]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# WAP to count the number of students with the "A" grade in the following tuple.

# grade = ("C","D","A","A","B","B","A")
# print(grade.count("A"))

# store the above values from the list& srt them from "A" to "D"

# grade = ("C","D","A","A","B","B","A")
# grade.sort()
# print(grade)

# Dictionaries in python

# Dictionaries are used to store data values in key.value pairs
# They are unordered ,mutable(changeable) & do not allow duplicate keys

# "key" : value

# dict = {
#     "name" : "sourav",
#     "cgpa" : 6.5,
#     "marks" : [95,87,91],
#     "subjects" : ("dac","python","dbms"),
# }

# lists and dictionaries can't be keys because they are mutable 

# print(dict("name"))
# print(dict("cgpa"))
# print(dict("marks"))

# print(dict("surname"))
# if the key doesn't exist it gives error

# dict["name"] = "sourabh" #overwrite 
# dict["surname"] = "Tripathi"

# null_dict = {}
# null_dict["name"] = "sourav"
# print(null_dict)

student = {
   "name" : "rahul kumar",
   "cgpa" : 7.5,
   "subjects" : {
      "phy" : 97,
      "chem" : 98, 
      "math" : 95,
   }
}

#nested dictionary

# print(student)
# print(student["subjects"])

# print(student["subjects"]["chem"])

# Dictionary Methods

print(student.keys())

print(list(student.keys()))
# typecasting student.keys() into list

print(len(student))

print(student.values())
# returns the values of all the keys

print(student.items())
#  returns the pairs of keys,values

pairs = list(student.items())
print(pairs[0])




