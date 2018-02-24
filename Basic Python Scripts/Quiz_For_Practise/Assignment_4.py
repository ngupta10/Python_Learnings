# 1.Build an interactive application which should simulate a Quiz contest. The following questions might be asked as
# input from user:
#Choose level (easy, intermediate, and hard): --> 3 modes of difficulty and user should input one of these choices.
#Please give us the number of question you want to attempt:  --> No of questions thrown should be the number entered
# through this prompt.
#Specify the question type (multiplication:M, addition:A, subtraction:S, division:D):  --> One of these operations to
# be performed.
#If the answer is right or wrong, appropriate messages should be printed and move to next question if attempt count
# is not exceeded.
#Hint: Random utility can be used to change complexity of questions.

#The program should ask if the user wants to continue even after attempting the number of questions specified and
# accordingly should loop or terminate.



import random
import sys

print("********************************* QUIZ *****************************************")
type_list = ["A", "a", "M", "m", "D", "d","S", "s"]

lev_list = ["easy","intermediate","hard"]

cont_or_exit_list = ["c","C"]


level = raw_input("Choose level (easy, intermediate, and hard): ")

if(level not in lev_list):
    sys.exit()


no_of_quest = input("Please give us the number of question you want to attempt:")

quest_type = raw_input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): ")




# This function generates random numbers for different levels
def random_generator():

        if level == "easy":
            return random.randint(1,5)



        elif level == "intermediate":
            return random.randint(5,10)



        elif level == "hard":
            return random.randint(10,20)

        else:
            print ("The level you mentioned is in appropriate")




# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x,y):
    x = x
    y = y
    z = x / y
    return z

count =1

while count <= no_of_quest:

    if quest_type not in type_list:
        print("The Operation you mentioned %s is not in the program" % quest_type)
        break



    if quest_type == "M" or quest_type == "m":

        num1 = random_generator()
        num2 = random_generator()


        try:
                x = int(input("What's %i multiplied by %i : "%(num1,num2)))
                if(x == multiply(num1,num2)):
                    print("That's right -- well done")


                else:
                    print ("Wrong Answer")

        except ValueError:
                print("Make sure to enter a number.")


    elif quest_type == "s" or quest_type == "S":
        num1 = random_generator()
        num2 = random_generator()

        try:
                x = int(input("What's %i subtracted by %i : "%(num1,num2)))
                if(x == subtract(num1,num2)):
                    print("That's right -- well done")

                else:
                    print ("Wrong Answer")

        except ValueError:
                print("Make sure to enter a number.")

    elif quest_type == "A" or quest_type == "a":
        num1 = random_generator()
        num2 = random_generator()

        try:
                x = int(input("What's %i addition with %i : " % (num1, num2)))
                if (x == add(num1, num2)):
                    print("That's right -- well done")

                else:
                    print ("Wrong Answer")

        except ValueError:
                print("Make sure to enter a number.")

    elif quest_type == "D" or quest_type == "d":
        num1 = random_generator()
        num2 = random_generator()

        try:
                x = int(input("What's %i divided by %i : " % (num1, num2)))
                if (x == divide(num1, num2)):
                    print("That's right -- well done")

                else:
                    print ("Wrong Answer")

        except ValueError:
                print("Make sure to enter a number.")
    if count == no_of_quest:
        cont_or_exit = raw_input("Continue or exit (Continue:C, Exit: E) : ")
        if cont_or_exit in cont_or_exit_list:
            count = count-1
    count += 1



