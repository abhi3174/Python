s=input("Enter a string:-")
d={}
for x in s:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"----",v)
for k,v in sorted(d.items()):
    print(k,"----",v)