n=int(input("enter how many elements :"))
a=[]
for i in range(n):
    num=int(input("Enter your numbers:"))
    a.append(num)
print("original array is:",a)
temp=[]
for num in a:
    if num not in temp:
        temp.append(num)
print("array after removing duplicates is ",temp)