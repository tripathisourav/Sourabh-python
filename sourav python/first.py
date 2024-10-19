print("Namaste Duniya")
print('my name is sourav','''my age is 23''')
print(23)
print(2+5)

name="sourav"
age=20
price=24.99

print("my name is :", name)
print("my age is :", age)

age2 = age
print(age2)

print(type(name))
print(type(age))
print(type(price))

age = 23
old = False
a = None
print(type(age))
print(type(old))
print(type(a))

# python is a case senstive language ex false and False are two difftrnt things

a = 2
b = 3
sum = a + b 
diff = a - b
print(sum)
print(diff)

# python is a implicit typed language there is no need to define the datatype of variable

A,B = 2,3
Txt = "@"
# idhar @ ek string hai jitna iss string ke aange number hoga utni baar ye print ho jayega
print(A*Txt*B)

A,B = "2",3
Txt="@"
# 2 and @ idhar par string hai
print((A+Txt)*B)

A,B = 2,3
C=4
print(A+B*C)

# result float
A,B=10,5.0
C=A*B
print(C)

A,B=1,2
C=A/B
print(C)
# result of division operator with two integers will be float

A,B=1.5,3
C=A//B
# (//) integer division with float and int will give int displayed as float
print(C, A/B)

# floor gives closest integer, which is lesser than or equal to the float value result of (A//B) is same as floor(A/B)
A,B=12,5
C=A//B
# D=A/B
# floor(D)
print(C)

A,B=-12,5
C=A//B
print(C)

# remainder is negative when denominator is negative in modulo(%)

A,B=-5,2
C=A%B
print(C)

A,B=5,-2
C=A%B
print(C)

#single line comment
""" This is 
    a multi-line 
    comment """