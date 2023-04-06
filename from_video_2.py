# guess = 0
# answer = 5

# while guess != answer:
#     guess = int(input("Guess: "))


def multiplay(*nembers):
    total = 1
    for number in nembers:
        total *= number
    return total


print("start")
print(multiplay(1, 2, 3))
print("finish")
