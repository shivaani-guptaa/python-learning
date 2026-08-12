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
#➡️  remove
fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)
#➡️  pop() 🗑️

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

#➡️  reverse() 🔄

# reverse() list ke elements ka order ulta kar deta hai.

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

numbers = [10, 20, 10, 30, 10, 40, 20]

print(numbers.count(10))
print(numbers.count(20))
print(numbers.count(50))

# ➡️ index() kya karta hai?

# List mein kisi value ka first position/index batata ha

numbers = [10, 20, 30, 20, 40, 50]

print(numbers.index(20))
print(numbers.index(40))
print(numbers.index(50))

# ➡️ copy() kya karta hai?

# Ek list ki copy banata ha

numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)

# ➡️  clear()

#➡️  clear() list ke saare elements hata deta hai, aur list empty ho jaati hai

numbers = [10, 20, 30, 40]

numbers.clear()

print(numbers)

# ➡️  del keyword

# ➡️ Ye remove() aur pop() se thoda different hai.
numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)

#➡️  que 2 

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)

#➡️  Slicing mein starting index include hota hai, ending index exclude hota hai.

# ➡️ del se poori list bhi delete kar sakte hain:   it gives error
# numbers = [10, 20, 30]

# del numbers

# print(numbers)

# 🧠 Difference
del numbers[1]

# ➡️ Sirf ek element delete

del numbers[1:4]

# ➡️ Kuch elements delete

del numbers

# ➡️ Poora variable delete


# 🔹 List Unpacking

# List ke elements ko alag-alag variables mein directly assign karna.
colors = ["red", "green", "blue"]

x, y, z = colors

print(x)
print(y)
print(z)
#➡️  question....

numbers = [10, 20, 30, 40, 50]

a, *b = numbers    

# *b ka simple meaning

# *b bol raha hai: "Jo values bach jaayein, sab mujhe de do."

print(a)
print(b)

#➡️  question....
numbers = [10, 20, 30, 40, 50]

*a, b = numbers

print(a)
print(b)

#➡️  question....
numbers = [5, 10, 15, 20, 25, 30]

a, *b, c = numbers

print(a)
print(b)
print(c)

# rule
# a → first value
# c → last value
# *b → beech ki saari values 

# ➡️ List + for loop

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)
#➡️  question....

fruits = ["apple", "mango", "banana"]

for fruit in fruits:
    print("I like", fruit)
#➡️  question....
numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)
#➡️  question....

fruits = ["apple", "mango", "banana", "apple"]

for fruit in fruits:
    if fruit == "apple":
        print("Found apple")