def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()

# In general, we wan to avoid duplicating code (DRY)
# This makes our code shorter, easier to read, and easier to update

def sayHello(name):
    print('Hello, ' + name)

sayHello('Victor')

# Parameters are variables that contain arguments
# When a function is called with arguments, the arguments are stored in parameters
