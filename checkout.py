def checkout(id):
    import time
    f1=open("data.txt","r")
    file=f1.readlines()
    f1.close()
    f1=open("data.txt","w")
    for i in file:
        j=i.split(" ")
        if j[0]==id:
            x=j[1]
            f1.write("")
        else:
            f1.write(i)
    f1=open("parking.txt","r")
    file=f1.readlines()
    f1.close()
    f1=open("parking.txt","w")
    for i in file:
        j=i.split(" ")
        f1.write(j[0])
        for k in range(2,len(j)):
            if x==(j[0]+str(len(j)-1)):
                f1.write('0\n')
            elif x==(j[0]+'1'):
                f1.write(" "+'0')
            elif x==(j[0]+str(k)):
                print("hii")
                f1.write(" "+'0')           
            else:
                f1.write(" "+j[k])
            
        
        
            





















    
