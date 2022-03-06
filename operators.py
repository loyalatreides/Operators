from calendar import c
from re import M


print('1 is 1', 1 is 1)
print('1 is 2', 1 is 2)
print('a in Kamran', 'a' in 'Kamran')
print('b in Kamran', 'b' in 'Kamran')

#Exercise
age = int(25)
height = float(5.8)
c_variable = complex(1+1j)
print('Your age: ', age)
print('Your height: ', height)
print('Enter complex number: ', c_variable)

#Area of triangle
base = int(input('Enter base of the triangle: '))
height = int(input('Enter height of the triangle: '))
area_of_the_triangle = float(0.5) * base * height
print('Area of the triangle is: ', area_of_the_triangle)

#Perimeter of triangle
side_1= float(input('Enter side 1: '))
side_2= float(input('Enter side 2: '))
side_3= float(input('Enter side 3: '))
perimeter = side_1 + side_2 + side_3
print('Perimeter of the triangle is: ', perimeter)

#Area of the rectangle
length = float(input('Enter length of the Rectangle: '))
breadth = float(input('Enter breadth of the Rectangle: '))
area = length * breadth
print('Area of the Rectangle is: ', area)

#Area and perimeter of the circle
radius = float(input('Enter radius of the circle: '))
area = 3.14 * radius ** 2
print('The area of the circle is: ', area)
perimeter = 2 * 3.14 * radius
print('The perimeter of the circle is: ', perimeter)

#Slope Formula y=mx+c m=slope c intercept of y
print('y=2x-2')
slope = 2
intercept_of_y = -2
print('slope: ', slope)
print('intercept: ', intercept_of_y)
slope = 1
intercept_of_x = 1/2
print('slop: ', slope)
print('intercept: ', intercept_of_x)

point_x1 = float(input('Enter point x1: '))
point_x2 = float(input('Enter point x2: '))
point_y1 = float(input('Enter point y1: '))
point_y2 = float(input('Enter point y1: '))
slope = float((point_y2-point_y1)/(point_x2/point_x1))
print('Slope of {0},{1} and {2},{3} is: '.format(point_x1, point_x2, point_y1, point_y2), slope) #using of format

#False comparison statement
print(len('python') != len('jargon'))
print(len('John Cena') == len('Peacemaker'))
print(len('Hamdard') == len('Hogwart'))

#Use of and operator to find if 'on' is found
print('on in python and jargon','on' in 'python' and 'on' in 'jargon')

#Use of in operator
a = 'I hope this course is not full of jargon'
print('Is there jargan in a?', 'jargon' in a)

#Use of not in operator
print('on not in dragon and python: ', 'on' not in 'dragon' and 'on' not in 'python')

#Converting value of len of python into float and then into string
print(str(float(len('Python'))))

#checking even or odd using is operator
even_number = int(input('Enter any even number:'))
if even_number % 2 is 0:
    print('Input number is even')
else:
    print('The number you enter is odd')

#Some check examples
print(7/3 is 2.7)
print((10) is int(10))
print(9.8 is 10)

#To calculate the pay of the person
hours = int(input('Enter hours: '))
rate = int(input('Enter rate per week: '))
weekly = rate * hours
print('Your weekly earnings are:', weekly)

#Calculate number of seconds in your life
years = int(input('Enter number of years you have lived: '))
seconds = years * 364 * 24 * 60 * 60
print('You have lived for {} seconds'.format(seconds))

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
