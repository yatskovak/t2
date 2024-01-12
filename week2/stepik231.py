# https://stepik.org/lesson/27995/step/1?unit=9194
# 2.31 Heron's formula 1 из 1 шага пройден 1 из 1 баллa  получен

# On the input, the program has integers, and the output should be a real number corresponding to the area of the triangle.

#a, b, c = 3, 4, 5   --->    s = 6
"""
import math

a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
s = math.sqrt( p*(p-a)*(p-b)*(p-c)  )
print(f'{s}')


"""
a, b, c = [int(input()) for i in range(3)]
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)
