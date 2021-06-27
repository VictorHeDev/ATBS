# collatz sequence

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number

number = int(input('Give me a Number: '))

try:
    looping = True
    while looping:
        number = collatz(number)
        if number == 1:
            looping = False
except:
    print('Please enter a valid integer')




