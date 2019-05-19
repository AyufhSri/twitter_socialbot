def followings_dict():
    followings={}
    k=0
    f=open("followings.txt","r")
    for i in f:
        a,b=i.split()
        a=a[1:-1]
        k+=1
        b=b[2:-2]
        l=list(b.split(","))
        followings[a]=l
    return followings