#    -------   Hacker Rank Solutions --------


# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
n=int(input())
if n%2==1:
    print("Weird")
elif n%2==0 and n>=2 and n<=5:
	print("Not Weird")
elif n%2==0 and n>=6 and n<=20:
	print("Weird")
elif n%2==0 and n>20:
	print("Not Weird")

# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division, a//b .
# The second line should contain the result of float division, a/b.
# No rounding or formatting is necessary.
a=int(input())
b=int(input())
print(a//b)
print(a/b)

# The provided code stub reads and integer,n
# from STDIN. For all non-negative integers i<n , print i^2.
n=int(input())
if n>=1 and n<=20:
	for i in range(n):
		print(i*i)

# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.
txt = str(input())
x = txt.swapcase()
print(x)
# In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if s has any alphabetical characters. Otherwise, print False.
# In the third line, print True if s has any digits. Otherwise, print False.
# In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if s has any uppercase characters. Otherwise, print False.
s = input()
c1=0
for i in s:
	if(i.isalnum()):
		c1 = c1 + 1
		break
if(c1==1):
	print("True")
else:
	print("False")
c1=0
for i in s:
	if(i.isalpha()):
		c1 = c1 + 1
		break
if(c1==0):
	print("False")
else:
	print("True")
c1=0
for i in s:
	if(i.isdigit()):
		c1 = c1 + 1
		break
if(c1==0):
	print("False")
else:
	print("True")
c1=0
for i in s:
	if(i.islower()):
		c1 = c1 + 1
		break
if(c1==0):
	print("False")
else:
	print("True")
c1=0
for i in s:
	if(i.isupper()):
		c1 = c1 + 1
		break
if(c1==0):
	print("False")
else:
	print("True")





# N,M = map(int,input().split())
# c = ".|."
# for i in range(N//2):
# print((c*((i*2)+1)).center(M, '-'))
# print(('WELCOME'.center(M,'-')))
# for j in range(N//2):
# print((c*((N-(j*2))-2)).center(M, '-'))



# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
n = int(input()) #number of elements in set
s = set(map(int, input().split()))
com = int(input()) #number of commands (N)
d = {}
for i in range(com):
	l = list(map(str,input().split()))
	d[i] = l
for i in d:
	op = d[i] #i is iterartion of dictionary keys
	if(op[0]=='pop'):
		s.pop()

	elif(op[0]=='remove'):
		s.remove(int(op[1]))
	
	elif(op[0]=='discard'):
		s.discard(int(op[1]))
sum = 0
for i in s:
	sum = sum+i
print(sum)



# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.
t = int(input())
d = {}
for i in range(t):
	l =[]
	a = int(input())
	sa = set(map(int, input().split()))
	b = int(input())
	sb = set(map(int, input().split()))
	l.append(sa)
	l.append(sb)
	d[i] = l # dictionary with elements as list, and each list contains two sets
for i in d: #keys of dictionary
	sets = d[i] #value of dictionary
	A = sets[0] # literally set A
	B = sets[1] # literally set B
	count = 0
	for j in A:
		if(j in B):
			count = count +1
	if (count == len(A)):
		print('True')
	else:
		print('False')


# Given two strings, determine if they share a common substring. A substring may be as small as one character.
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# def twoStrings(s1, s2):
# 	s10= s1.lower()
# 	s20= s2.lower()
# 	for i in s10:
# 		if i in s20:
# 			return 'YES'
# 	else:
# 		return 'NO'
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(input().strip())
#     for q_itr in range(q):
#         s1 = input()
#         s2 = input()
#         result = twoStrings(s1, s2)
#         fptr.write(result + '\n')
#     fptr.close()

# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. 
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
# import sys
# d = sys.stdin.read().splitlines()
# d = [list(map(int,i.split())) for i in d]
# maxval = None
# for j in range(4):
#     for i in range(4):
#         add = d[j][i] + d[j][i+1] + d[j][i+2] + d[j+1][i+1] + d[j+2][i] + d[j+2][i+1] + d[j+2][i+2]
#         if maxval ==None:
#             maxval=add
#         elif add>maxval:
#             maxval=add
# print(maxval)


# for i in range(int(input())):
#     try:
#         a, b = map(int, input().split())
#         print(a//b)
#     except Exception as e:
#         print("Error Code:",e)

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# def maxMin(k, arr):
#     arr = sorted(arr)
#     i =-1
#     j=k-2
#     m=arr[-1]
#     while(j< len(arr)-1):
#     	i=+1
#     	j=+1
#     	max_arr=arr[j]
#     	min_arr=arr[i]
#     	m=min(m,max_arr-min_arr)
#     return m

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     k = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr_item = int(input().strip())
#         arr.append(arr_item)

#     result = maxMin(k, arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
