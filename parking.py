#parking allotment
def parking(id):
    import time
    f1=open("login.txt","r")
    file=f1.readlines()
    for i in file:
        j=i.split(" ")
        if id==j[0]:
            vehicle=int(j[3])
            break
    f1.close()
    print("Finding free slot for your vehicle.")
    f1=open("parking.txt","r")
    file=f1.readlines()
    f1.close()
#truck
    if vehicle==3:
        e=file[4]
        f=e.split(" ")
        if int(f[1])==1:
            print("The truck slot is occupied! wait for some time.")
            f1=open("parking.txt","a")
            for i in file:
                f1.write(i)
        else:
            print("slot is empty at block",f[0],"you can park your truck there. Thank You")
            curr=time.time()
            entry=time.ctime()
            f1=open("parking.txt","w")
            for i in range(len(file)-1):
                f1.write(file[i])
            s=f[0]+" "+str(1)
            f1.write(s)
            f1.close()
            f1=open("data.txt","a")
            y=str(id)+" "+"E1"+"\n"
            f1.write(y)
            f1.close()
            f1=open("log.txt","a")
            x="id no.->"+str(id)+" parked "+"truck "+"on E1 at ["+str(entry)+"]"+"\n"
            f1.write(x)
            f1.close()
#4 wheeler
    elif vehicle==1:
        q=0
        for i in range(len(file)-2):
            j=file[i].split(" ")
            for k in range(1,len(j)):
                if int(j[k])==0:
                    print("slot is empty at block "+j[0]+str(k)+" you can park there. Thank You")
                    curr=time.time()
                    entry=time.ctime()
                    m=i
                    n=k
                    q=1
                    f1=open("data.txt","a")
                    y=str(id)+" "+j[0]+str(k)+"\n"
                    f1.write(y)
                    f1.close()
                    f1=open("log.txt","a")
                    x="id no.->"+str(id)+" parked "+"4 wheeler "+"on "+j[0]+str(k)+" at ["+str(entry)+"]"+"\n"
                    f1.write(x)
                    f1.close()
                    break
            if q==1:
                break
        if q==0:
            print("no free slots.")
            f1=open("parking.txt","w")
            for l in file:
                f1.write(l)
            f1.close()
        elif q==1:
            f1=open("parking.txt","w")
            i=file[m]
            j=i.split(" ")
            if n==len(j)-1:
                j[n]='1\n'
            else:
                j[n]='1'
            l=j[0]
            for k in range(1,len(j)):
                l=l+" "+j[k]
            file[m]=l
            for s in file:
                f1.write(s)
#2 wheeler
    elif vehicle==2:
        q=0
        i=file[3]
        j=i.split(" ")
        for k in range(1,len(j)):
            if int(j[k])==0:
                print("slot is empty at block "+j[0]+str(k)+" you can park there. Thank You")
                curr=time.time()
                entry=time.ctime()
                f1=open("data.txt","a")
                y=str(id)+" "+j[0]+str(k)+"\n"
                f1.write(y)
                f1.close()
                f1=open("log.txt","a")
                x="id no.->"+str(id)+" parked "+"2 wheeler "+"on "+j[0]+str(k)+" at ["+str(entry)+"]"+"\n"
                f1.write(x)
                f1.close()
                n=k
                q=1
                break
        if q==0:
            print("no free slots.")
            f1=open("parking.txt","w")
            for l in file:
                f1.write(l)
            f1.close()
        else:
            f1=open("parking.txt","w")
            i=file[3]
            j=i.split(" ")
            if n==len(j)-1:
                j[n]='1\n'
            else:
                j[n]='1'
            l=j[0]
            for k in range(1,len(j)):
                l=l+" "+j[k]
            file[3]=l
            for s in file:
                f1.write(s)















