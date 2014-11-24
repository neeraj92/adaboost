from parameter import *

# Parameter class that holds parameter value for threshold based parameter
class ThresholdBasedClassifierParameter (Parameter):
	# init function
	def __init__ (self):
		self.threshold = None
		self.attribute = None	
		self.compareFunc = None
	
	def setParameter (self , parameterName , parameterValue):
		if parameterName == "Threshold":
			self.threshold = parameterValue
		elif parameterName == "Attribute":
			self.attribute = parameterValue
		elif parameterName == "CompareFunction":
			self.compareFunc = parameterValue
	
	def getParameter (self , parameterName , parameterValue):
		if parameterName == "Threshold":
			return self.threshold
		elif parameterName == "Attribute":
			return self.attribute
		elif parameterName == "CompareFunction":
			return self.compareFunc
	
	def __str__ (self):
		return "Threshold Value:%s \nAttribute:%s"% (self.threshold , self.attribute)


def comparePositive (val1 , val2):
	if val1 >= val2:
		return True
	return False

def compareNegative (val1 , val2):
	if val1 <= val2:
		return True
	return False
