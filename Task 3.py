while True:
    number = int(input('Enter the number: '))

    if number == 7:
        print('Good bye!')
        break
    elif number > 0: print('Number is positive')
    elif number < 0: print('Number is negative')
    elif number == 0: print('Number is equal to zero')