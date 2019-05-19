def followers_dict():
    followers={}
    k=0
    f=open("followers.txt","r")
    for i in f:
        a,b=i.split()
        a=a[1:-1]
        k+=1
        b=b[2:-2]
        l=list(b.split(","))
        followers[a]=l
    return followers