# Import time module
import numpy as np
import matplotlib.pyplot as plt
import pprint
import random
# it = 1
# runtimee = []
# iterations=[]
# while(it < 5):
    #print("it=",it)
def inputFnc(n):
    men = []
    for i in range(n):
        men.append(i)
        i = i + 1
    women = men.copy()
    for i in women:
        women[i] += n
    print("men=", men, "women=", women)
    # return  men,women
    menprefs = {}
    womenprefs = {}
    for item in men:
        random.shuffle(women)
        menprefs[item] = women.copy()
    for item in women:
        random.shuffle(men)
        womenprefs[item] = men.copy()
    menspreference = dict(menprefs.items())
    pref = []

    for value in dict(menprefs.items()).values():
        pref.append(value)
    for value in dict(womenprefs.items()).values():
        pref.append(value)

    return pref
def wPrefersM1OverM(prefer, w, m, m1):
        # Check if w prefers m over her
        # current engagement m1
        for i in range(num_of_mw):

            if (prefer[w][i] == m1):
                return True

            if (prefer[w][i] == m):
                return False

def stableMarriage(prefer):

            wPartner = [-1 for i in range(num_of_mw)]

            mFree = [False for i in range(num_of_mw)]

            freeCount = num_of_mw

            while (freeCount > 0):

                m = 0
                while (m < num_of_mw):
                    if (mFree[m] == False):
                        break
                    m += 1

                i = 0
                while i < num_of_mw and mFree[m] == False:
                    w = prefer[m][i]

                    if (wPartner[w - num_of_mw] == -1):
                        wPartner[w - num_of_mw] = m
                        mFree[m] = True
                        freeCount -= 1

                    else:

                        m1 = wPartner[w - num_of_mw]

                        if (wPrefersM1OverM(prefer, w, m, m1) == False):
                            wPartner[w - num_of_mw] = m
                            mFree[m] = True
                            mFree[m1] = False
                    i += 1

            print("Woman ", " Man")
            for i in range(num_of_mw):
                print(i + num_of_mw, "\t", wPartner[i])

num_of_mw = int(input("Enter your value: "))
pref = inputFnc(num_of_mw)
# print(f'\nPreferences')
#print(pref)
#for F :
print("Original pref=\n",pref)

it = 1
runtimee = []
iterations=[]
while(it < 5):
    print("it=",it)

    stableMarriage(pref)
    #stableMarriage(diffMan)
    import time

    start = time.time()

                    # define a sample code segment
    a = 0
    for i in range(1000):
        a += (i ** 100)

                    # record end time
        end = time.time()
        timee=(end - start) * 10 ** 3
                        # print the difference between start
                        # and end time in milli. secs
    print("The time of execution of above program is :",it,"-",
                              timee, "ms")
    runtimee.append([timee])
    print("rt",runtimee)
    iterations.append([it])
    print("itr", iterations)
    it = it+1
plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure."] = True
plt.savefig('fig.png',bbox_inches='tight')

x = np.array(runtimee)
y = np.array(iterations)

plt.title("Line graph")
plt.plot(x, y, color="red")
plt.show()
