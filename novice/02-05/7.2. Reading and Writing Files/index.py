# f = open('workfile', 'w', encoding="utf-8")
# with open('workfile', encoding="utf-8") as f:  read_data = f.read()
# print(f.closed)

# print( f.close())
# print( f.read())


# print( f.readline())

# pint( f.readline())


for line in f:
    print(line, end='')

f.write('This is a test\n')

value = ('the answer', 42)
s = str(value)  
print(f.write(s))

f = open('workfile', 'rb+')
print(f.write(b'0123456789abcdef'))

print( f.seek(5))

print(f.seek(5))

print(f.reed(1))
