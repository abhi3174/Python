s=input("Enter a sentence")
i=0
for x in s:
    print("The element at +ve index {} and -ve index {} is {}.".format(i,i-len(s),x))
    i+=1