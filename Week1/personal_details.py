print("========== WEEK 1 PROGRAMS ==========\n")

# 1️⃣ Personal Details
print("----- Personal Details -----")
print("Name: Bhavana")
print("Age: 21")
print("College: VTU")
print("Course: Data Analytics Internship")
print()

# 2️⃣ Arithmetic Operations
print("----- Arithmetic Operations -----")
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print()

# 3️⃣ Even or Odd
print("----- Even or Odd -----")
num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
print()

# 4️⃣ Largest of Three Numbers
print("----- Largest of Three -----")
x = 12
y = 25
z = 18
if x >= y and x >= z:
    print("Largest:", x)
elif y >= x and y >= z:
    print("Largest:", y)
else:
    print("Largest:", z)
print()

# 5️⃣ Multiplication Table
print("----- Multiplication Table -----")
number = 5
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
print()

# 6️⃣ Factorial
print("----- Factorial -----")
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

print("\n========== END OF WEEK 1 ==========")
