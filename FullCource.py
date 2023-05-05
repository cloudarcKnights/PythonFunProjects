

# 29 Inheritance (inhert the attributes of another class without having to write it out again) 

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()

# 28 Class Functions 
from student import Student

student1 = Student("Oscar", "Accounting", "3.1")
student2 = Student("Phyllis", "Business", "3.8")

print(student2.on_honor_roll())


# 27 Multiple choice Quiz
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct" )

run_test(questions)

# 26 Classes & Objects 

from student import Student

student1 = Student("Jim", "Business", "3.1", False)
student2 = Student("Pam", "Art", "2.5", True)

print(student2.gpa)


# 25 Modules and Pip (need to have a module file with tools in it) www.list of python modules.com

import useful_tools

print(useful_tools.roll_dice(10))

24 Writing to File 
employee_file = open("employoo1.txt", "w")

employee_file.write("Toby in human resources")
employee_file.write("\nKelly in customer service")

employee_file.close()

23 Reading Files

employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)

print(employee_file.readable())
print(employee_file.read())
print(employee_file.readlines())


employee_file.close()

22 Try/Exceptions

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("invalid input")

# 21 building a Translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))


# 20 2D Lists & Nested Loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in number_grid:
    for col in row:
        print(col)

# 19 Exponent Function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 4))

# 18 For Loops
friends = ["Jim", "Karen", "Kevin"]

for index in range(5):
   if index == 0:
      print("first Iteration")
   else:
      print("Not first")


# 17 Building a Guessing Game

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses: 
    print("Out of Guesses, You Lose!")
else:

    print("You Win!")


# 16 While Loops
i = 1
while i <= 10:
    print(i)
    i = i + 1 
    # i += 1 Shortcut

print("Done with Loop")

# 15 Dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

print(monthConversions.get("lll", "Not a valid key"))


# 14 Better Calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)

else:
    print("Invalid Operator")

# 13 If Statements & Comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3
    
print(max_num(3, 40, 5))


# 12 If Statements
is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and (is_tall):
    print("You are not a male, but are tall")
else:
    print("you are either not a male and not tall")

# 11 Return function
def cube(num):
    return num*num*num


result = cube(4)
print(result)


# 10 Functions
def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age))


sayhi("Mike", 39)
sayhi("Steve", 40)

# 9 Tuples used for data that can't be changed
coordinates = [(4, 5), (3, 8) (2, 9)]
coordinates[1] = 10
print(coordinates[1])

# 8
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

friends2 = friends.copy()
print(friends2)

# 7
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends [1] = "Mike"
print(friends[1:3])

# 6
name = input("what is your name: ")
age = input("How old are you: ")
color = input("what is your favorate color: ")

print("Best person is " + name )
print("This is how old he is " + age )
print("His favorate color is " + color)

# 6
color = input ("Enter a color: ")
plural_noun = input ("Enter a Plural Noun: ")
celebrity = input ("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)


# 5
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)


# 4
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)


# 3
from math import *
my_num = -5
print(sqrt(36))

# 2
phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))


# 1
character_name = "Tom"
character_age = 50.45455
is_male = False

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

