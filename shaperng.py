import random
s=random.SystemRandom()
xcmax=10
ycmax=10
pointsmax=12
def Generate2DPoint(FixedX=None, FixedY=None, xmax=xcmax, ymax=ycmax, xmin=-xcmax, ymin=-ycmax):
    t=()
    if FixedX!=None and FixedY!=None:
        t=(FixedX,FixedY)
    elif FixedX!=None and FixedY==None:
        t=(FixedX,s.randint(ymin,ymax))
    elif FixedX==None and FixedY!=None:
        t=(s.randint(xmin,xmax),FixedY)
    else:
        t=(s.randint(xmin,xmax),s.randint(ymin,ymax))
    return t
f=open('polygons.txt','w')
for i in range(1024):
    shape=[]
    sym=s.choices(['none','2wayx','2wayy','double2way'],weights=[0.1,0.3,0.3,0.3],k=1)[0]
    shape.append(sym)
    points=s.randint(3,pointsmax)
    if sym=='none':
        sp=[]
        for i in range(points):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='2wayy':
        sp=[]
        fixedn=s.randint(2,max(2,int(points/2)))
        for i1 in range(fixedn):
            sp.append(Generate2DPoint(0,None,0,ycmax,0,-ycmax))
        for i in range(points-fixedn):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,0,-ycmax))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='2wayx':
        sp=[]
        fixedn=s.randint(2,max(2,int(points/2)))
        for i1 in range(fixedn):
            sp.append(Generate2DPoint(None,0,xcmax,0,-ycmax,0))
        for i in range(points-fixedn):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,0))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='double2way':
        sp=[]
        fixednx=s.randint(1,max(2,int(points/3)))
        fixedny=s.randint(1,max(2,int(points/3)))
        sp.append((0,0))
        for i1 in range(fixednx-1):
            sp.append(Generate2DPoint(0,None,0,ycmax,0,-ycmax))
        for i1 in range(fixedny-1):
            sp.append(Generate2DPoint(None,0,xcmax,0,-xcmax,0))
        for i in range(points-fixednx-fixedny):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,0,0))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    f.write(str(shape))
    f.write('\n')
f.close()