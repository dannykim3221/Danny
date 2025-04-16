def gugu(a, b) :
    for i in range(1, 10) :
        for j in range(a, b + 1) :
            print(f'{j} x {i} =  {j * i:2d}', end='\t')
        print()

gugu(2, 5)
print()
gugu(6, 9)
