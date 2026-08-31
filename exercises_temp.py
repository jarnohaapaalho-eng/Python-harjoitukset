# This .py file is intended as temporary exercises done during the class or otherwise

#libraries
import math
import random

#variables
name = input("What is your name? ")
age = int(input("How old are you? "))
new_age = age + 10

number_1 = 3
number_2 = 4

height = float(input("how tall are you? "))
weight = float(input("how much do you weight? "))
bmi = weight / (height / 100) **2

# Output

print ("Hello, my name is " + name + " and in 10 years I'll be " + str(new_age) + " years old")

print (f"Your BMI is: {bmi:.2f}")

print ("Don't mind the maths below.")

#ez maths
print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2)

# how many times the number can go in to the other (i.e 3 goes twice to 6, but only once to 5)
print(number_1 // number_2)

# modulo / jakojäännös
print(number_1 % number_2)

# exponentials
print(number_1 ** number_2)
