import numpy as np

with open('input.txt','r') as f:
    A = f.read()


B = A.split('\n')
res = np.zeros(12)


for L in B:
    letters = list(L[:])
    
    for i in range(12):
        if letters[i] =='1':
            res[i]+=1
        else:
            res[i] -= 1

r = res > 0    

gamma = ''
epsilon  = ''

for l in r:
    if l:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
    
        
def binaryToDecimal(binary):
    """
    THX geeks for geeks
    """
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


g = binaryToDecimal(int(gamma))
e = binaryToDecimal(int(epsilon))

print(g*e)

#%%
dezis = np.arange(11,-1,-1)

X = np.array(B, dtype = float)
for d in dezis:
    foo = np.average(np.round(X % 10.0**(d+1), -d))
   
    if foo >= 10.0**d/2:      
        X = X[np.round(X % 10.0**(d+1), -d) >=  10.0**d] 

    else:        
        X = X[np.round(X % 10.0**(d+1), -d) <  10.0**d]
        
    if len(X)==1:
        break
oxy_bin = int(X[0])


X = np.array(B, dtype = float)
for d in dezis:
    foo = np.average(np.round(X % 10.0**(d+1), -d))
   
    if foo < 10.0**d/2:      
        X = X[np.round(X % 10.0**(d+1), -d) >=  10.0**d] 

    else:        
        X = X[np.round(X % 10.0**(d+1), -d) <  10.0**d]
        
    if len(X)==1:
        break
co2_bin = int(X[0])

oxy = binaryToDecimal(oxy_bin)
co2 = binaryToDecimal(co2_bin)
print(oxy*co2)

