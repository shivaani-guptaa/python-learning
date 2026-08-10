# list = List ek variable me multiple values store karne ke kaam aati hai

data = ["Shivani", 20, 85.5, True]

print(data)

data = ["Shivani", 20, 85.5, True]

print(data[0])
print(data[1])
print(data[-1])  

numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(numbers[2])
print(numbers[-2])

fruits = ["apple", "banana", "mango", "orange", "grapes"]

print(fruits[1:4])
print(fruits[:3])
print(fruits[2:])

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)
numbers = [10, 20, 30, 40]

numbers[2] = 100

print(numbers)

fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)

fruits = ["apple", "banana", "mango"]

fruits.insert(1, "orange")

print(fruits)
# remove
fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)
# pop() 🗑️

fruits = ["apple", "banana", "mango"]

fruits.pop(1)

print(fruits)

fruits = ["apple", "banana", "mango"]

fruits.pop()

print(fruits)

# sort() 🔤🔢  =  sort() list ko ascending order me arrange karta hai.

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# reverse() 🔄

# reverse() list ke elements ka order ulta kar deta hai.

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

numbers = [10, 20, 10, 30, 10, 40, 20]

print(numbers.count(10))
print(numbers.count(20))
print(numbers.count(50))

# index() kya karta hai?

# List mein kisi value ka first position/index batata ha

numbers = [10, 20, 30, 20, 40, 50]

print(numbers.index(20))
print(numbers.index(40))
print(numbers.index(50))

# copy() kya karta hai?

# Ek list ki copy banata ha

numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)


