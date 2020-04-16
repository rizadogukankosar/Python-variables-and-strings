# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:45:52 2020

@author: doguk
"""  

str1 =  "hello world"
str2 =  "HeLlO wOrLd"

print(str1[1]) #e

print(str1[1:5]) #ello

print(str1[:5]) #hello

print(str1[2:]) #lo world

print(len(str1)) #11 -> lenght of str1

print(str1.upper()) # HELLO WORLD

print(str2.lower()) # hello world

print(str1.replace("l", "k")) #hekko workd  l -> k

print(str1.split(" ")) #['hello' , 'world']

print(str1.split(" ")[0]) # hello

name = input("please, write your name") #take a value from user