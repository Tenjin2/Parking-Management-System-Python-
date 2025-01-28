#parking allotment system
#user interface
def login():
    print("Welcome to Parking Allotment System")
    print("please login ")
    print("1.sign up/n2.login")
    n=int(input("enter choice"))
    if (n==1):
        username=input("eenter your name : ")
        passw=int(input("give a strong password: "))
        print("now you need to login")
    if (n==1 || n==2):
        name=input("enter your entered name: ")
        password=int(input("enter password: "))
    else:
        print("invalid choice")
    return name,password

#allotment of parking
def allot(name):
    print("hii ",name,", please provide us your general details.")
    
























