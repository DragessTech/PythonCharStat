#Initializing stats
strength = 0
constitution = 0
wisdom = 0
intelligence = 0
dexterity = 0
charisma = 0
race = 0

#Create function to show Stats when called
def stats():
    print("Name = " + name)
    print("Age = " + age)
    print("Race = " + Race)
    print("Class = " + Class)
    print("STR = " + strength)
    print("DEX = " + dexterity)
    print("CON = " + constitution)
    print("INT = " + intelligence)
    print("WIS = " + wisdom)
    print("CHR = " + charisma)

#taking input from user
print("Hello, and welcome to Character Stat Creator!")
name = raw_input("Please enter your name: ")
age = input("Please enter your age: ")
sex = raw_input("Are you a boy, or a girl: ")
siblings = input("How many siblings do you have? ")
work = input("How many days a week do you work? ")
school = input("How many years did you spend in school? ")
self = input("In a scale of 1 - 10, how would you rate yourself? ")
Class = "Warrior"
Race = "Human"



#Runs stats function to show stats
stats()
