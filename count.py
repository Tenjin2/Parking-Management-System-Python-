f1=open("parking.txt","r")
file=f1.readlines()
count_guest=0
count_faculty=0
count_vacant=0
for i in file:
    j=i.split(" ")
    for k in range(1,len(j)):
        if int(j[k])==2:
            count_guest+=1
        elif int(j[k])==1:
            count_faculty+=1
        else:
            count_vacant+=1
f1.close()
dict
print("guests: ",count_guest)
print("faculty: ",count_faculty)
print("vacant space: ",count_vacant)
