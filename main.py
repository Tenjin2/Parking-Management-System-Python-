import login
import parking
import checkout
import admin
k=login.login()
id=k[0]
if k[2]=="admin":
    n=1
else:
    n=0
if n==1:
    a=1
    while(a==1):
        print("Hello sir! What do you want to do?")
        print("1.add slot\n2.book slots\n3.view faculty details\n")
        y=int(input("enter your choice: "))
        admin.admin(y)
        a=int(input("do you want to continue?\n1.yes\n2.no\n"))
elif n==0:
    q=0
    f1=open("data.txt","r")
    file=f1.readlines()
    for i in file:
        j=i.split(" ")
        if j[0]==id:
            checkout.checkout(id)
            print("you have successfully checked out. Thank You!")
            q=1
    if q!=1:
        parking.parking(id)
            
