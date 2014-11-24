# File with statistics utilities

import math

#function to get mean
def getMean (data):
#	print "%s len of data"%(len(data))
	if len (data) == 0:
		return 0
	return sum (data) / len (data)


#function to get std
def getStd (data):
	if len (data) == 0:
		return 0
	
	dataMean = getMean (data)
	
	totalSum = 0
	for i in range (0 , len (data)):
		totalSum += (data[i] - dataMean) * (data[i] - dataMean)
	
	return (math.sqrt (totalSum / len (data)))

# function to get the normal distribution value given mean and std
def getNormalDistribution (dataMean , dataStd , inputValue):
	value = (1 /float(math.sqrt(2*3.14)*dataStd)) * math.exp (-0.5 *math.pow ((float(inputValue - dataMean) / float(dataStd)) , 2) )
	return value
