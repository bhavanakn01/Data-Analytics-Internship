print("========== WEEK 2 PROGRAMS ==========\n")

# 1️⃣ List Program
print("----- List Program -----")
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)
print("First Element:", numbers[0])
print()

# 2️⃣ Tuple Program
print("----- Tuple Program -----")
data = (1, 2, 3, 4, 5)
print("Tuple:", data)
print("Second Element:", data[1])
print()

# 3️⃣ Dictionary Program
print("----- Dictionary Program -----")
student = {
    "Name": "Bhavana",
    "Age": 21,
    "Course": "Data Analytics"
}
print("Student Details:", student)
print()

# 4️⃣ Set Program
print("----- Set Program -----")
num_set = {1, 2, 3, 4, 4, 5}
print("Set:", num_set)
print()

# 5️⃣ String Operations
print("----- String Operations -----")
text = "Data Analytics"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print()

# 6️⃣ File Handling
print("----- File Handling -----")
file = open("sample.txt", "w")
file.write("Welcome to Data Analytics Internship")
file.close()

file = open("sample.txt", "r")
print(file.read())
file.close()

# 7️⃣ Exception Handling
print("\n----- Exception Handling -----")
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("\n========== END OF WEEK 2 ==========")
