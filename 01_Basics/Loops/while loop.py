# 🔹 while loop
# while loop tab tak chalta hai jab tak condition True hai.
i = 1

while i <= 3:
    print(i)
    i = i + 1
i = 10

while i >= 6:
    print(i)
    i = i - 1

# 🔹 while + if

# while loop ke andar bhi condition laga sakte hain.

i = 1

while i <= 7:
    if i % 2 != 0:
        print(i)
    i = i + 1

    # 🔹 while + break

# while loop mein bhi break use kar sakte ho:

i = 1

while i <= 6:
    if i == 5:
        break
    print(i)
    i = i + 1

    # 🔹 while + continue

# continue current iteration ko skip karta hai.

i = 0

while i < 5:
    i = i + 1

    if i == 2:
        continue

    print(i)
    
    
# while loop + pass
# pass kuch nahi karta, loop normal chalta rehta hai:

i = 1

while i <= 4:
    if i == 2:
        pass
    print(i)
    i = i + 1

    
