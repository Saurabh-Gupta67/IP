# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:21:36 2026

@author: Student
"""
"""
a=int(input('enter integer'))
print('the value of a =',a,'type(a)')

b=float(input('enter float'))
print('the value of b=',b,'type(b)')

c=(input('enter string'))
print('the value of c=',c,'type(c)')

d=True
print('the value of d=',d,'type(d)')
"""
"""
age=input("Enter Age: ")
marks = input("Enter Marks: ")
print("Without Conversion: ")
print(age + marks)
age=int(age)
marks = float(marks)
print("Age after 5 years:", age + 5)
print("Marks + 2;", marks + 2) 
"""
"""
a=10
b=5.5
print(a + b) # implicit conversion
# print(a + "5") # TypeError
c = "5"
print(a + int(c)) # Explicit conversion
"""
"""
a = 100
b = 100
print(id(a))
print(id(b))
b = 200
print(id(a))
print(id(b))
"""

"""
a = input('Enter num1')
b = input('Enter num2')

print('Before swap a=', a, 'b=',b);

temp=a
a=b
b=temp
print('After swap a=',a, 'b=',b);
"""

"""
#tuple unpacking
a = 10
b = 20
a, b=b, a
print(a,b)
"""
"""
first = input("Enter first value:")
second = input("Enter second value:")
try:
    num1 = float(first)
    num2 = float(second)
    print("Addition=", num1=num2)
except valueError:
    if first.isalpha() and second.isalpha():
        print ("Concatenation=", fisrt+second)
    else:
        print("Concatention=", first+second
"""
      
"""
age=input("Enter Age")
marks=-input("Enter Age")
print("Without Conversion")
print(age+marks)
age=int(age)
marks float(marks)
print("Age after 5 years:", age+5) 
print "Marks+2, marks+2)
"""