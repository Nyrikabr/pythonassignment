#sum of list
data=[2,4,1,47,38]
res=0
for i in range(0,5):
    res+=data[i]
print(res)

#finding the max element
data=[2,4,1,47,38]
for i in range(0,4):
    if(data[i]>data[i+1]):
        m=data[i]
print(m)  

#minimum
data=[2,4,1,47,38]
for i in range(0,4):
    if(data[i]<data[i+1]):
        m=data[i]
print(m)  
 

#average of num
data=[2,4,1,47,38]
res=0
for i in range(0,len(data)):
    res+=data[i]
avr=res/len(data)
print(avr)

#search
num=int(input("Enter the number to search\n"))
flag=0
data=[2,4,1,47,38]
for i in range(0,len(data)):
    if data[i]==num:
        flag=flag+1
        break
if flag==1:
     print("Element is found\n")
else:
     print("Element is not found\n")
 
#search other(assign)
num=int(input("Enter the number to search\n"))
flag=0
data=[2,4,1,47,38]
for i in range(0,len(data)):
    if data[i]==num:
        flag=1
        break
if(flag==1):
     print("Element is found\n")
else:
     print("Element is not found\n")