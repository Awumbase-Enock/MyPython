"""print("**i am learning**")
print("__you have to learn__")
print("*you have to learn*")
print("_you have to le")"""

'''name = "Alice"
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")

print("Hello", "world" , end="!", sep=", ")
print(" henry","Osafo","marfo",end=" >>>",sep="-")

females = ("Nozi", "Esther", "pauline", "Favour", "Shammaine")
male = "Esther"
if male in females:
    print("{} is a female" .format(male))
else:
    print("{} is not a female".format(male))

my_day = "Friday"
if my_day == "Friday":
    yes = "you are right"
    print("correct, {} is the day she was born, {}".format(my_day, yes))
    #print("Annette was born on {}".format(my_day))
elif my_day == "Monday":
    print("That's mums day")
elif my_day == "Tuesday":
    print("I was Born on this day")
elif my_day == "Wednesday":
    print("this day is for Alfred")
elif my_day == "Thursday":
    print("ahh, this day is obviously for Kyei")
elif my_day == "Saturday":
    print("this is dad's")
elif my_day == "Sunday":
    pass
    #\'if\' statements cannot be empty, there must be at least one statement in every
    # \'if\' and \'elif\' block. You can use the pass statement to do nothing and avoid
    # getting an error.
    #print("A blessed day on which I gotta go to Church")
else:
    print("you know what?? , I dont wanna know")'''

#program to calculate the factorial of a number eg. 10
result = 1
i = 1
while i <= 10:
    result = result * i
    i = i+1

print("the factorial of 100 is: {}" .format(result))