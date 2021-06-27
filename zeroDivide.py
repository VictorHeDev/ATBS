def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# Exception handling - detect errors, handle them, continue to run
# The code that could potentially have an error is put in the 'try' clause
# Program execution moves to the start of a following 'except' clause
# if an error happens
