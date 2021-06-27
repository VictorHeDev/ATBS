def collatz(number):
    if number % 2 == 0:
        result = number // 2
        return result
    else:
        result = number * 3 + 1
        return result

try: 
    n = int(input('Please give me a number: '))
    print(n)
    while n > 1: 
        n = collatz(n)
        print(n)
except ValueError:
    print('Please enter a positive integer that is greater than 1')

