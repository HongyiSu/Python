# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:13:06 2018
MCMC_vs_GridSearch
@author: root
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

#calculate travel times between two points
def travel_time(x,y,xr,yr,Vp):
    t=1./Vp*((xr-x)**2+(yr-y)**2)**(0.5)
    return(t)

def travel_time3D(x,y,z,xr,yr,zr,Vp):
    t=1./Vp*((xr-x)**2+(yr-y)**2+(zr-z)**2)**(0.5)
    return(t)    


#Aster's parameter, MODIFIED
mt=np.array([10,10],dtype=float)     #get the actual epicenter from the global search method previously, this is 2D   
mt3D=np.array([10,10,10],dtype=float) #This is for 3D
dx=0.1
Vp=6
xr=np.array([1, 1,19,19, 1,19])
yr=np.array([1,19, 1,19,10,10])
#zr=np.array([0, 0, 0, 0, 0, 0])
sigma=0.1
#t_obs=np.array([3.12,3.26,2.98,3.12,2.84,2.98])
t_obs=np.zeros(len(xr),dtype=float)
for st_id in np.arange(len(xr)):
    t_obs[st_id]=travel_time(x=mt[0],y=mt[1],xr=xr[st_id],yr=yr[st_id],Vp=Vp) #travel time 2D
#        t_obs[st_id]=travel_time3D(x=mt3D[0],y=mt3D[1],z=mt3D[2]xr=xr[st_id],yr=yr[st_id],Vp=Vp, zr=zr[st_id]) #travel time 3D


xmin2=0
xmax2=20
ymin2=0
ymax2=20
    

###########################################################
#################### GRID SEARCH ##########################   
########################################################### 
xvec=np.arange(xmin2,xmax2,dx)
yvec=np.arange(ymin2,ymax2,dx)
nx=len(xvec)        
ny=len(yvec)
X,Y=np.meshgrid(xvec,yvec)
X2,Y2=X,Y #copy for plotting
ng=X.shape[0]*X.shape[1] #number of gridpoints (merge misfit into a vector for each station)
dA=dx**2 #area of each cell

X=np.reshape(X,ng) #reshape for the calculation below
Y=np.reshape(Y,ng)
t=np.zeros((len(xr),ng)) #initialize travel_time vector: #stations x #gridpoints
   
for st_id in np.arange(len(xr)):
    for idx in np.arange(ng):
        t[st_id,idx]=travel_time(x=X[idx],y=Y[idx],xr=xr[st_id],yr=yr[st_id],Vp=Vp) #travel-time calculation
        
Fmiss=np.zeros((ng,1)) #initialize misfit vector: #stations x #gridpoints
tmp_F=np.zeros((ng,1))
for st_id in np.arange(len(xr)):
    for idx in np.arange(ng):
        tmp_F[idx]=(1./(2*sigma**2)*(t[st_id,idx]-t_obs[st_id])**2) 
    Fmiss=Fmiss+tmp_F

FmissRS=np.reshape(Fmiss,([ny,nx])) #reshape missfit for plotting
  
#compute K
K_tmp=np.zeros((ng,1)) 
K=np.zeros((ng,1)) 
K_tmp=np.exp(-Fmiss)
for idx in np.arange(ng):
    K[idx]=dA*K_tmp[idx]
K=np.sum(K)
sig_max=max(1./K*np.exp(-Fmiss)) 
Prob=np.zeros([ng,1])        #probability
Prob=1./K*np.exp(-Fmiss)
ProbRS=np.reshape(Prob,([ny,nx])) #reshape probability for plotting



##########################################################
#################### PLOTTING GRID SEARCH ################
##########################################################
#plotting misfit
fig=plt.figure()
ax=plt.subplot(1, 1, 1)
plt.pcolor(X2, Y2, FmissRS, cmap='jet', vmin=Fmiss.min(), vmax=Fmiss.max())
plt.title('Misfit Function')
# set the limits of the plot to the limits of the data
plt.axis([X2.min(), min(X2.max(),Y2.max()), X2.min(), min(X2.max(),Y2.max())])
plt.colorbar()
for st_id in np.arange(len(xr)): #loop over stations
    plt.plot(xr[st_id],yr[st_id],"v",color='white',markersize=22)
    ax.annotate(str(st_id+1), xy=(xr[st_id] - 0.1,  yr[st_id] -0.1))

plt.show()
        

#plotting probability
fig=plt.figure()
ax=plt.subplot(1, 1, 1)
plt.pcolor(X2, Y2, ProbRS, cmap='jet', vmin=ProbRS.min(), vmax=ProbRS.max())
plt.title('Probability')
# set the limits of the plot to the limits of the data
plt.axis([X2.min(), min(X2.max(),Y2.max()), X2.min(), min(X2.max(),Y2.max())])
plt.colorbar()
for st_id in np.arange(len(xr)): #loop over stations
    plt.plot(xr[st_id],yr[st_id],"v",color='white',markersize=22)
    ax.annotate(str(st_id+1), xy=(xr[st_id] - 0.1,  yr[st_id] -0.1))  

plt.show()


