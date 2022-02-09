# a = 5
# b = a
# print(f'a: {a} - b: {b}')
# a = 10
# print(f'a: {a} - b: {b}')

# a = [1, 2, 3]
# b = a
# c = [a, b]
# print(c)
# a.append(100)
# print(f'a: {a} - b: {b} - c: {c}')

a1 = [1, 2, [100, 101], 3, 4]
b1 = list(a1)
a1.append(5)
print(a1)
print(b1)
a1[2].append(102)
print(a1)
print(b1)
