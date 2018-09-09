print("Hello, and welcome to Character Stat Creator!")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
sex = input("Are you a boy, or a girl: ")
siblings = int(input("How many siblings do you have? "))
work = int(input("How many days a week do you work? "))
school = int(input("How many years did you spend in school? "))
self = int(input("In a scale of 1 - 10, how would you rate yourself? "))
race = 0

def years(age):
    if age < 10:
        print("Hello")

    elif age > 10:
        print("Good bye")
years()