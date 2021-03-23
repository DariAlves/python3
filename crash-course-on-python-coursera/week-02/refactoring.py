# code a - this function is not very readable
def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

# code b - We re-write code to be more self-documenting
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)
