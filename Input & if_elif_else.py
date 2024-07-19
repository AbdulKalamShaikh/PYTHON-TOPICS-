##########input######
#The input() function allows user input.
#A String, representing a default message before the input.

'''
a=input()
print(a)
'''
'''b=input('Enter name: ')
print(b)'''

'''c=input('Enter number: ') #This is wrong because "input" by default take a string data
print(c)'''

'''d=int(input('Enter Number: '))
print('Number: ',d)'''

##############IF/ELIF_ELSE
#logical condition
#>Greater
#>=Greater than equal
#< less than
#<=less than equal
#==equal
#!= not equal

############1
'''a=10
b=5

if(a>b):
    print('a is bigger number')
else:
    print('b is bigger number')
'''

###############2
'''
a=5
b=5
if(a>b):
    print('a is bigger number')
elif(a==b):
    print('a and b is equals')
else:
    print('b is bigger number')
'''

#############3 input
'''
a=int(input('Enter number1: '))
b= int(input('Enter number2: '))

if(a>b): 
    print('A is bigger')
elif(a==b):
    print('A and B are equals')
else:
    print('B is bigger')
'''

###########4 and 
'''
a=int(input('Enter number1: '))

if(a>0 and a<=10): 
    print('1 to 10 Group')
elif(a>10 and a<=20):
    print('11 to 20 group')
else:
    print('21+ group')
'''

#############5 or
#Enter only mango,banana
'''
a=input('Enter Fruit Name: ')

if(a=="mango" or a=="banana"):
    print('Yes this is right')
else:
    print('Wrong')
'''

###########6 not
'''
a=int(input('Enter Number1: '))
b=int(input('Enter Number2: '))

if(not a>b):
    print('A is not bigger')
else:
    print('B is bigger')
'''
#asaas