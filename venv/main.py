from collections import Counter
import operator
import pandas
import math
import matplotlib.pyplot as plt
import functions

N=51
R=[]
A=358
M=5516
seed=1.0
seeed=seed
for i in range(N):
    seed=functions.get_rand(seed,A,M)
    R.append(seed/M)
    print('R'+str(i)+':'+str(seed)+ '   X'+str(i)+':'+str(seed/M))

functions.show_plt(R)
Mo=functions.M_colcuate(R)
print('----------------------------------------------------')
print('Ocenka Mx: '+str(Mo))
D=functions.D_colculate(R)
print('Ocenka Dx: '+str(D))
Sko=functions.sko_colculate(R)
print('Ocenka sko: '+str(Sko))
checker=functions.check_ravn(R)
print('2k/n = '+str(checker))
pp=functions.period(seeed,A,M)
