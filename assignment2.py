# python program to make a simple calculater

#1. add
#2. sub
#3. mult
#4. div

operation=("1 add, 2 sub, 3 mult, 4 div:")
o=operation
print("select operation to perform:")
print("1 add")
print("2 sub")
print("3 mult")
print("4 div")


operation == input()

if operation == "1":
    num1 = input("enter first number:")
    num2 = input("enter second number:")
    print("The sum is" + str(int(num1) + int(num2)))
elif operation == "2":
     num1 = input("enter first number:")
     num2 = input("enter second number:")
     print("The sub is"- str(int(num1)-int(num2)))
elif operation == "3":
     num1 = input("enter first number:")
     num2 = input("enter second number:")
     print("The mult is" * str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("enter first number:")
    num2 = input("enter second number:")
    print("The div is" / str(int(num1) / int(num2)))

else:
    print("invalid Entry")





#Python program to check for a leap year.

#A leap year only if it perfectly didided by 4. Examle
#2017 is not a leap year
#1900 is not a leap year
#2012 is a leap year
#2000 is a leap year

year = int(input("enter the year:"))
if (year%4)==0:
    print("It is a leap year")

else:
    print("It is nor a leap year")















# Python program to find the area triangle
base= float(input("Enter the base"))
height= float(input("Enter height"))
area=1/2*base*height

print(area)














#Python program to check whether a a number is prime or not

num = 407

# To take input from the user
# num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")

