# The loop will continually update the variable name,
# until 'your name is typed' then the condition of while loop with be false
# loop will no longer run

# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')


while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')