## No need to declare the variables. They
### are created when the value is assigned

number = 4
helloString = "Hello Hi!!!"

print (number)
print (helloString)
 

 # Explicitly assign the type of the variable

number = int(6)
helloString = str ("Its me")

print (number)
print (helloString)

## Changing integer to String
"""
This is a multiline comment
The integer variable is modified to String and printed.

String variables can be declared either by using single or double quotes:


"""
number = str('Integer modified to String')
print (number)

print(type(number))
print(type(helloString))


'''
Many Values to Multiple Variables
Make sure the number of variables matches the number of values, or else you will get an error.
'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


'''
One Value to Multiple Variables
'''
x = y = z = "Orange"
print(x)
print(y)
print(z)

'''
Unpacking an array
'''
fruits = ["Apple", "Banana", "Cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)