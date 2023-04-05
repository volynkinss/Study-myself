# Displaying even numbers in range

numbers = range(1, 10)
even_numbers = 0
for number in numbers:
    if number % 2 == 0:
        print(number)
        even_numbers += 1
    else:
        continue
print(even_numbers, "even numbers on display")
