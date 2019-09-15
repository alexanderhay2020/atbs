# This works through the 'while loop' portion of ATBS

#i=0
#while i < 5:
#    print 'hello world'
#    i=i+1

#name=''
#while name != 'your name':
#    print 'please type your name'
#    name=raw_input()
#print 'thank you'


# Using a 'break' command
# program does same thing as program above

#name=''
#while True: #starts infinite loop
#    print 'please type your name'
#    name=raw_input()
#    if name=='your name':
#        break
#print 'thank you'


# Using a 'continue' command

i=0
while i<5:
    i=i+1
    if i==3:
        continue
    print 'i=' + str(i)
