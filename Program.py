#PYTHON ITEM 36 PROGRAM
#Assigning integer, string, and float variables respectively.
int_variable = 4
string_value = "these are words"
float_variable = 3.14

#Printing the variables
print int_variable
print string_value
print float_variable

#Using operators
# +
def adding(x,y):
    addition = x + y
    return addition
print adding(3,5)
# -
def subtracting(x,y):
    subtraction = x - y
    return subtraction
print subtracting(10,5)
# *
def multiply(x,y):
     multiplication = x * y
     return multiplication
print multiply(3,5)
# /
def divide(x,y):
    division = x / y
    return division
print divide(14,7)
# %
def remaining(x,y):
    remainder = x % y
    return remainder
remaining = (10,3)
# +=
a = 10
c = 12
c += a
print"C = ", c
# =
a = 10
b = 5
c = a + b
print "C = ", c
#logical operators and conditional statements
d = 10
e = 15
f= 10
x = True
y = False
if d == e and d == f:
    print "D = E"
elif d == e or d == f:
    print "D = F"
elif not x:
    print "True"
else:
    print "Nothing is equal"


#Loops
#While
counter = 0
while counter < 10:
    print counter
    counter = counter + 1
#For
for counter in range(10,20):
    print counter
#Lists
list_of_states = ["Oregon",
                  "Washington",
                  "California",]
for state in list_of_states:
    print state

#Tuple
state_tuple = ("Idaho","Colorado","Michigan")
for state in ("Idaho","Colorado","Michigan"):
    print state

#Function
def stringfunction(str):
    "Words"
    print str
    return

stringfunction("Words")

