import serial
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import Canvas

modeChoices = {'LED', 'Red RGB LED', 'Green RGB LED', 'Blue RGB LED', 'Servo'}
portChoices = {'COM0','COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8'}
UARTBaudRate = ''
COMPort = ''

def enableDisableChannelOne():
	if(channelOneBox.get() == 1):
		ser.write(b'0E1S')
	else:
		ser.write(b'0D1S')
	return

def enableDisableChannelTwo():
	if(channelTwoBox.get() == 1):
		ser.write(b'0E2S')
	else:
		ser.write(b'0D2S')
	return

def enableDisableChannelThree():
	if(channelThreeBox.get() == 1):
		ser.write(b'0E3S')
	else:
		ser.write(b'0D3S')
	return

def submitOneChannelFreq():
	data = bytes(feqOneEntry.get()+'S', 'utf-8')
	ser.write(b'1F1')
	ser.write(data)
	return

def submitOneChannelDC():
	DCOneValueStr = bytes(str(DCOneValue.get())+'S', 'utf-8')
	ser.write(b'0P1')
	ser.write(DCOneValueStr)
	return

def submitTwoChannelFreq():
	data = bytes(feqTwoEntry.get()+'S', 'utf-8')
	ser.write(b'0F2')
	ser.write(data)
	return 

def submitTwoChannelDC():
	DCTwoValueStr = bytes(str(DCTwoValue.get())+'S',  'utf-8')
	ser.write(b'0P2')
	ser.write(DCTwoValueStr)
	return

def submitThreeChannelFreq():
	data = bytes(feqThreeEntry.get()+'S', 'utf-8')
	ser.write(b'0F3')
	ser.write(data)
	return  

def submitThreeChannelDC():
	DCThreeValueStr = bytes(str(DCThreeValue.get())+'S', 'utf-8')
	ser.write(b'0P3')
	ser.write(DCThreeValueStr)
	return  

def moduleOne():
	global feqOneEntry, DCOneValue
	enableDisableChannelOne()
	if(channelOneBox.get() == 1):
		modeOptionChannelOne = tk.StringVar(guiroot)
		modeOptionChannelOne.set('LED')
		modeOneMenu = tk.OptionMenu(guiroot, modeOptionChannelOne, *modeChoices)
		modeOneMenu.grid(row=2, column=0,rowspan=2, columnspan=3)

		#if(modeOptionChannelOne.get() != ''):
		tk.Label(guiroot, text='Frequency:').grid(row=4, column=0)
		feqOneEntry = tk.Entry(guiroot)
		feqOneEntry.grid(row=4, column=1, pady=10) 
		tk.Label(guiroot, text='Duty Cycle:').grid(row=5, column=0, pady=10)
		DCOneValue = tk.IntVar() 
		DCOneEntry = tk.Scale(guiroot, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, variable=DCOneValue)
		DCOneEntry.grid(row=5, column=1)
		tk.Label(guiroot,textvariable=DCOneValue, width=2).grid(row=5,column=1, sticky="e")
		startOneFreq = tk.Button(guiroot, text='Submit Freq',width=9, command=submitOneChannelFreq).grid(row=6, column=1, sticky="w")
		startOneDC = tk.Button(guiroot, text='Submit DC',width=9, command=submitOneChannelDC).grid(row=6, column=1, sticky="e")


def moduleTwo():
	global feqTwoEntry, DCTwoValue
	enableDisableChannelTwo()
	if(channelTwoBox.get() == 1):
		modeOptionChannelTwo = tk.StringVar(guiroot)
		modeOptionChannelTwo.set('LED')
		modeTwoMenu = tk.OptionMenu(guiroot, modeOptionChannelTwo, *modeChoices)
		modeTwoMenu.grid(row=2, column=5,rowspan=2, columnspan=3)

		#if(modeOptionChannelTwo.get() != ''):
		tk.Label(guiroot, text='Frequency:').grid(row=4, column=5, sticky="e")
		feqTwoEntry = tk.Entry(guiroot)
		feqTwoEntry.grid(row=4, column=6, pady=10) 
		tk.Label(guiroot, text='Duty Cycle:').grid(row=5, column=5, sticky="e")
		DCTwoValue = tk.IntVar() 
		DCTwoEntry = tk.Scale(guiroot, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, variable=DCTwoValue)
		DCTwoEntry.grid(row=5, column=6)
		tk.Label(guiroot,textvariable=DCTwoValue, width=2).grid(row=5,column=6, sticky="e")
		startTwoFreq = tk.Button(guiroot, text='Submit Freq',width=9, command=submitTwoChannelFreq).grid(row=6, column=6, sticky="w")
		startTwoDC = tk.Button(guiroot, text='Submit DC',width=9, command=submitTwoChannelDC).grid(row=6, column=6, sticky="e")

