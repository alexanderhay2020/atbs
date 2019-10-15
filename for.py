# Working through for loop in ATBS

#print 'my name is '
#for i in range(5): #initializes i as 0, auto iterates
#    print 'Jimmy Five Times ' +str(i)


# same thing as program befre but with a while loop
# while loops need defining, for loops self define
#i=0
#while i<5:
#    print 'Jimmy Five Times ' + str(i)
#    i=i+1


# range function - defines where i is initialized
#print 'my name is '
#for i in range(5,10, 2): #initializes i as 5, iterates until 10, steps by 2
#    print 'Jimmy Five Times ' +str(i)

# sums 1-100
total=0
for num in range(101):
    total = total + num
print total
