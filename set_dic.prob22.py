
z = set()
for x in range (1,11):
    x = int(input('введите 10 чисел: '))
    z.add(x)
    print(tuple(z))

    z.add(234)
    print(z)