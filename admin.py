def admin(y):
    if y==1:
        b=input("enter block in which you want to add slot: ")
        f1=open("parking.txt","r")
        file=f1.readlines()
        f1.close()
        f1=open("parking.txt","w")
        for i in file:
            j=i.split(" ")
            if b==j[0]:
                f1.write(j[0])
                for k in range(1,len(j)-1):
                    f1.write(' '+j[k])
                f1.write(' '+'0'+' '+'0\n')
            else:
                f1.write(i)
    elif y==2:
        b=int(input("enter how many slots you want to book: "))
        f1=open("parking.txt","r")
        file=f1.readlines()
        f1.close()
        f1=open("parking.txt","w")
        q=0
        for i in file:
            j=i.split(" ")
            f1.write(j[0])
            for k in range(1,len(j)):
                if q==b:
                    f1.write(' '+j[k])
                else:
                    if j[k]=='0':
                        j[k]='2'
                        f1.write(' '+j[k])
                        q+=1
                    else:
                        f1.write(' '+j[k])
        f1.close()
    elif y==3:
        f1=open("login.txt","r")
        file=f1.readlines()
        for i in file:
            j=i.split(" ")
            if j[2]=='faculty':
                print(j[0]+" "+j[1]+"->"+" "+"faculty")
            elif j[2]=='guest':
                print(j[0]+" "+j[1]+"->"+" "+"guest")
            elif j[2]=='admin':
                print(j[0]+" "+j[1]+"->"+" "+"admin")
        
                        
                    
            
