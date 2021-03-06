from collections import Counter
import operator
import pandas
import math
import matplotlib.pyplot as plt
import functions
def get_rand(seed,A,M):
    seed=(A*seed)%M
    return seed
def show_plt(aa):
    aaa = Counter(aa)
    sorted_x = sorted(aaa.items(), key=operator.itemgetter(0))
    df = pandas.DataFrame.from_dict(dict(sorted_x), orient='index')
    df.plot(kind='bar')
    plt.show()

def M_colcuate(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
def D_colculate(Arr):
    M=M_colcuate(Arr)
    D=0
    for ar in Arr:
        D=D+((ar-M)*(ar-M))
    return D/len(Arr)
    # return d*(len(r)/(len(r)-1))
def sko_colculate(Arr):
    D=D_colculate(Arr)
    return math.sqrt(D)

def check_ravn(Arr):
    i=0
    counter=0
    while (i<len(Arr)-1):
        if (((Arr[i] ** 2)+(Arr[i+1]**2))<1):
            counter+=1
        i+=2
    return (counter*2)/len(Arr)

def period(seed,A,M):
    RR=[]
    for i in range(2000000):
        seed=get_rand(seed,A,M)
        RR.append(seed/M)
    Xv=RR[2000000-1]
    i1=-1
    i2=-1
    flag=False
    for i in range(len(RR)):
        if(RR[i]== Xv):
            if(flag==False):
                flag=True
                i1=i
                continue
            else:
                i2=i
                break
    per=i2-i1

    i3=0
    while(RR[i3]!=RR[i3+per]):
        i3+=1
    aper=i3+per
    print('Period: '+str(per))
    print('interval: '+str(aper))
