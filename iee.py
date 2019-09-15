# Program from Automate the Boring Stuff
# with if, else, elif statements


# 'if' example
#name='Alice'
#if name == 'Bob': #changed from 'Alice' to illisutrate point
#  print 'Hi Alice'
#print 'Done'

# 'else' example
#password='swordfisgh' #changed from 'swordfish' to illustrate point
#if password=='swordfish':
#    print 'access granted'
#else:
#    print 'wrong password'

# 'elif' (else if) example
#name='Bob'
#age=30
#if name=='Alice':
#    print 'hi Alice'
#elif age<12:
#    print 'ur a kiddo, kiddo'
#elif age>2000:
#    print 'hello vampire'
#elif age<100:
#    print 'ur a grampa'


# Fasley Truthy example

myname=raw_input()
if myname:
    print 'thank you for entering a name'
else:
    print 'you did not enter a name'

# If a name is entered then myname when calling the if command contains a value, making it true.
# Likewise, if something is not entered  myname does not have a value, making it false.
