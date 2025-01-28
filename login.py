#parking allotment system
#user interface
def login():
    print("***Welcome to Parking Allotment System***")
    print("please login ")
    z=0
    while z==0:
        print("1.sign up\n2.login\n")
        n=int(input("enter choice"))
        if (n==1):
            id=input("enter your id: ")
            name=input("enter your name : ")
            faculty=input("faculty or guest: ")
            vehicle=input("enter your vehicle type: \n1. 4 wheeler\n2. 2 wheeler\n3. truck\n")
            passw=input("give a strong password: ")
            f1=open("login.txt",'a')
            s=id+" "+name+" "+faculty+" "+vehicle+" "+passw+'\n'
            f1.write(s)
            f1.close()
            print("now you need to login")
        if (n==1 or n==2):
            f1=open("login.txt","r")
            file=f1.readlines()
            name=input("enter your entered name: ")
            password=int(input("enter password: "))
            s=0
            for i in file:
                j=i.split(" ")
                if name == j[1]:
                    if password==int(j[4]):
                        k=j
                        s=1
                        break
            f1.close()
            if s==0:
                print("data not found you need to login first.")
                z=0
            elif s==1:
                print("Successfully logged in!")
                z=1
        else:
            print("invalid choice. Try Again!")
    return k
        
























