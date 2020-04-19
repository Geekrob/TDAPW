#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 
@author: cndaqiang 2019-

"""
import pyramids.io.qeresult as qeout
import pyramids.plot.setting as setfig
import pyramids.plot.PlotUtility as ppu
from pyramids.io.fdf import tdapOptions
from matplotlib import pyplot as plt
import numpy as np
import os


#check qe
runok=qeout.CheckQE()
plt.switch_backend('agg')
option=tdapOptions()
edt=option.tdTimeStep[0]   #fs
edt_au=option.edt[0] #a.u.
nstep=option.nstep
#         #
fig, axs = plt.subplots(2,2,sharex=True,sharey=False,figsize=(16,16))
#         
#TDAField
time,TDAFIELD=qeout.ReadTDFIELD('TDAFIELD')
xyz=["x","y","z"]
style=["-o","-v","*"]
for x in np.arange(3):
   axs[0,0].plot(time,TDAFIELD[:,x],style[x],label=xyz[x])


kargs=setfig.getPropertyFromPosition(ylabel=r'TDAFIELD(Ry/bohr/e)',
                                   xlabel='Time(fs)',
                                   title='(a) Vector potential',
                                   #hline=[0.0],
                                   xlimits=[0,None],
                                   ylimits=None#[0,0.12]#
                                            )             
setfig.setProperty(axs[0,0],**kargs)


#`fig` 画图展示
#         
#Energy
energy   =  qeout.GetEnergy() 
runFinalStep=energy.shape[0]
runtime  =  np.arange(0,runFinalStep,1)*edt
axs[0,1].plot(runtime,energy)
 

kargs=setfig.getPropertyFromPosition(ylabel=r'Eenergy(eV)',
                                   xlabel='Time(fs)',
                                   title='(b) Total energy',
                                   #hline=[0.0],
                                   xlimits=[0,None],
                                   ylimits=None#[0,0.12]#
                                            )             
setfig.setProperty(axs[0,1],**kargs)




#        
#Excitation
TotalStep,nkstot,npol,nbnd,wk,norm = qeout.Readnorm()
homo=qeout.GetHomo()
time=np.arange(TotalStep)*edt

#画哪些k点的激发
ksample=np.arange(nkstot)
Nksample=ksample.shape[0]
exciteelectron=np.zeros((TotalStep,Nksample))
hole=np.zeros((TotalStep,Nksample))    #if only "=", change hole will chenge exciteelectron

#目前程序还未只是SOC，所以npol=1，不用考虑太多
colors = setfig.getColors(Nksample)
for ik in ksample:
   exciteelectron[:,ik]=norm[:,ik,homo:nbnd].sum(axis=1) #*wk[ik] 
               #py index from 0, for ik ,so sum(axis=1 not 2)
               #homo:nbnd
   hole[:,ik]=(norm[0,ik,0:homo]-norm[:,ik,0:homo]).sum(axis=1) #*wk[ik]  #py index from 0
   axs[1,0].plot(time,exciteelectron[:,ik],label='Kpoint'+str(ksample[ik]),color=colors[ik])
   #axs[1].plot(time,hole[:,ik])

axs[1,0].legend()

kargs=setfig.getPropertyFromPosition(ylabel=r'Excitation',
                                   xlabel='Time(fs)',
                                   title='(c) Excitation at each kpoint',
                                   #hline=[0.0],
                                   xlimits=[0,None],
                                   ylimits=None #[0,1]#
                                            )             
setfig.setProperty(axs[1,0],**kargs)


#all excitation
wknorm=np.zeros(norm.shape)
for ik in np.arange(nkstot):
   wknorm[:,ik,:]=norm[:,ik,:]*wk[ik]
exciteelectron=wknorm[:,:,homo:nbnd].sum(axis=1).sum(axis=1)

wknorm=np.zeros((TotalStep,Nksample,nbnd))
for ik in np.arange(nkstot):
   wknorm[:,ik,:]=(1-norm[:,ik,:])*wk[ik]
hole=wknorm[:,:,0:homo].sum(axis=1).sum(axis=1)
axs[1,1].plot(time,exciteelectron)
#axs[1,1].plot(time,hole)

#fix fig
plt.tight_layout()

kargs=setfig.getPropertyFromPosition(ylabel=r'Excitation',
                                   xlabel='Time(fs)',
                                   title='(d) Total Excitation',
                                   #hline=[0.0],
                                   #xlimits=[0,None],
                                   ylimits=None #[0,1]#
                                            )             
setfig.setProperty(axs[1,1],**kargs)


SaveName='fig'+str(edt_au)+'_'+str(nstep)
for save_type in ['.png','.pdf']:
   filename = SaveName + save_type
   plt.savefig(filename,dpi=200)

   





#print(energy)
#
#axs[1].plot(energy)
#
#
#norm, kweight, nocc = qeout.readExcitationFile()
#excite = (norm - norm[0,:,:])
#for ib in range(excite.shape[2]):
#    excite[:,:,ib] *= kweight
#    #pass
#time = np.array(range(excite.shape[0]+1))
#step = min(time.shape[0]-1, excite.shape[0])
#axs[0].plot(time[1:step+1], (excite[:step,:,:nocc]).sum(axis=(1,2)))
#axs[0].plot(time[1:step+1], (excite[:step,:,nocc:]).sum(axis=(1,2)))