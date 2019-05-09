from random import randint

# Imports 
import random
import math
import string

#Define all functions to be used
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not 1 & n: 
        return False
    for p in range(3, int(n**0.5) + 1, 2):
        if n % p == 0:
            return False
    return True

def vowel_count(string):
    count = 0
    for x in string:
        if x in ['a','e','i','o','u']:
            count=count+1
    return count

def sort_by_vowel_count(word):
    return word.sort(key=vowel_count,reverse=True)



studentNumber = input("Student Number: ")
print ("")
type(studentNumber)
sNumber = [int(i) for i in str(studentNumber)]
print ("Accepted the student number: " + studentNumber)
print ("")
sNumLen = len(sNumber)

print ()
p = 0

for i in range (0, sNumLen):
    
    if (isprime(sNumber[i])):
        p += 1
 
if p == 0:
    print ("Note: No Prime Numbers were found. Defaulting to 1 in order to allow division.")
    p += 1
    print ("1. The number of prime numbers in this student number is: ", p)
else:
    print ("1. The number of prime numbers in this student number is: ", p)
print (" ")

q = 30

print ("The Value of q before randomizing the number: ", q)
print (" ")
q = randint(24,51)
print ("2. The Random number now is: ", q)
print (" ")


r = math.floor(q / p)

print ("3. The number of strings to be generated is: ", r)
print (" ")

print ("4. List of Strings: ")
print ("-----------------")


arrWords = []
boolSwitch = True
for i in range(0,r):
    if boolSwitch:
        arrWords.append(''.join(random.choices(string.ascii_lowercase, k=5)))
        boolSwitch = False
    else:
        arrWords.append(''.join(random.choices(string.ascii_lowercase, k=7)))
        boolSwitch = True

for i in range(0, r):
    print (i, " - ",arrWords[i])

print ("-----------------")    

print ("")
print ("5. Sorted List:")
print ("-----------------") 


arrWords.sort(key = vowel_count, reverse = True)
for i in range(0, r):
    print (i, " - ", arrWords[i], "(Vowels:", vowel_count(arrWords[i]),")")
print ("-----------------") 










