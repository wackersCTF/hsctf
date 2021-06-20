#hsctf 2021 rev warmup chal
import math
def cold(t):
    return(t[17:]+t[0:17])

def cool(t):
    s = ""
    for i in range(len(t)):
        if(i %2==0):
            s+=chr(math.floor(ord(t[i])+3*(i/2)))
        else:
            s += t[i]
    return s

def warm(t):
    a = t[0,t.index("l")+1]
    t1 = t[(t.index("l")+1):]
    b = t1[0,t1.index("l")+1]
    c = t1[(t1.index("l")+1):]
    return (c+b+a)

def hot(t): # requires input of string with len 33
    adj = [-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13]
    for i in range(len(t)):
        s+=chr(ord(t[i])+adj[i])
    return s

match = "4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy"
flag = "testl"
r = hot(warm(cool(cold(flag))))
if (flag.length() == 33 and r == (match)):
    print("correct: "+ r)
else:
    print("incorrect: " + r)
