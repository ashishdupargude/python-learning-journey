# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#             return n

# l = ["Harry","Rohan","Shubham","an"]
# print(rem(l,"an"))


def rem(l, word):
    n = []

    for item in l:
        if item != word:
            n.append(item)

    return n  # Outside the for loop


l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))