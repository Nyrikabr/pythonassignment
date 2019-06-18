# -*- coding: utf-8 -*-
#simple interest
def si(p,t,r):
    res=(p*t*r)/100
    return res
p=int(input("Enter the p\n"))
t=int(input("Enter the t\n"))
r=int(input("Enter the r\n"))
res=si(p,t,r)
print(res)

#prime
num1=int(input("Enter Num1"))
num2=int(input("Enter Num2"))
for i in range(num1,num2+1):
    if i>1:
        for n in range(2,i):
            if(i%n)==0:
                break
        else:
            print(i)
    
#fseries
num=int(input("Enter the number"))
def fs(num):
    if num<=1:
        return num
    else:
        return (fs(num-1)+fs(num-2))
for i in range(num):
    print(fs(i))

#Electric
con=int(input("Enter the consumption\n"))
if con<=100:
    print("Rate per unit rupees is ",2*con)
elif con>100 and con<=200:
    print("Rate per unit rupees is ",3*con)
elif con>200 and con<=300:
    print("Rate per unit rupees is ",5*con)
else:
    print("Rate per unit rupees is ",6*con)

    