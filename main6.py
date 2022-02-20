import math
figure = input('The geometric figure (circle,triangle, rectangle) is : ')
figure = figure.lower()
if figure == 'circle':
    radius = int(input('The radius is : '))
    print('The area of the circle is : ', math.pi * radius**2)
elif figure == 'triangle':
    a = int(input('Side A is  : '))
    b = int(input('Side B is  : '))
    c = int(input('Side C is  : '))
    p = (a + b + c) / 2
    print('The area of the triangle is : ', (math.sqrt(p * (p - a) * (p - b) * (p - c))))
else:
    a = int(input('Side A is  : '))
    b = int(input('Side B is  : '))
    print('The area of the rectangle is : ', a * b)
