# https://stepik.org/lesson/27995/step/1?unit=9194
# 2.23 Floor-space of the room

def s_triangle(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    #import math
    #s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

def s_rectangle(a,b):
    return a * b

def s_circle(r):
    return  3.14 * r**2

figure= input()

#a, b, c = 3, 4, 5
if figure == "triangle":
    a, b, c = [int(input()) for i in range(3)]
    s1 = s_triangle(a, b, c)
elif figure == "circle":
    r = int(input())
    s1 = s_circle(r)
elif figure == "rectangle":
    a, b = [int(input()) for i in range(2)]
    s1 = s_rectangle(a,b)

print(f'{s1}')
# !!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""


Floor-space of the room

Residents of the Malevia country often experiment with the plan of their rooms. Rooms can be triangular, rectangular and round. To quickly calculate the floorage it is required to write a program, which gets the type of the room shape and the relevant parameters as input - the program should output the area of the resulting room.

The value of 3.14 is used instead of the number π in Malevia.

Input format used by the Malevians:

triangle
a
b
c

where a, b and c — lengths of the triangle sides.

rectangle
a
b

where a and b —lengths of the rectangle sides.

circle
r

where r — circle radius.

Sample Input 1:

rectangle
4
10

Sample Output 1:

40.0

Sample Input 2:

circle
5

Sample Output 2:

78.5

Sample Input 3:

triangle
3
4
5

Sample Output 3:

6.0

Напишите программу. Тестируется через stdin → stdout


"""