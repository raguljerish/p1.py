#raguljerish 
n,k=map (int,input ("Enter limit numbers:").split ())
while n<=k:
    for i in range (2,n):
        if n%i==0:
          break       
    else :
        print (n)
    n+=1
