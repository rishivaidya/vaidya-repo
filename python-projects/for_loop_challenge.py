# Draw shape based on list
# Given is numbers = [5, 5, 2, 5, 5, 2, 2]

numbers = [5, 5, 2, 5, 5, 2, 2]

for x_count in numbers:
    output = ''
    for i in range(x_count):
        output += 'x'
    print(output)