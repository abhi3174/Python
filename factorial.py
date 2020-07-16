def facto(n):
    if n==0:
        r=1
    else :
        r=n*facto(n-1)
    return r
s=int(input("Enter the value for factorial-"))
d=facto(s)
print(d)