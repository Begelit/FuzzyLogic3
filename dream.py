import numpy as np
from matplotlib import pyplot as plt
import os
import os.path
import pandas as pd

def straight1(x,a,b):
	return (x - a)/(b-a)
def straight2(x):
	return 1+x*0
def straight3(x,a,b):
	return (b - x)/(b-a)

"""
def gausFunc(x,):
	return (1/np.sqrt(2*np.pi))*np.exp((-1/2)*(((x-2)/0.5)**2)) 
"""
####################
####################
####################

def createPlotLux():
	fig,ax = plt.subplots()
	# M
	ax.plot(np.linspace(0,3),straight3(np.linspace(0,3),0,3),'b')
	# S
	ax.plot(np.linspace(1,5),straight1(np.linspace(1,5),1,5),'g')
	ax.plot(np.linspace(5,10),straight3(np.linspace(5,10),5,10),'g')
	# D1
	ax.plot(np.linspace(7,12),straight1(np.linspace(7,12),7,12),'y')
	ax.plot(np.linspace(12,15),straight2(np.linspace(12,15)),'y')
	ax.plot(np.linspace(15,20),straight3(np.linspace(15,20),15,20),'y')
	# D2
	ax.plot(np.linspace(15,20),straight1(np.linspace(15,20),15,20),'r')
	ax.plot(np.linspace(20,40),straight2(np.linspace(20,40)),'r')
	
	ax.minorticks_on()

	ax.grid(which='major',color = 'k',linewidth = 1)
	ax.grid(which='minor', color = 'k', linestyle = ':')
	
	plt.xlabel('LUX', fontsize=14, fontweight='bold')
	plt.annotate('M',xy = (0,1),xycoords = 'data',xytext=(0,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'blue' )
	plt.annotate('S',xy = (5,1),xycoords = 'data',xytext=(5,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'green' )
	plt.annotate('D1',xy = (12,1),xycoords = 'data',xytext=(12,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'yellow')
	plt.annotate('D2',xy = (20,1),xycoords = 'data',xytext=(20,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'red' )
	
	if os.path.exists('/home/koza/idz3/Plots/Lux.png') == True:
		os.remove('/home/koza/idz3/Plots/Lux.png')
	plt.savefig('/home/koza/idz3/Plots/Lux.png')

#	plt.show()
	
#createPlotLux()

def createPlotBrnAct():
	fig,ax = plt.subplots()
	# M
	ax.plot(np.linspace(0,4),straight2(np.linspace(0,4)),'b')
	ax.plot(np.linspace(4,6),straight3(np.linspace(4,6),4,6),'b')
	# S
	ax.plot(np.linspace(5,9),straight1(np.linspace(5,9),5,9),'g')
	ax.plot(np.linspace(9,14),straight2(np.linspace(9,14)),'g')
	ax.plot(np.linspace(14,16),straight3(np.linspace(14,16),14,16),'g')
	# D
	ax.plot(np.linspace(13,15),straight1(np.linspace(13,14),13,14),'r')
	ax.plot(np.linspace(15,20),straight2(np.linspace(15,20)),'r')
	
	ax.minorticks_on()

	ax.grid(which='major',color = 'k',linewidth = 1)
	ax.grid(which='minor', color = 'k', linestyle = ':')
	
	plt.xlabel('BRAIN AND PHYSICAL ACTIVITY(hours)', fontsize=14, fontweight='bold')
	plt.annotate('M',xy = (4,1),xycoords = 'data',xytext=(4,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'blue')
	plt.annotate('S',xy = (10,1),xycoords = 'data',xytext=(10,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'green')
	plt.annotate('D',xy = (15,1),xycoords = 'data',xytext=(15,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'red')	
	
	if os.path.exists('/home/koza/idz3/Plots/BrainPhysActivity.png') == True:
		os.remove('/home/koza/idz3/Plots/BrainPhysActivity.png')
	plt.savefig('/home/koza/idz3/Plots/BrainPhysActivity.png')
	
#	plt.show()

#createPlotBrnAct()
	
def createPlotTemper():
	fig,ax = plt.subplots()
	# M
	ax.plot(np.linspace(0,14),straight2(np.linspace(0,14)),'b')
	ax.plot(np.linspace(14,20),straight3(np.linspace(14,20),14,20),'b')
	# S
	ax.plot(np.linspace(14,20),straight1(np.linspace(14,20),14,20),'g')
	ax.plot(np.linspace(20,23),straight2(np.linspace(20,23)),'g')
	ax.plot(np.linspace(23,25),straight3(np.linspace(23,25),23,25),'g')
	# D1
	ax.plot(np.linspace(22,27),straight1(np.linspace(22,27),22,27),'y')
	ax.plot(np.linspace(27,30),straight3(np.linspace(27,30),27,30),'y')
	# D2
	ax.plot(np.linspace(28,35),straight1(np.linspace(28,35),28,35),'r')
	ax.plot(np.linspace(35,50),straight2(np.linspace(35,50)),'r')
	
	ax.minorticks_on()

	ax.grid(which='major',color = 'k',linewidth = 1)
	ax.grid(which='minor', color = 'k', linestyle = ':')
	
	plt.xlabel('TEMPERATURE(C)', fontsize=14, fontweight='bold')
	plt.annotate('M',xy = (14,1),xycoords = 'data',xytext=(14,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'blue')
	plt.annotate('S',xy = (22,1),xycoords = 'data',xytext=(22,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'green')
	plt.annotate('D1',xy = (27,1),xycoords = 'data',xytext=(27,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'yellow')
	plt.annotate('D2',xy = (35,1),xycoords = 'data',xytext=(35,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'red')
	
	if os.path.exists('/home/koza/idz3/Plots/Temperature.png') == True:
		os.remove('/home/koza/idz3/Plots/Temperature.png')
	plt.savefig('/home/koza/idz3/Plots/Temperature.png')

#	plt.show()
	
#createPlotTemper()

def createPlotMelat():
	fig,ax=plt.subplots()
	# M2
	ax.plot(np.linspace(0,20),straight2(np.linspace(0,20)),'purple')
	ax.plot(np.linspace(20,22),straight3(np.linspace(20,22),20,22),'purple')
	# M1
	ax.plot(np.linspace(20,22),straight1(np.linspace(20,22),20,22),'blue')
	ax.plot(np.linspace(22,25),straight3(np.linspace(22,25),22,25),'blue')
	# S
	ax.plot(np.linspace(22,25),straight1(np.linspace(22,25),22,25),'green')
	ax.plot(np.linspace(25,28),straight2(np.linspace(25,28)),'green')
	ax.plot(np.linspace(28,35),straight3(np.linspace(28,35),28,35),'green')
	# D
	ax.plot(np.linspace(30,35),straight1(np.linspace(30,35),30,35),'red')
	ax.plot(np.linspace(35,40),straight2(np.linspace(35,40)),'red')
	ax.plot(np.linspace(40,45),straight3(np.linspace(40,45),40,45),'red')
	
	ax.minorticks_on()

	ax.grid(which='major',color = 'k',linewidth = 1)
	ax.grid(which='minor', color = 'k', linestyle = ':')
	
	plt.xlabel('MELATONIN(mkg)', fontsize=14, fontweight='bold')
	plt.annotate('M2',xy = (10,1),xycoords = 'data',xytext=(10,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'purple')
	plt.annotate('M1',xy = (21,1),xycoords = 'data',xytext=(21,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'blue')
	plt.annotate('S',xy = (26,1),xycoords = 'data',xytext=(26,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'green')
	plt.annotate('D',xy = (35,1),xycoords = 'data',xytext=(35,1.03),textcoords='data',fontweight='bold',fontsize=14,color = 'red')
	
	if os.path.exists('/home/koza/idz3/Plots/Melatonin.png') == True:
		os.remove('/home/koza/idz3/Plots/Melatonin.png')
	plt.savefig('/home/koza/idz3/Plots/Melatonin.png')

	
#	plt.show()
	
#createPlotMelat()

####################
####################
####################

def regulationBase():
	lux = ['M','S','D1','D2']
	act = ['M','S','D']
	tmp = ['M','S','D1','D2']
	listBase = []
	for i in lux:
		for l in act:
			for k in tmp:
				listBase+=[[i,l,k]]
	row1 = 0
	df = pd.DataFrame(listBase)
	if os.path.exists('/home/koza/idz3/RegulationInp.csv') == True:
		os.remove('/home/koza/idz3/RegulationInp.csv')
	df.to_csv('/home/koza/idz3/RegulationInp.csv', header=False, index=False)

#regulationBase()

####################
####################
####################

def RegLux(luxVal):
	if luxVal >=0 and luxVal <= 3:
		if straight3(luxVal,0,3) >= straight1(luxVal,1,5):
			return 'M'
		else:
			return 'S'
	if luxVal > 3 and luxVal <= 7:
		return 'S'
	if luxVal > 7 and luxVal <= 10:
		if straight3(luxVal,5,10) >= straight1(luxVal,7,12):
			return 'S'
		else:
			return 'D1'
	if luxVal > 10 and luxVal <=15:
		return 'D1'
	if luxVal > 15 and luxVal <=20:
		if straight3(luxVal,15,20) >= straight1(luxVal,15,20):
			return 'D1'
		else:
			return 'D2'
	if luxVal > 20 and luxVal < 40:
		return 'D2'
	
def RegAct(ActVal):
	if ActVal >=0 and ActVal <= 5:
		return 'M'
	if ActVal > 4 and ActVal <= 6:
		if straight3(ActVal,4,6) >= straight1(ActVal,5,9):
			return 'M'
		else:
			return 'S'
	if ActVal > 6 and ActVal <= 14:
		return 'S'
	if ActVal > 14 and ActVal <= 15:
		if straight3(ActVal,14,16) >= straight1(ActVal,14,15):
			return 'S'
		else:
			return 'D'
	if ActVal > 15 and ActVal <= 20:
		return 'D'

def RegTemp(TempVal):
	if TempVal >= 0 and TempVal <= 14:
		return 'M'
	if TempVal > 14 and TempVal <= 20:
		if straight3(TempVal,14,20) >= straight1(TempVal,14,20):
			return 'M'
		else:
			return 'S'
	if TempVal > 20 and TempVal <=23:
		return 'S'
	if TempVal > 23 and TempVal <= 25:
		if straight3(TempVal,23,25) >= straight1(TempVal,22,27):
			return 'S'
		else:
			return 'D1'
	if TempVal > 25 and TempVal <= 28:
		return 'D1'
	if TempVal > 28 and TempVal <= 30:
		if straight3(TempVal,27,30) >= straight1(TempVal,28,35):
			return 'D1'
		else:
			return 'D2'
	if TempVal > 30 and TempVal <= 50:
		return 'D2'

####################
####################
####################

def phaseRes(lux, act, tmp):
	reglist = [RegLux(lux), RegAct(act), RegTemp(tmp)]
	df2 = pd.read_csv('/home/koza/idz3/RegulationInpFull.csv', sep = ',')
	for index,row in df2.iterrows():
		if df2.loc[index].tolist()[:3] == reglist:
			return df2.loc[index].tolist()

def MainFunc():
	while True:
		lux = input('\nВведите значение параметра степени освещённости - lux, от 0 до 40: ')
		if float(lux) < 0 or float(lux) > 40:
			print('\n! ! ! Значение lux = '+lux+' за пределами диапозона ! ! !')
		else:
			break
	print('\nlux = '+lux)
	while True:
		act = input('\nВведите значение параметра мозговой и физической активности в часах - act, от 0 до 20: ')
		if float(act) < 0 or float(act) > 20:
			print('\n! ! ! Значение lux = '+act+' за пределами диапозона ! ! !')
		else:
			break
	print('\nact = '+act)
	while True:
		temp = input('\nВведите значение параметра температуры помещения - temp, от 0 до 50: ')
		if float(temp) < 0 or float(temp) > 50:
			print('\n! ! ! Значение lux = '+temp+' за пределами диапозона ! ! !')
		else:
			break
	print('\ntemp = '+temp+'\n')
	reglist = phaseRes(float(lux), float(act), float(temp))
	print('#################')
	print('#################\n')
	print('Нечеткие правила: \n')
	print('Освещённость(lux): '+reglist[0])
	print('Активность(act): '+reglist[1])
	print('Температура(temp): '+reglist[2])
	print('Мелатонин: '+reglist[3]+' - Выходная переменная')
	
MainFunc()
	
		
	
	
	
	
	
	
	
