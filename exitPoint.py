import signal
from os.path import basename
from inspect import stack

exitStatus = False

#changes exitStatus to True
def exitHandler(signum, frame):
	global exitStatus
	exitStatus = True

#function that does nothing
def blankFunction():
	return

#places point for program to exit with optional message
#takes boolean argument (debug), if true print name of program that is exiting
#takes function argument (functionToExecute) to execute before exiting
#takes message argument (message) to print before exiting
def exitPoint(debug=False, functionToExecute=blankFunction, message=''):
	global exitStatus
	if(exitStatus):
		functionToExecute()
		print('')
		if (message != ''):
			print(message)
		if (debug):
			filePath = stack()[1][1]
			fileName = basename(filePath)
			print("Exiting from " + fileName + "...")
	
		signal.signal(signal.SIGINT, original_sigint)
		exit(1)

#make ctr-c execute exitHandler
original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exitHandler)
