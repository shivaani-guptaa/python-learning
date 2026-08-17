# 🔹 : TUPLE.........
# Tuple bhi List ki tarah multiple values store karta hai.
# Difference
# List → [] → change kar sakte hain
# Tuple → () → normally change nahi kar sakt

# numbers = (10, 20, 30, 40)

# print(numbers)

# numbers = (10, 20, 30)

# numbers[0] = 100

# print(numbers)


# negative indexing 👇
numbers = (10, 20, 30, 40, 50)

print(numbers[-1])
print(numbers[-2])
# slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

# question 

numbers = (10, 20, 30, 40, 50)

print(numbers[2:])

# count() 👇
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))

# index()
fruits = ("apple", "mango", "banana", "mango", "orange")

print(fruits.index("mango"))

# Tuple Unpacking 🔹
fruits = ("apple", "mango", "banana")

a, b, c = fruits

print(a)
print(b)
print(c)

# * unpacking

fruits = ("apple", "mango", "banana", "orange", "grapes")

a, *b = fruits

print(a)
print(b)
# question 


fruits = ("apple", "mango", "banana", "orange", "grapes")

a, *b, c = fruits

print(a)
print(b)
print(c)
# single-element tuple.

a = (10)   #Ye tuple nahi, simple integer hai:
b = (10,)    #Ye tuple hai 

print(type(a))
print(type(b))

a = ("Python")
b = ("Python",)

print(type(a))
print(type(b))


