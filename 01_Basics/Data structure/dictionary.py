# "name"  → key
# "Shivani" → value

# "age"   → key
# 20      → value

# "marks" → key
# 85      → value

# Dictionary ko { } curly brackets se banate hain.
# Dictionary mutable hoti hai, yani uski value change kar sakte hain.

student = {
    "name": "Shivani",
    "age": 20,
    "course": "BCA"
}

print(student["course"])

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2024
}

print(car["brand"])
print(car["year"])

# Dictionary mein value change karna

student = {
    "name": "Shivani",
    "age": 20,
    "course": "BCA"
}

student["age"] = 21

print(student["age"])

# Dictionary mein new item add karna

person = {
    "name": "Rahul",
    "age": 21
}

person["city"] = "Delhi"

print(person)

# Dictionary se item delete karna — del

fruits = {
    "a": "apple",
    "b": "banana",
    "c": "cherry"
}

del fruits["b"]

print(fruits)
# len() with Dictionary

# len() dictionary mein total key-value pairs count karta hai
person = {
    "name": "Rahul",
    "age": 21,
    "city": "Delhi",
    "course": "BCA"
}

print(len(person))

# keys()
person = {
    "name": "Rahul",
    "age": 21,
    "city": "Delhi"
}

print(person.keys())

# values()

person = {
    "name": "Rahul",
    "age": 21,
    "city": "Delhi"
}

print(person.values())

# items() :  items() dictionary ke key + value dono deta hai.

student = {
    "name": "Shivani",
    "age": 20
}

print(student.items())

# get() Method
# get() dictionary mein kisi key ki value access karta hai.
student = {
    "name": "Shivani",
    "age": 20
}

print(student.get("name"))

# ⭐ [] aur get() mein difference
# Agar key dictionary mein hai:
print(student["age"])
print(student.get("age"))

# Lekin agar key nahi hai:

print(student.get("city"))  #get() error nahi deta. 

# get() mein default value bhi de sakti ho.

person = {
    "name": "Rahul",
    "age": 21
}

print(person.get("city", "Not Found"))

# pop()  : pop() dictionary se kisi key-value pair ko remove karta hai.

fruits = {
    "a": "apple",
    "b": "banana",
    "c": "cherry"
}

fruits.pop("b")

print(fruits)

# 🔹 popitem()
# popitem() dictionary ka last key-value pair remove karta hai.
person = {
    "name": "Rahul",
    "age": 21,
    "city": "Delhi"
}

person.popitem()

print(person)


# clear() poori dictionary empty kar deta hai.

fruits = {
    "a": "apple",
    "b": "banana"
}

fruits.clear()

print(fruits)

# {} → Empty dictionary
# [] → Empty list
# () → Empty tuple



# update() se dictionary mein multiple key-value pairs add ya existing values update kar sakte hain.
student = {
    "name": "Shivani",
    "age": 20
}

student.update({
    "age": 21,
    "course": "BCA"
})

print(student)

person = {
    "name": "Rahul",
    "age": 21
}

person.update({
    "age": 22,
    "city": "Delhi"
})

print(person)
# in se check kar sakte hain ki koi key dictionary mein exist karti hai ya nahi.
person = {
    "name": "Rahul",
    "age": 21,
    "city": "Delhi"
}

print("city" in person)
print("phone" in person)

# 🔹 not in
student = {
    "name": "Shivani",
    "course": "BCA"
}

print("age" not in student)
print("name" not in student)

# 🔹 fromkeys()

# fromkeys() se multiple keys wali new dictionary bana sakte hain.
keys = ("name", "age", "city")

student = dict.fromkeys(keys, "Unknown")

print(student)
#question

keys = ("a", "b", "c")

data = dict.fromkeys(keys, 0)

print(data)

# 🔹 Dictionary Comprehension

numbers = [1, 2, 3, 4]

square = {}

for n in numbers:
    square[n] = n * n

print(square)

# 2nd method
numbers = [1, 2, 3, 4]

square = {n: n * n for n in numbers}

print(square)
#que
numbers = [1, 2, 3]

result = {n: n + 10 for n in numbers}

print(result)

# que dic with condition
numbers = [1, 2, 3, 4, 5, 6]

even = {n: n * n for n in numbers if n % 2 == 0}

print(even)

# que 
numbers = [1, 2, 3, 4, 5]

result = {n: n * 2 for n in numbers if n % 2 != 0}

print(result)


