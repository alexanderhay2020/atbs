print 'Hello World'
print 'What is your name?'
myname=raw_input()
print 'It is good to meet you ' + myname
print 'Your name is ' + str(len(myname)) + ' characters.' # cannot combine str and ints in a nprint function, needs to be one or the other
print 'What is your age?'
myage=raw_input()
print 'You will be ' + str(int(myage)+1) + ' in a year.'
