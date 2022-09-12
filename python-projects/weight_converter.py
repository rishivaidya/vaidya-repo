import math

# Convert weight from pounds to kg or vice versa

weight  = float(input('Weight: '))
unit = input('(K)g or (L)bs?: ')

if unit.upper() == 'L':
    kg_weight = weight * 0.45
    print(f'{weight} is {kg_weight} Kg')
elif unit.upper() == 'K':
    lbs_weight = weight / 0.45
    print(f'{weight} is {lbs_weight} Lbs')
else:
    print('Incorrect unit!')
