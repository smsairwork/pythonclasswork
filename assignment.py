# A program that checks whether an alphabet is a vowel or a constant
# ch = input("Enter the Alphabet : ")
# if ch in['A' 'E' 'I' 'O' 'U' 'a' 'e' 'i' 'o' 'u']:
#   print(ch, "is a vowel")

# else:
#   print(ch, "is a consonant")

ch = 'z'
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Letter is a vowel")

else:
    print("Letter is a consonant")

# A program that returns the sum of two integers

num1 = int(input("Enter number 1 : "))
num2: int = int(input("Enter number 2  :"))
result = num1 + num2

print(num1 + num2)


#Type casting - coverts a data type into another data type
number=8
print(float(number))

num=89.7
num=10
print(int(num))
print(type(num))




























number = 12  # Replace this with the number you want to check

if number % 4 == 0:
    print(number, "is a multiple of four")
else:
    print(number, "is not a multiple of four")
