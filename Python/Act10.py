from random import randint
import random
import math
import string
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True
def vowel_count_test(string):
    count=0
    for z in string:
        if z in ['a','e','i','o','u']:
            count=count+1
    return count
def sort_by_vowel_count(words):
    return words.sort(key=vowel_count_test,reverse=True)

studentNr = input("What is your Student Number? ")
print ("")
type(studentNr)
studNr = [int(i) for i in str(studentNr)]
print ("0. The Student number is " + studentNr)
print (" ")
studentNrLen = len(studNr)

primeNumbers = 0

for i in range (0, studentNrLen):
    
    if (isprime(studNr[i])):
        primeNumbers += 1
 
if primeNumbers == 0:
    primeNumbers += 1
    print ("There was no prime numbers so to make sure we can divide the random number with the prime numbers we made the 0 a 1")
    print ("1. The number of prime numbers in this student number is: ", primeNumbers)
else:
    print ("1. The number of prime numbers in this student number is: ", primeNumbers)
print ("")

q = randint(25,50)
print ("2. The Random number is: ", q)
print (" ")


r = math.floor(q / primeNumbers)

print ("3. The number of strings to be generated is: ", r)
print (" ")

print ("4. List of Strings: ")
print ("******************")


arrayOfStrings = []
boolTest = True
for i in range(0,r):
    if boolTest:
        arrayOfStrings.append(''.join(random.choices(string.ascii_lowercase, k=5)))
        boolTest = False
    else:
        arrayOfStrings.append(''.join(random.choices(string.ascii_lowercase, k=7)))
        boolTest = True

for i in range(0, r):
    print (i, " - ",arrayOfStrings[i])

print ("***************")    

print ("")
print ("5. Sorted List:")
print ("***************") 

#sorted(arrayOfStrings, key=lambda word: sum(ch in 'aeiou' for ch in word),  reverse=False)
arrayOfStrings.sort(key = vowel_count_test, reverse = True)
for i in range(0, r):
    print (i, " - ", arrayOfStrings[i], "(Vowels:", vowel_count_test(arrayOfStrings[i]),")")
print ("***************") 










