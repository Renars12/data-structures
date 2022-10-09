name = 'Anna' #string
Age = 17 #integer
Height = 1,68  #float
has_laptop = True  #boolean

names = ['Anna', 'Oskars', 'Jenifer', 'Anna']
ages = [17,18,18,15]

print(f'{names[0]} is {ages[0]} years old.')
print(f'{names[1]} is {ages[1]} years old.')
print(f'{names[2]} is {ages[2]} years old.')
print(f'{names[3]} is {ages[3]} years old.')

names = ['Anna', 'Oskars', 'Jenifer', 'Anna', 'Miks']
ages = [17,18,18,15,20]

for number in range(len(names)):
    print (f'{names[number]} is {ages[number]} years old.')
