#topper
ravi={'sub1':61,'sub2':87,'sub3':78,'sub4':56,'sub5':87,'sub6':90}
rashmi={'sub1':89,'sub2':98,'sub3':78,'sub4':56,'sub5':87,'sub6':45}
lokesh={'sub1':78,'sub2':75,'sub3':68,'sub4':84,'sub5':95,'sub6':93}

temp=0
temp1=0
temp2=0
for i in ravi.values():  
    temp=sum(ravi.values())
for i in rashmi.values():
    temp1=sum(rashmi.values())
for i in lokesh.values():
    temp2=sum(lokesh.values())
if(temp>temp1 and temp>temp2):
    print("Ravi is topper with score",temp)
elif(temp1>temp and temp1>temp2):
    print("Rashmi is topper with score",temp1)
#elif(temp2>temp and temp2>temp1):
else:
    print("lokesh is topper with score",temp2) 
    
#lowest marks
ravi={'sub1':61,'sub2':87,'sub3':78,'sub4':56,'sub5':87,'sub6':90}
rashmi={'sub1':89,'sub2':98,'sub3':78,'sub4':56,'sub5':87,'sub6':45}
lokesh={'sub1':78,'sub2':75,'sub3':68,'sub4':84,'sub5':95,'sub6':93}

temp=0
temp1=0
temp2=0
for i in ravi.values():
    temp=sum(ravi.values())
for i in rashmi.values():
    temp1=sum(rashmi.values())
for i in lokesh.values():
    temp2=sum(lokesh.values())
if(temp<temp1 and temp<temp2):
    print("Ravi scored less with score",temp)
elif(temp1<temp and temp1<temp2):
    print("Rashmi scored less with score",temp1)
#elif(temp2<temp and temp2<temp1):
else:
    print("lokesh scored less with score",temp2)
    

#find hieght score in each subject
 