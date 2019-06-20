bases = [10, 20, 30]
heights = [2, 3, 4]

for base in bases:
    print('---------------------')
    for height in heights:
        area = base * height / 2
        print('Luas dari alas: %d, dan tinggi: %d adalah %r' % (base, height, area))
