#raguljerish 
n=input ("Enter a number:")
a=0
for i in range (len (n)):
       a=a+int (n[i])**len (n)
if int (n)==a:
    print ("yes")
else:
    print ("no")
