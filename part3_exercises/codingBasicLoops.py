# PartIII(1) Coding Basic Loops

# (1)(a)
# Write a for loop that prints the ASCII code of each character in a string
# named S. Use the builtin function ord(character) to convert each character
# to an ASCII integer.

S = 'Test'
computedSum = 0
charList = []

for char in S:
    print(ord(char))



# (1)(b)
# Change your loop to compute the sum of the ASCII codes of all the
# characters in a string.

for char in S:
    computedSum += ord(char)

print(computedSum)

# (1)(c)
# Change your code again to return a new list that contains the ASCII codes
# of each character in the string. Does the expression map(ord, S) have a
# similar effect? How about [ord(c) for c in S]?

for char in S:
    charList.append()

