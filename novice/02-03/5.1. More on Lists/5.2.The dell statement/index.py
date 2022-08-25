# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple'))

# print(fruits.count('tangerine'))

# print(fruits.index('banana'))

# print(fruits.index('banana', 4))

# fruits.reverse()
# print(fruits)

# fruits.append('grape')
# print(fruits)

# fruits.sort()
# print(fruits)

# print(fruits.pop())


# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry") 
# queue.append("Graham")
# print(queue.popleft() )

# print(queue.popleft() )

# print(queue )




# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)


# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)

# print(stack.pop())

# print(stack)

# print(stack.pop())

# print(stack.pop())

# print(stack)



# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]


# ([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])



# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))

# print(combs)



# vec = [-4, -2, 0, 2, 4]

# print([x*2 for x in vec])

# print([x for x in vec if x >= 0])

# print([abs(x) for x in vec])




# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([weapon.strip() for weapon in freshfruit])



# print([(x, x**2) for x in range(6)])



# [x, x**2 for x in range(6)]
#   File "<stdin>", line 1
# print([x, x**2 for x in range(6)])




# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])


# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]


# print([[row[i] for row in matrix] for i in range(4)])


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)


transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)


print(list(zip(*matrix)))