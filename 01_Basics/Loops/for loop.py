# Loops
#  Loops ka use kisi kaam ko baar-baar repeat karne ke liye hota hai.

numbers = [10, 20, 30]

for number in numbers:
    print(number)

    # range()
for i in range(3):
    print(i)

    # 🔹 range(start, stop)
for i in range(3, 8):
    print(i)  

    # 🔹 range(start, stop, step)
for i in range(2, 11, 2):
    print(i)

    # reverse counting
# range() mein negative step dekar reverse ja sakte hain:
for i in range(10, 4, -1):
    print(i)    

    # for loop + if
for i in range(1, 8):
    if i % 2 != 0:
        print(i)

#    for loop + String

word = "Python"

for char in word:
    print(char)     

    # for loop + Dictionary
person = {
    "name": "Rahul",
    "city": "Delhi"
}

for key in person:
    print(key)   
#question
student = {
    "name": "Shivani",
    "age": 20,
    "course": "BCA"
}

for value in student.values():
    print(value)

    person = {
    "name": "Rahul",
    "age": 21,
    "city": "Delhi"
}

for value in person.values():
    print(value)

    # sum of element

    numbers = [5, 10, 15]

total = 0

for number in numbers:
    total = total + number

print(total)

# 🔹 break
# break loop ko turant stop kar deta hai.

for i in range(1, 6):
    if i == 4:
        break
    print(i)

    # 🔹  continue
# continue current iteration ko skip karta hai, lekin loop ko stop nahi karta.
for i in range(1, 6):
    if i == 2:
        continue
    print(i)

    # 🔹 pass
# break → loop stop 🛑
# continue → current iteration skip ⏭️
# pass → kuch nahi karo, loop normally chalega

for i in range(1, 5):
    if i == 3:
        pass
    print(i)


