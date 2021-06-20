# nc not-really-math.hsc.tf 1337
# since addition comes b4 multiplication, i split the characters by multiplication
# 1. split the problem by multplication 
# 2. calculate the addition part and replace it
# 3. calculate the product
# 4. take the mod of it
# addition part looks like 6a8 or 3a5a5a4

def multiplyList(myList): #copied and pasted from stack overflow or somewhere cuz too lazy lol
    result = 1
    for x in myList:
         result = result * x
    return result

problem = input() # get the thingy that needs to be calculated
problem = problem.split("m") # split the problem by multiplication
print(problem) # you get each part in a separate item (addition parts are all separated)
for i in problem: 
	if "a" in i: 
		j = i.split("a") # split the numbers in the addition part
		print(j)
		for k in range(len(j)): # this just converts each item in the list j from string to integer
			j[k] = int(j[k])
		summ = sum(j) #sum() is a built in python thing that calculates the sum of a list
		problem[problem.index(i)] = str(summ) # this replaces the addition part with the sum

print("no more addition parts: " + str(problem)) # now all the addition parts are replaced with sums
for k in range(len(problem)): # again, converts each item from string to integer
	problem[k] = int(problem[k]) 

product = multiplyList(problem) # multiplies all the values in the list
print(product)
if product > 2**32 - 2: # takes the mod if its over 2**32 -1
	product = product % (2**32 - 1)
print(product)
