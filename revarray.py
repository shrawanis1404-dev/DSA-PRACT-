n=int(input("enter how many elements :"))
a=[]
for i in range(n):
    num=int(input("Enter your numbers:"))
    a.append(num)
print("original array is:",a)
rev=[]
for i in range(len(a)-1,-1,-1):
    rev.append(a[i])
print("Array after reversing is:",rev)
