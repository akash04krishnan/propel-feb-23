'''
#Assignment4
#Write a procedure that solves quadratic equations using the quadratic formula:
# It should take as arguments three numbers a, b, and c.
# It should print error messages if a is zero, or if the roots are complex.
# Otherwise it should print the two roots.
# import complex math module

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=b**2-4*a*c
l1=(-b - d**(1/2))/(2*a)
l2=(-b + d**(1/2))/(2*a)
print(l1,"and",l2)
'''
'''
#2Write a program that reads in a string on the command line and returns a table of the frequency of occurrence
# of each word. Ignore the case. A sample run of the program would look this
#Enter some letters >>> The cat in the hat 
#The - 2
#Cat - 1
#In - 1
#Hat - 1
#This should involve writing a function that takes in a string and returns a dictionary with these letters
# and counts.
def occurrence(x1):
    comLine.lower()
    x = comLine.split(' ')
   # print(comLine)
    #print(x)
    s=[]
    for i in x:
        if i not in s:
            s.append(i)
    for i in range(0,len(s)):
        z = x.count(s[i])
        print(s[i], z)

comLine = str(input('enter a command line'))
occurrence(comLine)
'''
'''
#3Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3
a=input("enter the string")
import re
letters=re.findall(r'[a-zA-Z]',a)
digit=re.findall(r'[0-9]',a)
print("total digit is",len(digit))
print("total alphabet is",len(letters))
'''
'''
#4Write a Python program to check the validity of a password input by the user.
# The password should satisfy the following conditions:

#a.	It should have at least 1 letter [a to z]
#b.	It should have at least 1 number [0 to 9]
#c.	It should have at least 1 capital letter [A to Z]
#d.	It should have at least one special character [$, #, @]
#e.	Minimum length = 6 characters
#f.	Maximum length = 12 characters
import re
a=input("enter the password : ")
flag=True
while True:
    if len(a)<6:
        break
    elif len(a)>12:
        break
    elif not re.search('[a-z]',a):
        break
    elif not re.search('[A-Z]',a):
        break
    elif not re.search('[0-9]',a):
        break
    elif not re.search('[@#$]',a):
        break
    else:
        print("valid password")
        flag=False
        break
if flag:
    print("invalid password!")
'''
'''
#5Write a Python program that takes a string of words separated by spaces, together with a ”target” word,
# and shows the position of the target word in the string of words.
#For example, if the string is: ‘we dont need no education we dont need no thought control no we dont’
#and the target word is ”dont”, then your program should return the list 1, 6, 13
#because ”dont” appears at the 1st, 6th, and 13th position in the string. Your program should
#return False if the target word doesn’t appear in the string.
def target(sentence):
    x=sentence.split(' ')
    flag=False
    print(x)
    a=[]
    find= str(input('enter a target word '))
    for i in range(len(x)):
        if x[i]==find:
            a.append(i)
            flag=True
        else:
           flag=False
    if flag:
        print('target',a)
    else:
        print('target is false')
sentence=str(input('enter a sentence'))
target(sentence)
'''
