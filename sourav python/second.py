#input in python
#input() statement is used to accept values(using keyboard) from user

# .string input
# name = input("name : ")
# print(name)                                       

# .int input
# age = int(input("age : "))
# print(age)

# .float input
# price = float(input("price : "))
# print(price)

# a**b a ki power b ke barabar hota hai
# A,B=2,3
# C=A**B
# print(C)

# C= not True and False or True
# print(C)

# CONDITIONAL STATEMENTS
# if-elif-else(SYNTAX)

#INDENTATION 4 space gap after condition statement
# if(condition):
#     stament1
# elif(condition):
#     statement2
# else:
#     statementN

#traffic lights code

# Light = input("Light : ")
# if(Light == "red"):
#     print("stop")
# elif(Light == "yellow"):
#     print("look")
# elif(Light == "green"):
#     print("go")
# else:
#     print("light is broken")

# print output for :
# A = 5 & G=M 
# ans: fee is 300
# A = 2 & G=F 
# ans: fee is 200

# A = int(input("A : "))
# G = input("M/F : ")
# if((A == 1 or A==2) and G == "M"):
#     print("fee is 100") 
# elif((A == 3 or A==4) or G == "F"):
#     print("fee is 200")   
# elif(A == 5 and G == "M"):
#     print("fee is 300")   
# else:
#     print("no fee")

# conditional statements
# single line if / ternary operator

# <var> = <val1> if <condition> else <val2>

# food = input("food: ")
# eat = "yes" if food == "cake" else "no"
# print(eat)

# <stt1> if <condition> else <stt2>

# food = input("food: ")
# print("sweet: ") if food == "cake" or food == "jalebi" else print("not sweet")

# clever if / ternary operator

# <var> = (false_val,true_val) [<condition>]
# agar condition shi hui toh right side wali true value chalegi or agar condition false hogi toh left side wali false value chalegi

# age = int(input("age : "))
# vote = ("yes", "no") [age<18]

# sal = float(input("salary : "))
# tax = sal*(0.1,0.2) [sal>50000]
# print(tax)

# best practices

# simple instructions
# one instruction per task
# short & meaningful variable names
# use appropriate comments
# avoid complex expressions

# simple instruction
# name = input("name :")
# print name 

# complex instruction
# print(input("name : "))





