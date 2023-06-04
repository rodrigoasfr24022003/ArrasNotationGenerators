import random
s=random.SystemRandom()
f=open('fraggenresults.txt','w')
mode="simple"
maxFragNumber=36
minFragNumber=1
minLayers=1
maxLayers=36
if mode=="simple":
    l=[]
    for i in range(s.randint(minLayers,maxLayers+1)):
        l.append(s.randint(minFragNumber,maxFragNumber+1))
    f.write(str(l))
    f.write('\n')
    f.close()