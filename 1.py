'''Identify and correct the errors in this function. This function should return the sum of the numbers in an iterable.
total = 0
def sum(numbers):
    for x in numbers
    total += x
    return numbers
print(sum((8, 2, 3, 0, 7))'''
total = 0
def sum(numbers):
    global total
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))



