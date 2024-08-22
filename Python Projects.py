# Program to print "hello world!" to console
print("hello world!")

#  User provides two numbers and selects an operation (addition, subtraction, multiplication, division).

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

sign = input("please choose the preferred operation[+,-,* or /]:")

if sign == "+":
    print("the sum is:", num1+num2)
elif sign == "-":
    print("the difference is:", num1-num2)
elif sign == "*":
    print("the product is:", num1*num2)
elif sign == "/":
    print("the quotient is:", num1/num2)
else:
    print("incorrect input")

# Develop a Body Mass Index calculator based on user input.

print("Hey do you wish to know your Body mass index(BMI) and the category to which you belong?")
print("Enter your details please")
print("")
weight = float(input("Please enter your weight(in Kilograms):"))
height = float(input("Please enter your height(in metres):"))

BMI = weight / height**2

print("Your Body Mass Index is: ", BMI)
print("")
if BMI < 18.5:
    print("Unfortunately, you're Underweight.")
#elif BMI > 18.5 and BMI <= 24.9:
elif 18.5 < BMI <= 24.9:
    print("Great!!, you're normal.")
#elif BMI > 24.9 and BMI <= 29.9:
elif 24.9 < BMI <= 29.9:
    print("Oh no!!, you're actually overweight.")
else:
    print("Oops!!, you're obese.")
print("my name is enock")
