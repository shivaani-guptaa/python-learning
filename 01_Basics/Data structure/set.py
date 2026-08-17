# 🐍Set : Set multiple values store karta hai, lekin duplicate values automatically remove kar deta hai.
fruits = {"apple", "mango", "apple", "banana", "mango"}

print(fruits)  #Yahan "apple" aur "mango" repeat hue hain, isliye set mein ek-ek hi rahenge.

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)

# a = {}    empty dictionary
# a = set()  empty set

numbers = {1, 2, 3, 2, 1, 4, 3}

print(len(numbers))

# Set mein ek new value add karne ke liye add() use karte hain:

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# 🔹 remove()

# Set se kisi item ko remove karne ke liye remove() use karte hain:
numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)

# 🔹 discard()

# discard() bhi set se item remove karta hai
fruits = {"apple", "mango", "banana"}

fruits.discard("orange")

print(fruits)

# remove() → item nahi mila to error
# discard() → item nahi mila to koi error nahi

# 🔹 pop()

# Set mein pop() kisi ek item ko remove karta hai.
numbers = {10, 20, 30}

numbers.pop()

print(numbers)

# clear() poore set ko empty kar deta hai:

fruits = {"apple", "mango", "banana"}

fruits.clear()

print(fruits)

# union()

# union() do sets ke saare unique elements ko combine karta hai.
a = {10, 20, 30}
b = {30, 40, 50}

print(a.union(b))

# intersection()

# intersection() do sets mein jo values common hain, sirf unhe deta hai.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.intersection(b))

# difference()

# difference() pehle set mein jo values hain, lekin second set mein nahi hain, unhe deta hai.

a = {10, 20, 30, 40}
b = {30, 40, 50}

print(a.difference(b))

# symmetric_difference() : woh values deta hai jo sirf ek set mein hain, dono mein common nahi.

a = {10, 20, 30}
b = {30, 40, 50}

print(a.symmetric_difference(b))

# union() → dono ke saare unique
# intersection() → dono mein common
# difference() → pehle mein, doosre mein nahi
# symmetric_difference() → sirf ek mein, common nahi
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# issubset()

# Check karta hai ki kya ek set ke saare elements doosre set ke andar hain.
a = {10, 20}
b = {10, 20, 30, 40}

print(a.issubset(b))

# issuperset()

# issuperset() issubset() ka opposite direction mein check karta hai.
# a.issubset(b) → a, b ke andar hai?
# a.issuperset(b) → a, b ko contain karta hai?

a = {10, 20, 30, 40}
b = {20, 30}

print(a.issuperset(b))

# isdisjoint()

# isdisjoint() check karta hai ki do sets mein koi common element hai ya nahi.
# Agar koi common element nahi hai → True

a = {10, 20, 30}
b = {40, 50, 60}

print(a.isdisjoint(b))



