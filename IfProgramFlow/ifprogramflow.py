# name = input("please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess !=5:
#     if guess < 5:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

#age= int(input("How old are you? "))
#if (age >= 16) and (age <= 65):
# if 15 < age < 66:
#     print("Have a good day at work")

# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#
# if (some_condition) or (some_weird_function_that_does_stuff()):
#     # do something

# x = "false"
# if x:
#     print("x is true")

# x = input("Please enter some text ")
# if x:
#     print("You entered {}".format(x))
# else:
#     print("You did not enter anything")
# print(not False)
# print(not True)

# age = int(input("How old are you? "))
# if not(age < 18):
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {} years".format(18-age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me an {}, Bob".format(letter))
