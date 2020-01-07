
a = 2 ** 16
b = 2 / 5, 2 / 5.0

c = 'spam' + 'eggs'
S = 'ham'
d = 'eggs ' + S
e = S * 5
f = S[:0]
g = 'green %s and %s' % ('eggs', S)
h = 'green {0} and {1}'.format('eggs', S)

i = ('x',)[0]
j = ('x', 'y')[1]

L = [1,2,3] + [4,5,6]
k = L, L[:], L[:0], L[-2], L[-2:]
m = ([1,2,3] + [4,5,6])[2:4]
n = [L[2], L[3]]
# L.reverse()
o = L.index(1)

p = {'a': 1, 'b': 2}['b']
D = {'x':1, 'y':2, 'z':3}
D['w'] = 0
q = D['x'] + D['w']
D[(1,2,3,)] = 4
r = list(D.keys()), list(D.values()), (1,2,3) in D

s = [[]], ['', [], (), {}, None]



def reverseList(L):
    L.reverse()
    print('reverseList(L): ', L)
    print('o in reverseList(L): ', o)


def sortList(L):
    # reverseList(L)
    L.sort()
    print('sortList(L): ', L)


keylist = [a, b, c, S, d, e, f, g, h, i, j, L, k, m, n, o, p, D, q, r, s]

for char in keylist:
    print(char)

print(type(i))

# reverseList(L)
# sortList(L)
# print('Index of L: ', o)
# print('Basic Variable L: ', L)
# print(s)





