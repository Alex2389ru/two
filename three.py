a = int(input('Число'))
b = 0

for i in range(0, a):
    if i % 3 != 0:
        continue
    b += i
print(b)