import random

l =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0]

pattern = ''

pattern_length = int(input("Please enter pattern length: "))

for i in range(0,pattern_length):
    pattern += str(l[random.randint(0,len(l)-1)])

print(pattern)
#Searching for the index of the string

x = input("Enter string to be searched: ")
x_length = len(x)
indexes = []
for i in range(0,len(pattern)):
    temp = pattern[i:i+(x_length)]
    if temp == x:
        indexes.append(i)

print(indexes)