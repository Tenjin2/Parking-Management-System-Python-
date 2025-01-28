def max(list):
    maxx=list[0]
    second=list[1]
    if maxx<second:
        s=maxx
        maxx=second
        second=s
    for i in range(2,len(list)):
        if second<list[i]:
            second=list[i]
            if maxx<second:
                s=maxx
                maxx=second
                second=s
    print(second)
list=[21,21,23,4,12]
max(list)
