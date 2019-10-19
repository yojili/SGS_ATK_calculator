# from statistics import mean,stdev
import numpy as np
import mainCalc as calc
import importlib
import time

startTime=time.time()

times=10000

mean=np.mean
max=np.max
min=np.min
stdev=np.std
sqrt=np.sqrt

DMG=[]
cntCrit=[]
cntCmb=[]

for i in range(times):
    importlib.reload(calc)
    DMG.append(calc.totalDMG)
    cntCrit.append(calc.crit)
    cntCmb.append(calc.index-10)

endTime=time.time()

print('トータルダメージ')
aveDMG=('平均値：{:.0f}'.format(mean(DMG)))
maxDMG=('最大値：{:.0f}'.format(max(DMG)))
minDMG=('最小値：{:.0f}'.format(min(DMG)))
stdevDMG=('標準誤差：{:.0f}'.format(stdev(DMG)/sqrt(times)))
print(aveDMG+'/'+maxDMG+'/'+minDMG+'/'+stdevDMG)

print('クリティカル回数')
aveCrit=('平均値：{:.0f}'.format(mean(cntCrit)))
maxCrit=('最大値：{:.0f}'.format(max(cntCrit)))
minCrit=('最小値：{:.0f}'.format(min(cntCrit)))
stdevCrit=('標準偏差：{:.0f}'.format(stdev(cntCrit)))
print(aveCrit+'/'+maxCrit+'/'+minCrit+'/'+stdevCrit)

print('コンボ回数')
aveCmb=('平均値：{:.0f}'.format(mean(cntCmb)))
maxCmb=('最大値：{:.0f}'.format(max(cntCmb)))
minCmb=('最小値：{:.0f}'.format(min(cntCmb)))
stdevCmb=('標準偏差：{:.0f}'.format(stdev(cntCmb)))
print(aveCmb+'/'+maxCmb+'/'+minCmb+'/'+stdevCmb)
print('実行時間：{:.3f}'.format(endTime-startTime)+'/試行回数：'+str(times))