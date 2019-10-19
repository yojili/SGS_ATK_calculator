import random
import consts as c
import calcATK
from math import floor
import importlib
importlib.reload(c)
importlib.reload(calcATK)

abilityCrit1=c.abilityCrit1
abilityCrit2=c.abilityCrit2
abilityCrit3=c.abilityCrit3
abilityCrit4=c.abilityCrit4
abilityCrit5=c.abilityCrit5
baffBonusCrit1=c.baffBonusCrit1
baffBonusCrit2=c.baffBonusCrit2
baffBonusCrit3=c.baffBonusCrit3
baffBonusCrit4=c.baffBonusCrit4
baffBonusCrit5=c.baffBonusCrit5
abilityCmb1=c.abilityCmb1
abilityCmb2=c.abilityCmb2
abilityCmb3=c.abilityCmb3
abilityCmb4=c.abilityCmb4
abilityCmb5=c.abilityCmb5
baffBonusCmb1=c.baffBonusCmb1
baffBonusCmb2=c.baffBonusCmb2
baffBonusCmb3=c.baffBonusCmb3
baffBonusCmb4=c.baffBonusCmb4
baffBonusCmb5=c.baffBonusCmb5
probInitCrit=c.probInitCrit
probInitCmb=c.probInitCmb
baffBonusCritAll=c.baffBonusCritAll
rankBonusCmb=c.rankBonusCmb
baffBonusCmbAll=c.baffBonusCmbAll
assist1=c.assist1
assist2=c.assist2
calcATK=calcATK.calcATK

totalDMG=0
crit=0

def logs(message):
  print(message)
  pass

def logic():
  global N
  global index
  global totalDMG
  global crit
  N+=1
  lotCrit=random.random()
  lotCmb=random.random()
  logs(str(index+1)+":"+str(listStriker[index%5]+1))
  if lotCrit<=probCrit[listStriker[index%5]]:
    logs('Critical Hit')
    crit+=1
    atkStriker[listStriker[index%5]]=calcATK[listStriker[index%5]]*1.5
    atkStriker[listStriker[index%5]]=floor(atkStriker[listStriker[index%5]])
  logs(atkStriker[listStriker[index%5]])
  totalDMG+=atkStriker[listStriker[index%5]]
  if listStriker[index%5]==0:
    lotCrit=random.random()
    if lotCrit<=0.1:
      logs('Critical Hit assist1')
      crit+=1
      totalDMG+=assist1*1.5
    else:
      totalDMG+=assist1
    lotCrit=random.random()
    if lotCrit<=0.1:
      logs('Critical Hit assist2')
      crit+=1
      totalDMG+=assist2*1.5
    else:
      totalDMG+=assist2
  
  if N==5:
    return
  if lotCmb<=probCmb[listStriker[index%5]]:
    logs('Combo')
    index+=1
    logic()


probCrit=[]
abilityCrit=(abilityCrit1,abilityCrit2,abilityCrit3,abilityCrit4,abilityCrit5)
baffBonusCrit=(baffBonusCrit1,baffBonusCrit2,baffBonusCrit3,baffBonusCrit4,baffBonusCrit5)
probCmb=[]
abilityCmb=(abilityCmb1,abilityCmb2,abilityCmb3,abilityCmb4,abilityCmb5)
baffBonusCmb=(baffBonusCmb1,baffBonusCmb2,baffBonusCmb3,baffBonusCmb4,baffBonusCmb5)

for numStriker in range(5):
  probCrit.append((probInitCrit+baffBonusCritAll+baffBonusCritAll+abilityCrit[numStriker]+baffBonusCrit[numStriker])/100)
  probCmb.append((probInitCmb+rankBonusCmb+baffBonusCmbAll+abilityCmb[numStriker]+baffBonusCmb[numStriker])/100)

listStriker=[0,1,2,3,4]
random.shuffle(listStriker)
index=0

for numLoop in range(10):
  atkStriker=[calcATK[0],calcATK[1],calcATK[2],calcATK[3],calcATK[4]]
  lotCrit=random.random()
  N=0
  logic()
  index+=1
