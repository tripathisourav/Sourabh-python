# TYPES OF OPERATORS
# An operator is a symbol that performs a certain operation b/w operands.

# -> Arthmetic Operators (+,-,*,/,%,**)

# a = 5
# b = 2

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)   #always a floating value
# print(a%b)   #remainder
# print(a**b)  #a^b


# -> Relational / Comparision Operators (==,!=,>,<,>=,<=)

# a = 50
# b = 20

# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)
# print(a > b)
# print(a < b)


# -> Assignment Operators (=,+=,-=,*=,/=,%=,**=)

# num = 10
# num = num + 10
# print("num : ", num)

# num += 10
# print("num : ", num)
# num -= 10
# print("num : ", num)
# num *= 10
# print("num : ", num)
# num /= 10
# print("num : ", num)
# num %= 10
# print("num : ", num)
# num **= 10
# print("num : ", num)


# -> Logical Operators (not,and,or)

# print(not True)
# print(not False)
#true false mein T or F hamesha capital honge

# a = 50
# b = 20
# print(not (a>b))

# val1 = True 
# val2 = True
# print("and operator", val1 and val2)
# print("or operator", val1 or val2)

# val1 = True 
# val2 = False
# print("and operator", val1 and val2)
# print("or operator", val1 or val2)

# val1 = False 
# val2 = False
# print("and operator", val1 and val2)
# print("or operator", val1 or val2)


# TYPE CONVERSION (conversion -> automatically and casting -> manually)

# a,b = 2, 4.25
# sum = a + b # 2.0 + 4.25 = 6.25
# print(sum) 

# a,b = "2", 4.25
# print(a + b)

# Typecasting 

# a,b = int("2"), 4.25
# print(type(a))
# print(a + b) #no error

# a,b = float("sourav"), 4.25 #error occurs 

# a = 3.14
# a = str(a)

# print(type(a))

# name = input("enter your name: ")
# print("welcome ",name)

# # the type value of any thing that we enter as a input is string
# a = input("enter a: ")
# print(type(a))

# # for getting the values in the type we want we need to typecast the input
# a = int(input("enter a: "))
# print(type(a))

# name = input("enter name: ")
# age = input("enter age: ")
# marks = float(input("enter marks: "))

# print("welcome", name)
# print("age=", age)
# print("marks=", marks)


#PRACTICE PROBLEMS

# Write a program to enter two numbers & print their sum.

# a = int(input("enter a: "))
# b = int(input("enter b: "))

# WAP to input side of a squar & print its area

# side = int(input("enter side of square: "))
# area = side * side
# print("area of square is ", area)

# WAP to input two floating point numbers & print their average

# a = float(input("enter first: "))
# b = float(input("enter second: "))

# print("average = ", (a+b)/2 ) 

# WAP to input two ineger numbers, a and b. Print True if a is greater than or equal to b.if not print false.

# a = int(input("enter a: "))
# b = int(input("enter b: "))

# if(a>=b):
#     print(True)
# else:
#     print(False)