def moduleThree():
	global feqThreeEntry, DCThreeValue
	enableDisableChannelThree()
	if(channelThreeBox.get() == 1):
		modeOptionChannelThree = tk.StringVar(guiroot)
		modeOptionChannelThree.set('LED')
		modeThreeMenu = tk.OptionMenu(guiroot, modeOptionChannelThree, *modeChoices)
		modeThreeMenu.grid(row=2, column=10,rowspan=2, columnspan=3)

		#if(modeOptionChannelThree.get() != ''):
		tk.Label(guiroot, text='Frequency:').grid(row=4, column=10, sticky="e")
		feqThreeEntry = tk.Entry(guiroot)
		feqThreeEntry.grid(row=4, column=11, pady=10) 
		tk.Label(guiroot, text='Duty Cycle:').grid(row=5, column=10, sticky="e")
		DCThreeValue = tk.IntVar() 
		DCThreeEntry = tk.Scale(guiroot, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, variable=DCThreeValue)
		DCThreeEntry.grid(row=5, column=11)
		tk.Label(guiroot,textvariable=DCThreeValue, width=2).grid(row=5,column=11, sticky="e")
		startThreeFreq = tk.Button(guiroot, text='Submit Freq',width=9, command=submitThreeChannelFreq).grid(row=6, column=11, sticky="w")
		startThreeDC = tk.Button(guiroot, text='Submit DC',width=9, command=submitThreeChannelDC).grid(row=6, column=11, sticky="e")

def submitCallBack():
	global ser
	if(COMOptionDropDown.get() == ''):
		tkMessageBox.showerror('Error', 'Not a valid COM PORT')
	if(baudEntry.get() == ''):
		tkMessageBox.showerror('Error', 'Not a valid Serial Baudrate')
	else:
		UARTBaudRate = baudEntry.get()
		COMPort = COMOptionDropDown.get()
		startRoot.destroy()
		ser = serial.Serial(COMPort, UARTBaudRate, timeout=10)
		GUIScreen()

def startScreen():
	global baudEntry
	global COMOptionDropDown
	global startRoot
	startRoot = tk.Tk()
	startRoot.title('ECE530 PWM Controller')
	startRoot.resizable(False,False)

	tk.Label(startRoot, text='COM Port').grid(row=0)
	tk.Label(startRoot, text='Serial Baudrate').grid(row=2)

	COMOptionDropDown = tk.StringVar(startRoot)
	COMOptionDropDown.set('')

	popupMenu = tk.OptionMenu(startRoot, COMOptionDropDown, *portChoices)
	popupMenu.grid(row=0, column=1) 

	baudEntry = tk.Entry(startRoot)  
	baudEntry.grid(row=2, column=1) 

	submitButton = tk.Button(startRoot, text='Submit',width=20, command=submitCallBack)
	submitButton.grid(row=5, column=0)
	cancelButton = tk.Button(startRoot, text='Exit', width=20, command=startRoot.destroy)
	cancelButton.grid(row=5, column=1)

	startRoot.mainloop()

def GUIScreen():
	global guiroot
	global channelOneBox, channelTwoBox, channelThreeBox
	guiroot = tk.Tk()
	guiroot.title('ECE530 PWM Controller')
	channelOneBox = tk.IntVar()
	channelTwoBox = tk.IntVar()
	channelThreeBox = tk.IntVar()
	check1 = tk.Checkbutton(guiroot, text='PWM Channel 1', variable=channelOneBox, command=moduleOne).grid(row=0, column=0, columnspan=3)
	check2 = tk.Checkbutton(guiroot, text='PWM Channel 2', variable=channelTwoBox, command=moduleTwo).grid(row=0, column=5, columnspan=3)#, padx=150
	check3 = tk.Checkbutton(guiroot, text='PWM Channel 3', variable=channelThreeBox, command=moduleThree).grid(row=0, column=10, columnspan=3, padx=0)

	guiroot.grid_columnconfigure(0, minsize=100)
	guiroot.grid_columnconfigure(1, minsize=150)
	guiroot.grid_columnconfigure(2, minsize=100)

	guiroot.grid_columnconfigure(5, minsize=100)
	guiroot.grid_columnconfigure(6, minsize=150)
	guiroot.grid_columnconfigure(7, minsize=100)

	guiroot.grid_columnconfigure(10, minsize=100)
	guiroot.grid_columnconfigure(11, minsize=150)
	guiroot.grid_columnconfigure(12, minsize=100)

	guiroot.mainloop()


startScreen()
#GUIScreen()