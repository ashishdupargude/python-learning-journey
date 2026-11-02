
# Day 9: Python Dictionaries

employee = {
    "name": "Ashish",
    "age": 27,
    "city": "Pune",
    "role": "Automation Tester"
}

print(employee)
print(employee["name"])
print(employee["age"])
print(employee["role"])





employee = {
    "name": "Ashish",
    "age": 27,
    "role": "Tester"
}

# Add a new key
employee["salary"] = 600000

# Update an existing value
employee["role"] = "Automation Tester"

print(employee)




employee = {
    "name": "Ashish",
    "age": 27,
    "role": "Tester"
}

# Add a new key
employee["salary"] = 600000

# Update an existing value
employee["role"] = "Automation Tester"

print(employee)




employee = {
    "name": "Ashish",
    "age": 27,
    "city": "Pune"
}

employee.pop("age")

print(employee)




employee = {
    "name": "Ashish",
    "age": 27,
    "role": "Automation Tester"
}

for key, value in employee.items():
    print(key, ":", value)
