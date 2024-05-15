print("hello world this is my first python code")
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
print("-----------")
print("|          |")
print("|          |")
print("|          |")
print("|          |")
print("------------")
#variable names can be separated by undersores(_)
char_name = "Favour"
char_stdyperiod = "4"
#concatenation
print("my name is "+char_name+" of bsc cs class of rntu")
print("i am in my first year")
print("I came from Ghana to India to study for "+char_stdyperiod+" years\n")
#\n is for a line to be created
print("Welcome Everyone\n")
#to show the length(number of characters) of a string NB: spaces are also regarded as characters
phrase="i love her so much"
print(len(phrase))
#to print characters by index(0,1,2,3,....)(0 index is always for the first character)
phrasee="maturity"
print(phrasee[7])
#to print the index of a character
print(phrasee.index("r"))
#to replace a string
print(phrasee.replace("maturity","responsibility"))

                                   #WORKING WITH NUMBERS
#numbers placed in parenthesis are executed first
my_num=10
print(my_num)
print(str(my_num)+" reasons why I want to code")
my=-10
print(abs(my))
print(10%3)

                           # to get input from users
name=input("please enter your name:")
age=input("Please enter your age:")
print("hello "+name + " you are "+age+" years old")

num1=input("please enter the first number:")
num2=input("please enter the second number:")
sum=float(num1)+float(num2)
print(sum)

#mad libs game
name = input("Enter a name: ")
color = input("Enter any color: ")
footwear = input("Enter a type of footwear: ")
ethic = input("Enter an ethic: ")

print(name +" is a big boy")
print(color+" is a bright color")
print(footwear+" are nice ")
print(ethic+" is key")

friends=["Thomas","Gilbert","Matt"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[-3])
#list functions
list_1=[2,3,4,5]
list_2=["Abby","CHristian","Juliet"]
list_2.extend(list_1)
print(list_2)
#NB: lists are enclosed in square brackets[] but tuples are enclosed in normal brackets()
#tuples(immutable)
list_1=(2,3,4,5)
print(list_1[2])

#functions
def hey_there():
    print("I am interest in you")
hey_there()
#passing parameters to a function
def hey_there(motive):
    print("I am " +motive+" in you")
hey_there("interest2")
hey_there("loverwww")
#return statements5
def sum(x,y):
    return x+y
z=sum(5,6)
print(z)

def prdt(x,y):
    s=x*y
    return s
s=prdt(4,5)
print(s)

def prdt_div(x,y):
    s=x*y
    j=x/y
    v=x+y
    return s,j,v
s,j,v=prdt_div(4,5)
print(s,j,v)

# IF statements
good_mark=False
bad_mark=False
if good_mark and bad_mark :
    print("Great job!! keep it up")
elif not(good_mark) and not(bad_mark):
    print("more room for improvement")
else:
    print("You can do better")

alive= input("enter bool:")

if alive == "true":
    print("it is good to be alive")
else:
    print("death is a sad thing")

#program to find largest among two numbers
num1=input("Enter the first num:\n")
num2= input("enter the second number:\n")
num3= input("Enter the third number:\n")
print(num1,num2,num3)
if num1 >= num2 and  num1 >= num3:
    print("num1 is the largest")
elif num2 >= num1 and num2 >= num3:
    print("num2 is the largest")
else:
    print("num3 is the largest")



