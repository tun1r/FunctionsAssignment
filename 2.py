'''Identify and correct the errors in this function. This function checks if the given number is within the range 3 to 9, both limits being inclusive.
def test_range(float n):
    if n in range(3,9):
        print( n, "is not in the range")
    else :
        print(n, "is in the given range.")
test_range(5)
'''
def test_range(n):
    if n in range(3,9+1):
        print( n, "is in in the range")
    else :
        print(n, "is not in the given range.")
test_range(5)
