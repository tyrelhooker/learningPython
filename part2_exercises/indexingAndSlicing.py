"""
Define a list named L that contains 4 strings or numbers. Then experiment with the boundary cases.
a. What happens when you try to index out of bounds, L[4]? - receive an error
b. what about slicing out of bounds? - The slice will capture the whole list
items.
c. How does Py handle it if you try to extract a sequence in reverse,
with the lower bound greater than the higher bound (L[3:1])? It appears to
insert at the first number index
"""

L = [6, 7, 8, 9]
# L[2:1] = '5'
print(L[2:1], L)

