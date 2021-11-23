a = "Ashwin"

b = []
count=0
for i in a:
    b.append(i)
for j in range(0,len(b)-1):
    for k in range(j+1,len(b)-1):
        if(b[j]==b[k]):
            count = count+1
            print ("Duplicate Letter is ",b[j])
            
#Duplicate letters
print(b)
print(count)
