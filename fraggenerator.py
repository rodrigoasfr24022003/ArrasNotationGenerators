import random
import fractions
s=random.SystemRandom()
f=open('fraggenresults.txt','w')
for i in range(0,36000):
    mode="advanced"
    maxFragNumber=36
    minFragNumber=1
    minLayers=1
    maxLayers=36
    def genAmmo():
        return [s.choice(['bullet','drone','swarm_drone','bee','overdrive','revitalist','navyist','whirlybird','trap','block','boomerang','sikerblock','laserline','ionlaser','apbullet','shellingbullet','missile','empmissile','nuke','empnuke','railgunslug','heavynuke','heavyempnuke','donutbullet','kbbullet','oapp_heatseeker','oappblackhole','ceptioner','ceptionist','missile','bomb','stabilizer','pillbox','trapboxes','taurusportal','minion','sunchip','oxyprojectile','laserblast']),fractions.Fraction(s.randint(1,60),6),fractions.Fraction(s.randint(1,60),6)]
    def genEffect():
        return[s.choice(['none','slide '+str(s.randint(5,73))+' of the Tank Effect Sheet']),'Level: '+str(s.randint(1,12)),'Time: '+str(s.randint(1,3600))+' s']
    def genPattern():
        def ConcentricCircleGen():
            l=[]
            for i in range(1,s.randint(2,13)):
                if i<=4:
                    l.append(s.randint(1,36))
                elif 5<=i<=7:
                    l.append(s.randint(1,72))
                elif 8<=i<=10:
                    l.append(s.randint(1,108))
                elif 11<=i<=13:
                    l.append(s.randint(1,144))
            return l
        def TwoDimGen():
            l1=[]
            for i in range(1,s.randint(2,37)):
                l2=[]
                for j in range(1,s.randint(2,37)): 
                    l2.append(s.randint(0,1))
                l1.append(l2)
            return l1
        patterntype=s.choice(['none',s.choice(['rect'+str([s.randint(1,36),s.randint(1,36)]),'tri_'+s.choice(['l','f','r','b'])+str([s.randint(1,36),s.randint(1,36)]),'concentric_circles'+str(ConcentricCircleGen()),'line'+str([s.randint(1,36)]),'chevron'+str([2*s.randint(1,36)+1]),'cross'+str([4*s.randint(1,36)+1]),'advsquarepattern'+str(TwoDimGen())])])
        return patterntype
    if mode=="simple":
        l=[]
        for i in range(s.randint(minLayers,maxLayers+1)):
            l.append(s.randint(minFragNumber,maxFragNumber+1))
        f.write(str(l))
        f.write('\n')
    elif mode=="advanced":
        l=[]
        for i in range(s.randint(minLayers,maxLayers+1)):
            l.append(['Calculated from Pattern',genAmmo(),genEffect(),genPattern()])
        f.write(str(l))
        f.write('\n')
    else:
        f.close()
        raise ValueError("Invalid mode.")
f.close()