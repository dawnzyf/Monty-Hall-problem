# Created by Dawn
import random
from random import randint
count=1
switch=0
stay=0
staywin=0
changewin=0
count1=1
while count1 in range(1,10001):
    cdoor=randint(0,2)
    sdoor=randint(0,2)
    change=random.choice([True,False])
    if change==False:
        stay+=1
        if cdoor==sdoor:
            staywin+=1
    if change==True:
        switch+=1
        if cdoor!=sdoor:
            changewin+=1
    count1+=1
print('switch:{}'.format(switch))
print('switchwin:{},{:.2f}%'.format(changewin,changewin/switch*100))
print('stay:',stay)
print('staywin:{},{:.2f}%'.format(staywin,staywin/stay*100))

