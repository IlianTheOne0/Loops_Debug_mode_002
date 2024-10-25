beginning = int(input('Beginning: '))
end = int(input('End: '))

beginning, end = (end, beginning) if beginning > end else (beginning, end)

def sumOfEvenNumbersFunction(beginning, end, bool):
    result = int()
    len = 0

    while beginning != end + 1:
        if beginning % 2 == 0:
            result += beginning
            if bool: len += 1

        beginning += 1

    if not bool: return result
    else: return result/len

def sumOfOddNumbersFunction(beginning, end, bool):
    result = int()
    len = 0

    while beginning != end + 1:
        if beginning % 2 != 0:
            result += beginning
            if bool: len += 1

        beginning += 1

    if not bool: return result
    else: return result / len

def sumOfMultipliesOf9(beginning, end, bool):
    result = int()
    len = 0

    while beginning != end + 1:
        if beginning % 9 == 0:
            result += beginning
            if bool: len += 1

        beginning += 1

    if not bool: return result
    else: return result / len

def isInteger(function):
    result = round(function, 3)

    if result.is_integer():
        result = int(result)

    return result

print('1. Sum of even numbers:', sumOfEvenNumbersFunction(beginning, end, False))
print('2. Sum of odd numbers:', sumOfOddNumbersFunction(beginning, end, False))
print('3. Sum of multiples of 9:', sumOfMultipliesOf9(beginning, end, False))
print('~'*50, '\n4. Arithmetic mean of even numbers:', isInteger(sumOfEvenNumbersFunction(beginning, end, True)))
print('5. Arithmetic mean of odd numbers:', isInteger(sumOfOddNumbersFunction(beginning, end, True)))
print('6. Arithmetic mean of of multiples of 9:', isInteger(sumOfMultipliesOf9(beginning, end, True)))

