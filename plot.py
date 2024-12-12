#from mpl import *
import numpy as np
import matplotlib.pyplot as plt


#Loading the solution files
euler = np.loadtxt("euler.txt")
rk2   = np.loadtxt("rk2.txt")
#rk3   = np.loadtxt("rk3.txt")
rk4   = np.loadtxt("rk4.txt")
exact   = np.loadtxt("exact.txt")
#----------------------------------------------

fig = plt.figure()
#plt.plot(euler[:,0],euler[:,1],label='Euler', c='g')
plt.plot(rk2[:,0],rk2[:,1],label='RK-2', c='r')
#plt.plot(rk3[:,0],rk3[:,1],'m',fillstyle='none',label='RK-3')
plt.plot(rk4[:,0],rk4[:,1],'c',fillstyle='none',label='RK-4')
plt.plot(rk4[:,0],rk4[:,1],'k',fillstyle='none',label='Exact')
plt.xlabel('t')
plt.ylabel('y')
#sfig.legend(loc=15)
plt.legend();
#plt.legend(bbox_to_anchor=(1,0), loc="lower right")
#plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
               # mode="expand", borderaxespad=0, ncol=2)
                
plt.grid(True, linestyle = '--')
#plt.axis('equal')
#plt.yticks(fontsize=12)
plt.savefig('u.pdf')

