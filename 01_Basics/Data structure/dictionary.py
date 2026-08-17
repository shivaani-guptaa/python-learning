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

