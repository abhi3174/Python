s=input("Eneter a string-")
sub=input("Enter the a new substring-")

flag=False
c=-1
n=len(s)
while True:
    c=s.find(sub,c+1,n)
    if c==-1:
       break
    print("found at position-",c)
    flag=True    
if flag==False:
    print("not available")

