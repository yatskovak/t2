#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print (" == ФЫВА  QQQ ==i ---1" )
print (" commit 3 " )
print (" commit a1 ==1  " )

def is_anagram(a,b):
    c =  a[::-1]
    print(f"\n\n==========  a={a}         b={b} =========== {c == b }")
    #print(  c == b )
    return c == b


a = "qaz"
b = "zaq"
assert is_anagram(a,b) is True
#is_anagram(a,b)
print("====="*12)
a = "aaa"
b = "zaq"
#is_anagram(a,b)
assert is_anagram(a,b) is False

