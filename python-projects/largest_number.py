# Find the largest number in a list

numbers = [1, 2, 3, 4, 5, 4]
largest = numbers[0]
for x in numbers:
    if x > largest:
        largest = x
print(largest)