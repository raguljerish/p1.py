#raguljerish 
N,K=map (int,input ("enter N and K values:").split ( ))
x=[]
for i in range (N):
     y=int (input ("enter array elements"))
     x.append (y)
add=0
for s in range (K):
    add=x[s]+add
print (add)
