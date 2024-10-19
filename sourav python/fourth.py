# STRINGS

# String is a datatype that stores sequence of characters

# str1 = "This is a string."
# str2 = 'ApnaCollege'
# str3 = """this is a string"""

#error occurs
# str = "this is a string
# and we are creating it in python" 

# str = "this is a string and we are creating it in python" 
# print(str)

# #\n gives us next line
# str = "this is a string and \n we are creating it in python" 
# print(str)

# #\t gives tab space
# str = "this is a string and \t we are creating it in python" 
# print(str)

# Basic Operations

# -> Concatenation
#    "hello" + "world" --> "helloworld"

# -> length of str
#    len(str)

# str1 = "Sourav"
# str2 = "Tripathi"
# final_str = str1 + " " + str2
# print(final_str)

# print(len(str1))
# print(len(str2))

#INDEXING

# str="Apna_College"

# A p n a _ C o l l e g e
# 0 1 2 3 4 5 6 7 8 9 10 11

# str[0] = A
# str[11] = e

# print(str[4])
# str[4] = "@" #assignment is not possible at a particular index elements at the index can be accessed but not updated
# print(str[4])

#SLICING
# Accessing parts of a string

# str[starting_idx : ending_idx] 
#ending idx is not included

# str = "Apna College"
# print(str[1:4])
# print(str[5:len(str)])
# print(str[:5]) #it is same as print(str[0:5])
# print(str[1:]) #it is same as print(str[1:len(str)])

# negative index

#  A p p l e
# -5 -4 -3 -2 -1

# str = "Apple"
# print(str[-3:-1]) 
# #output "pl"
# print(str[-5:-1]) 
# #output "Appl"

#ending idx is not included

# String Functions

# str = "i am a coder."

# a = str.endswith("er.")
# #returns true if the string ends with the substr
# print(a)

# b = str.capitalize()
# #capitalizes the first character
# print(b)
# #no changes will occur in the orignal string for doing that
# str = str.capitalize()


# # str.replace(old,new)
# #replaces all occurences of old with new

# print(str.replace("a","b"))
# print(str.replace("coder","developer"))

# #str.find(word)
# #returns 1st index on the 1st occurence

# print(str.find("o"))
# print(str.find("am"))
# print(str.find("q")) # returns -1 invalid index

#str.count("ab")
#counts the occurence of substr

# print(str.count("a"))
# print(str.count("o"))

# Q1 WAP TO INPUT USER first name & print its length

# name = input("enter your name: ")
# print("length of string is: ", len(name))

# Q2 WAP to find the occurence of $ in a string

# str = "i am the $ symbol $99 "
# print(str.count("$"))

# CONDITIONAL STATEMENTS

# if-elif-else(SYNTAX)

# if(condition):
#     statement1
# elif(condition):
#     statement2
# else:
#     statementN

# age = 21

# if(age >= 18):
#     print("can vote and apply for licence")


# light = "green"

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")

# print("end of code")

#we can write multiple elif and if statements in the above code but for elif statements the above statement must be if

# num = 5

# if(num>2):
#     print("num is greater then 2")
# if(num>3):
#     print("num is greater then 3")

#both statements will be printed

# if(num>2):
#     print("num is greater then 2")
# elif(num>3):
#     print("num is greater then 3")

# light = "green"

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")
# else:
#     print("light is broken")

# print("end of code")

# in python proper indentation is necessary i.e proper spacing 
# age = 24
# if(age>=18):
#     print("can vote")
# else:
#     print("can't vote")

# marks = int(input("enter marks of the student : "))

# if(marks>=90):
#     grade = "A"
# if(marks>=80 and marks <90):
#     grade = "B"
# if(marks>=70 and marks <80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of he student is -> ", grade)

# iss code mein if-if or sirf else diya hai jis karan pura code chal rha hai or last mein aate aate grade "D" ho ja rha hai

# marks = int(input("enter marks of the student : "))

# if(marks>=90):
#     grade = "A"
# elif(marks>=80 and marks <90):
#     grade = "B"
# elif(marks>=70 and marks <80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of he student is -> ", grade)

# nesting 

    # age = 34

    # if(age >=)18:
    #     if(age >= 80):
    #         print("can't drive")
    #     else:
    #         print("can drive")

    # else:
    #     print("can't drive")

# Q1 WAP to check if a number entered by the user is odd or even

# num = int(input("enter the number "))

# rem = num % 2

# if(rem == 0):
#     print("even number ")
# else:
#     print("odd number ")

# Q2 WAP to find the greatest of three numbers entered by the user

# num1 = int(input("enter the first number "))
# num2 = int(input("enter the second number "))
# num3 = int(input("enter the third number "))

# if(num1 > num2):
#     if(num1 > num3):
#         print("num1 is the greatest")
#     elif(num3 > num1):
#         print("num3 is the greatest")

# elif(num2 > num3):
#     print("num2 is the grestest")

# else:
    # print("num3 is greatest")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("num1 is the greatest")
# elif num2 >= num1 and num2 >= num3:
#     print("num2 is the greatest")
# else:
#     print("num3 is the greatest")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if(num1 >= num2 and num1 >= num3):
#     print("num1 is greatest")
# elif(num2 >= num3):
#     print("num2 is grestest")
# else:
#     print("num3 is greatest")


# Q3 WAP to check if a number is multiple of 7 or not

# num = int(input("enter the number: "))

# rem = num % 7

# if(rem == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")

# Homework Qyestion
# WAP to find the greatest of 4 numbers


