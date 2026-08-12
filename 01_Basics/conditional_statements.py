# age = 20

# if age >= 18:
#     print("You are eligible to vote")

# marks = int(input("Enter your marks"))

# if marks >= 90:
#     print("A")
# elif marks >= 60:
#     print("B")
# else:
#     print("C")

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

    # Camparision Operators

# x = 10

# print(x > 5)
# print(x < 5)
# print(x == 10)
# print(x != 10)

# password = "python123"

# if password == "python123":
#     print("Login successful")
# else:
#     print("Wrong password")

    # 1️⃣ and

age = 20
has_id = True

if age >= 18 and has_id == True:
    print("Entry allowed")
else:
    print("Entry denied")

    # 2️⃣ or
    age = 16
has_id = True

if age >= 18 or has_id == True:
    print("Entry allowed")
else:
    print("Entry denied")

    # 3️⃣ not
is_raining = False

if not is_raining:
    print("Go outside")
else:
    print("Take umbrella")

    # 4️⃣ Nested if

age = 20
has_id = True

if age >= 18:
    if has_id == True:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

    # practice 

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")


age = 20
has_id = True
is_student = True

if age >= 18 and has_id:
    if is_student:
        print("Student Entry")
    else:
        print("Normal Entry")
else:
    print("Entry Denied")
