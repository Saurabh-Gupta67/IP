# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:51:16 2026

@author: Student
"""

a=int(input("Enter a number"))

if(a>0):
    print('the number is positive')
else:
    print('the number is negative')


#3
a=int (input('Enter a number'))
 
if(a>0):
    print('the number is positive')
 
a=int(input("Enter a number"))
 
if(a%2==0):
     print('the number is even')
 
else: 
     print('the number is odd')
     
marks=int(input('Enter your marks'))

if(marks>=90):
    print('A')
elif(marks>=75):
    print('B')
elif(marks>=50):
    print('C')
else:
    print('Fail')
#4

age=int(input("Enter your age"))
n=input("Enter your Nationality")
if(age>=18):
    if(n=="Indian"):
        print("eligible to vote")
    else:
        print("Your are not Indian")
else:
    print("Not eligible to vote")

#6
year=int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,"is a Leap Year.")
else:
    print(year,"is not a Leap Year.")
#7
a=int(input('Enter a='))
b=int(input('Enter b='))
op=input('Enter operator')

if(op=='+'):
    c=a+b
    print('addition is=',c)
elif(op=='-'):
    c=a-b
    print('sub is=',c)
elif(op=='*'):
    print('mul is=',c)
elif(op=='/'):
    print('div is=',c)
elif(op=='%'):
    c=a%b
    print('mod is=',c)
else:
    print('Invalid operator')
#8
purchase_amount=int(input("Enter a Amount="))
if(purchase_amount<=2000):
    discount=2000*0.20
    amount=purchase_amount-discount
    print('Amout after discount',amount)
elif(purchase_amount>=1000):
     discount=1000*0.10
     amount=purchase_amount-discount
     print('Amount after discount',amount)
else:
    print('no discount')
#10
print("-----MENU-----")
print("1. check Even/odd")
print("2. Find Largest of  Three Number")
print("3. Grade System")

choice = int(input("Enter your choice (1-3)"))

if(choice == 1):
    a=int(input("Enter a number"))
     
    if(a%2==0):
         print('the number is even')
     
    else: 
         print('the number is odd')

elif(choice == 2):
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter third number:"))
    if(a>=b and a>=c):
        print("Largest =",a)
    elif(b>=a and b>=c):
        print("Largest =",a)
        
elif(choice == 3):
   marks=int(input('Enter your marks'))

if(marks>=90):
    print('A')
elif(marks>=75):
    print('B')
elif(marks>=50):
    print('C')
else:
    print('Fail')
    
     
    

