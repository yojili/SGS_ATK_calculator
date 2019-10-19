import consts as c
import random
import importlib
importlib.reload(c)

rawATK=[c.rawATK1,c.rawATK2,c.rawATK3,c.rawATK4,c.rawATK5]
skills=[c.skill2,c.skill3,c.skill4,c.skill5]
random.shuffle(skills)
n=random.randint(1,11)
if n<=6:
  del skills[2:4]
elif n>6 and n<=10:
  del skills[1:4]
else:
  del skills[0:4]
skills.append(c.skill1)

calcATK=[c.rawATK1,c.rawATK2,c.rawATK3,c.rawATK4,c.rawATK5]

for i in range(len(skills)):
  numStriker=[1,2,3,4,5]
  for j in range(skills[i][1]):
    num=numStriker.pop(random.randint(0,len(numStriker)-1))
    calcATK[num-1]+=skills[i][0]
