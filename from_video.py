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
