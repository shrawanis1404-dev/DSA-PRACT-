n=int(input("enter how many elements :"))
a=[]
for i in range(n):
    num=int(input("Enter your numbers:"))
    a.append(num)
print(a)
sr=int(input("Enter number to be searched:"))
found=False
for i in range(len(a)):
       if sr==a[i]:
           print(sr ,"is found at the",i,"position")
           found=True
           break
if not found:       
    print("not found")
        