def lenght(str1):
    l = len(str1)
    print("Length of inputed string is : ", l)

def max_of_three_strings():
    n1 = input("Enter 1st string : ")
    n2 = input("Enter 2nd string : ")
    n3 = input("Enter 3rd string : ")
    print("The maximum of the three strings is =", max(n1,n2,n3)) 

def hash1(str1):
    str2 = ''
    for i in range(0, len(str1)):
        if str1[i] == ' ':
            str2 += ' '
        elif i % 2 == 0:
            str2 += str1[i]
        else:
            str2 += '#'
    print(str2)
def counter(str1):
    s = str1.split()
    l = len(s)
    print("number of words in the given string are : ", l)

print("""
a. Find the length of string
b. Return maximum of three strings
c. Accept a string and replace every successive character with ‘#’ 
d. Find number of words in the given string""")

str1 = str(input("Enter the string, (for maximum of three strings, separate strings needs to be added :) ):  "))
while True:
    x = input("Enter a choice :) : ")
    x = x.lower()
    if x =='a':
        lenght(str1)
    elif x == 'b':
        max_of_three_strings()
    elif x =='c':
        hash1(str1)
    elif x =='d':
        counter(str1) 
    elif x == 'stop':
        break     
    else:
        print("Try Again :)")
