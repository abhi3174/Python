word=input("Enter any string-")
dicct={}
for x in word:
    dicct[x]=dicct.get(x,0)+1
print(dicct)
print(sorted(dicct))
for k,v in dicct.items():
    print(k,v)
