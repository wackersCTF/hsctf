#Author: prince_of_tennis 6/16/2021 hsctf
import subprocess
import os

def Fib(n, computed = {0: 4, 1: 5}):
    if n not in computed:
        computed[n] = Fib(n-1, computed) + Fib(n-2, computed)
    return computed[n]

def seq(n):
    if(n==0): 
        return 4
    else:
        x= int(seq(n-1)+Fib(n))
        if(len(str(x))>=10):
            x = int(str(x)[-10:])
        return(x)
# driver code
n=0


stream = os.popen('nc extended-fibonacci-sequence-2.hsc.tf 1337')
output = stream.readlines()
print(output)


'''
print(subprocess_return)
summ = 0
for i in range(n+1):
    x= seq(i)
    summ+=x

print(str(summ)[-10:].lstrip("0"))
'''
