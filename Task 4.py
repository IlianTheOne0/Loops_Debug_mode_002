temp = list()
result = int()

while True:
    number = int(input('Enter the number: '))

    if number == 7:
        temp.append(number)
        print('Good bye!')
        break
    else:
        temp.append(number)

for i in temp:
    result += i

print('Maximum number of numbers entered:', max(temp))
print('Minimum number of numbers entered:', min(temp))
print('Sum of the entered numbers:', result)