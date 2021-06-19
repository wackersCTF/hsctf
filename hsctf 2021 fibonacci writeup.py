#Author: prince_of_tennis 6/15/2021 hsctf


# this was my original attempt at fib, too slow
'''
def Fib(n): # definitely works correctly
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return int(Fib(n-1)+Fib(n-2))
'''


# fibonacci but fast, essentually stores already computed fibonacci numbers in a list and checks if a new number is already in
# that list. That way, its much faster than having to compute everything. Literally stolen from stack overflow.
def Fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = Fib(n-1, computed) + Fib(n-2, computed)
    return computed[n]


# this is the sequence part. This got me stuck for a while because S0 was not defined but I forgot how sequences work. Basically S0
# is not defined because a sequence with 0 elements is just 0. 
def seq(n):
    if(n==0): 
        return 0
    else:
        x= int(str(seq(n-1))+str(Fib(n)))
        #^this is probably the weirdest part. It's concatenating the previous sequence term and the fib value as seen in the pdf.
        
        if(len(str(x))>=11):
            x = int(str(x)[-11:]) #since we only need the last 11 digits, to make things faster, I only saved 11 digits.
        return(x)
n = int(input("#"))

summ = 0
for i in range(n+1): # this is the summation part. The range is n+1 because python loops always go one less than the max value.
    x= seq(i)
    summ+=x
    print(i)

print(str(summ)[-11:].lstrip("0")) # takes away leading zeroes and any extra digits though that's probably unnecessary.  

