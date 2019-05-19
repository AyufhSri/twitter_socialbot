f = open("tweets.txt", "r")
g = open("tweets_modified.txt", "w+")
h = open("tweets_description.txt", "w+")
f1 = f.readlines()
s1 = ""
s2 = ""
for x in f1:
    i = 0
    for j in range(0, 12):
        i = x.find(",", i+1)
    s1 = x[1:i+1]
    c = x[i+3]
    j = x.find(c, i+1)
    j = x.find(c+",", j+1)
    j = j+1
    s2 = x[i+2:j]
    s1 += x[j+1: -2]
    g.write(s1+"\r")
    h.write(s2+'\r')

f.close()
g.close()
h.close()
