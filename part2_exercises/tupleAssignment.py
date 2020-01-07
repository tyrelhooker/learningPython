'''
What is happening to X and Y below?d
'''
X = 'spam'
Y = 'eggs'
X, Y = Y, X
print(X, Y)


# Dictionaries are't accessed by offsets so what does the following frag do?
D = {}
D[1] = 'a'
D[2] = 'b'
print(D)

# Create a dictionary E with three entries, for keys 'a', 'b', and 'c'.
# a. What happens when you try to index a non-existent key, D['d']?
# What does python do if you try to assign to a nonexistent key 'd', D['d'] =
# 'spam'?
# How does this compare to out-of-bounds assignments and references for
# lists? Does this sound like the rule for variable names?

E = {
    'a': 'Tony',
    'b': 'Toby',
    'c': 'Tody'
}

E['d'] = 'spam'


print(E)

