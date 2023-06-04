import random
import fractions
s=random.SystemRandom()
f=open('fraggenresults.txt','w')
mode="advanced"
maxFragNumber=36
minFragNumber=1
minLayers=1
maxLayers=36
def genAmmo():
    return [s.choice(['bullet','drone','swarm_drone','bee','overdrive','revitalist','navyist','whirlybird','trap','block','boomerang','sikerblock','laserline','ionlaser','apbullet','shellingbullet','missile','empmissile','nuke','empnuke','railgunslug','heavynuke','heavyempnuke','donutbullet','kbbullet','oapp_heatseeker','oappblackhole','ceptioner','ceptionist','missile','bomb','stabilizer','pillbox','trapboxes','taurusportal','minion','sunchip','oxyprojectile','laserblast']),fractions.Fraction(s.randint(1,60),6),fractions.Fraction(s.randint(1,60),6)]
def genEffect():
    return[s.choice('none','slide '+str(s.randint(5,73))+' of the Tank Effect Sheet'),'Level: '+str(s.randint(1,12)),'Time: '+str(s.randint(1,3600))+' s']
if mode=="simple":
    l=[]
    for i in range(s.randint(minLayers,maxLayers+1)):
        l.append(s.randint(minFragNumber,maxFragNumber+1))
    f.write(str(l))
    f.write('\n')
    f.close()
elif mode=="advanced":
    l=[]
    for i in range(s.randint(minLayers,maxLayers+1)):
        l.append([s.randint(minFragNumber,maxFragNumber+1),genAmmo(),genEffect()])
    f.write(str(l))
    f.write('\n')
    f.close()
else:
    raise ValueError("Invalid mode.")