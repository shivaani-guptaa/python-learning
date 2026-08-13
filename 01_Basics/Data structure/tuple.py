# 🔹 : TUPLE.........
# Tuple bhi List ki tarah multiple values store karta hai.
# Difference
# List → [] → change kar sakte hain
# Tuple → () → normally change nahi kar sakt

numbers = (10, 20, 30, 40)

print(numbers)

numbers = (10, 20, 30)

numbers[0] = 100

print(numbers)


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
