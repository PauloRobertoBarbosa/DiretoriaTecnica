# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"hi i'm {self.name}")
#
#
# paulo = Person("supimpa")
# paulo.talk()
#
# bob = Person ("Bob")
# bob.talk()
#
# tot = Person("Lauro")
# tot.talk()

#inheritance
# class Mammal:
#     def walk(self):
#         print("walk bixo")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("auf")
#     pass
#
#
# class Cat(Mammal):
#     def anno(self):
#         print("annoying")
#     pass
#
#
# dog1 = Dog()
# cat1 = Cat()
#
# dog1.walk()
# dog1.bark()
# cat1.walk()
# cat1.anno()

import os
# import pandas as pd
# from matplotlib import pyplot as plt
# dataset = pd.read_csv(r'C:\Users\paulo.roberto\Downloads\kc_house_data.csv', sep=',')
# dataset['size'] = dataset['bedrooms']*20
# def categoriza(s):
#     if s >= 80:
#         return 'Big'
#     elif s>= 60:
#         return 'Medium'
#     elif s >= 40:
#         return 'Small'
#
# dataset['cat_size'] = dataset['size'].apply(categoriza)
# dataset.fillna(0, inplace=True)
# print(dataset['bedrooms'].std())

import pandas as pd
import numpy as np
import openpyxl as xl
import os

os.chdir(r'C:\Users\paulo.roberto\Documents')
file = open(r"C:\Users\paulo.roberto\Documents\Realizado 2019 VP tecnica.txt",'r', encoding='ANSI', errors='surrogateescape')
count = 0
for i in file:
    count += 1

print(count)

