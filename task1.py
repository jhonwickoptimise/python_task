# square pattern::
def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

n = int(input("Enter the size of the square: "))
square_pattern(n)

# number square pattern3:

def number_square_pattern(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j, end=' ')
        print()

n = int(input("Enter the size of the number square: "))
number_square_pattern(n)

# triangle pattern::
def triangle_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end=' ')
        print()

n = int(input("Enter the size of the triangle: "))
triangle_pattern(n)

# number_triangle_pattern
def number_triangle_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()

n = int(input("Enter the size of the number triangle: "))
number_triangle_pattern(n)
