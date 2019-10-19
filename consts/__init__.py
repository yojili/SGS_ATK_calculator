import random
from consts.consts1 import *
from consts.consts2 import *
from consts.consts3 import *
from consts.consts4 import *
from consts.consts5 import *
from consts.consts_all import *
from consts.assist import *

numChosen1=random.randint(0,4)
abilityCrit1=listCrit1[numChosen1]
abilityCmb1=listCmb1[numChosen1]

numChosen2=random.randint(0,4)
abilityCrit2=listCrit2[numChosen2]
abilityCmb2=listCmb2[numChosen2]

numChosen3=random.randint(0,4)
abilityCrit3=listCrit3[numChosen3]
abilityCmb3=listCmb3[numChosen3]

numChosen4=random.randint(0,4)
abilityCrit4=listCrit4[numChosen4]
abilityCmb4=listCmb4[numChosen4]

numChosen5=random.randint(0,4)
abilityCrit5=listCrit5[numChosen5]
abilityCmb5=listCmb5[numChosen5]

assistATKs=[assistATK1,assistATK2,assistATK3,assistATK4,assistATK5]
random.shuffle(assistATKs)
assist1=assistATKs.pop()
assist2=assistATKs.pop()
