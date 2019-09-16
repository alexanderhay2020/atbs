# Working through the functions portion of ATBS

import random, sys, os, math # can import more than one module at a time

# sys.exit() kills program

# random.randint(1,10) # creates random integer between 1 and 10

#def hello(): # beginning of new funtcion, defines but does not execute
#    print 'hello'
#    print 'howdy'
#
#hello() # calls function
#hello()
#hello()

#def hello(name): # defines function with input
#    print 'hello ' + name
#
#hello('alex')
#hello('bobo')


# working with returning values

eggs=0

def plusOne(number):
    return number+1
    global eggs # pulls eggs variable from global scope
print plusOne(5)
