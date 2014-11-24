from parameter import Parameter
from bayesattribute import *

# Parameter class to hold the Naive Bayes classifier parameters
class BayesClassifierParameter (Parameter):
	
	def __init__ (self):
		self.attributes = dict ()
	
	def setParameter (self , parameterName , parameterValue):
		self.attributes[parameterName] = parameterValue
	
	def getParameter (self , parameterName):
		if parameterName in self.attributes.keys ():
			return self.attributes[parameterName]
	
	def __str__ (self):
		output = ""
		for key in self.attributes.keys ():
			output += str(self.attributes[key]) + "\n"

		return output
	
