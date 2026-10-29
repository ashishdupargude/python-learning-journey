
# Day 8: Python Tuples

languages = ("Python", "Java", "JavaScript")

print(languages)
print(languages[0])
print("Total languages:", len(languages))

# Tuples cannot be changed after creation.

# Day 8: Python Sets

numbers = {10, 20, 30, 20, 10}

print("Original set:", numbers)

numbers.add(40)
print("After adding:", numbers)

numbers.remove(20)
print("After removing:", numbers)

print("Total unique numbers:", len(numbers))
