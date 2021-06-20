#Author: wyl3_wak 6/16/2021 hsctf

import os

# setup
f = [4, 5]
for n in range(2, 1001):
    f.append(f[n-1] + f[n-2])

s = [4]
for n in range(1, 1001):
    sN = s[n-1] + f[n]
    if len(str(sN)) > 10:
        sN = int(str(sN)[-10:])
    s.append(sN)

sumOfsN = []
summ = 0
for i in s:
    summ = summ + i
    sumOfsN.append(summ)
print("done")

while True:
    #stream = os.popen('ls')
    #output = stream.readlines()
    #print(output)

    #testing code
    os.system('pwd')
    os.system('cd ~')
    os.system('ls -la')
'''
data = str(s.recv(1024))
    number = ""
    numbers = "023456789"
    if data != '':
        print(data)
    for i in data:
        if i in numbers:
            number = number + i
    if number != "":
        s.send(str(sumOfsN[int(number)]).encode())

'''
