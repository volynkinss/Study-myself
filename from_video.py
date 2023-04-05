# Doing exersises for teach python

# name = "John Smith"
# age = 20
# new_patient = True

# name = input("What is your name? ")
# favourate_color = input("What is your favourate color? ")
# print(name + " likes " + favourate_color)

# weight_kg = input("What is your weight in kg? ")
# weight_pounds = int(weight_kg) / 0.454
# print("Your weight in kilograms pounds ", weight_pounds)

# name = "Varvara"
# print(name[1:-1])

# first = "Dima "
# last = "Volynkin"
# message = first + " [" + last + "] " + "are a children"
# msg = f"{first} [{last}] are a children"
# print(message)
# print(msg)

# msg = "i want to learn Python to have work without contact people"
# print(len(msg))
# print(msg.upper())
# print(msg.lower())
# print(msg.find("i"))
# print(msg.replace("contact people", "sales to people"))

# price = 1000000
# good_credit = True
# if good_credit:
#    payment = price * 0.1
# else:
#    payment = price * 0.2
# print(f"Need to pull down ${payment}")

# name = input("Input your name ")
# length_of_name = len(name)
# min_length_of_name = 3
# max_length_of_name = 50
# if length_of_name < min_length_of_name:
#    print("Name must be at least 3 charaters")
# elif length_of_name > max_length_of_name:
#    print("name can be maximum of 50 charaters")
# else:
#    print("Name looks good!")

# weight = input("Weight: ")
# weight = int(weight)
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#    converted = weight / 0.454
#    print(f"You are {converted} kilograms")
# elif unit.upper() == "K":
#    converted = weight * 0.454
#    print(f"You are {converted}  pounds")
# else:
#    print("unit unknown")


# help = """start - to start the car
# stop - to stop the car
# quit - to quit"""
# start = "Car started... Reary to Go! "
# stop = "Car stoped."
# started = False
# while True:
#    comand = input().lower()
#    if comand == "help":
#        print(help)
#    elif comand == "start":
#        if started:
#            print("Car is already started!")
#        else:
#            started = True
#            print(start)
#    elif comand == "stop":
#        if not started:
#            print("Car is already stopped!")
#        else:
#            started = False
#            print(stop)
#    elif comand == "quit":
#        break
#    else:
#        print("I don't understand that... ")


# prices = [10, 20, 30]
# print(sum(prices))
# total = 0
# for price in prices:
#    total += price
# print(f"Total: {total}")

# for x in range(4):
#   for y in range(3):
#        print(x, y)

# numbers = [6, 1, 4, 2, 7]
# for item_count in numbers:
#    output = ""
#    for count in range(item_count):
#        output += "L"
#    print(output)

# list_of_numbers = input("Введите числа через пробел: ").split()
# max = list_of_numbers[0]
# for number in list_of_numbers:
#    if number > max:
#        max = number
# print(max)
# print(max(list_of_numbers))

# list_of_numbers = input("Введите числа через пробел: ").split()
# for number in list_of_numbers:
#    if list_of_numbers.count(number) >= 1:
#        list_of_numbers.remove(number)
# print(list_of_numbers)
# DEBILL

# list_of_numbers = input("Введите числа через пробел: ").split()
# unical = []
# for number in list_of_numbers:
#    if number not in unical:
#        unical.append(number)
# print(unical)

# numbers = {
#    "1": "one",
#    "2": "two",
#    "3": "three",
#    "4": "four",
#    "5": "five",
#    "6": "six",
#    "7": "seven",
#    "8": "eight",
#    "9": "nine",
#    "0": "zero",
# }
# text_phone = ""
# phone_number = input("Phone: ")
# for num in phone_number:
#    text_phone += numbers.get(num, "!") + " "
#    print(numbers[num], " ", end="")
# print(text_phone)


# create function of convert smile to emojies
# def convert_massege(message):
#    words = message.split(" ")
#    emojis = {":)": "🙂", ":(": "😒"}
#    reform_message = ""
#    for word in words:
#        reform_message += emojis.get(word, word) + " "
#    return reform_message
#
#
# message = input(">")
# print(convert_massege(message))
#
# message_two = input("...")
# print(convert_massege(message_two))

# exceptions
# try:
#    age = int(input("Age: "))
#    imcome = 20000
#    risk = imcome / age
#    print(risk)
#    print(age)
# except ValueError:
#    print("Invalid value")
# except ZeroDivisionError:
#    print("Age can not be 0!")


# classes & constructions
# class Point:
#    def __init__(self, x, y):
#        pass

#    def move(self):
#        print("move")

#    def draw(self):
#        print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.draw()

# classes & constructions practice
# class Person:
#    def __init__(self, name):
#        self.name = name
#
#    def talk(self):
#        print(f"Hi, I am {self.name}. Nice to see you!")


# Nick = Person("Nick")
# Nick.talk()

# Vlad = Person("Vladlen")
# Vlad.talk()

# from utils import find_max

# list_of_num = input("Введите числа через пробел: ").split()
# maximum = find_max(list_of_num)
# print(maximum)

# 2 Dice
import random


class Dice:
    def roll(self):
        numbers = (1, 2, 3, 4, 5, 6)
        throw = random.choice(numbers)
        return throw


# Dice.roll()

dice1 = Dice()
# dice2 = Dice()
print(dice1.roll(), ",", dice1.roll())
