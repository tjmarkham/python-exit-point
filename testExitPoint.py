from exitPoint import exitPoint
from time import sleep

count = 0

def testFunction():
	print("Running test function before exiting. Count = ", count)

while(1==1) :
	exitPoint(True, testFunction, "Goodbye message!")
	count += 1
	print("Check out this infinite loop! Count = ", count)
	sleep(1)
