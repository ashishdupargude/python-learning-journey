
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not yet eligible to vote.")



marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 75:
    print("Distinction")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")
