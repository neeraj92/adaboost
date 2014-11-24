# Class for an object
class Model(object):
	def __init__(self):
		# Name of the model
		self.modelName = "Null"

		# Parameter values
		self.parameter = "Null"
	
	def setParameter (self , parameter):
		self.parameter = parameter
	
	def getParameter (self , parameter):
		return self.parameter
	
	def setModelName (self , modelName):
		self.modelName = modelName
	
	def getModelName (self , modelName):
		return self.modelName
	
	# toString function
	def __str__ (self):
		return "Model Name:%s \n Parameters:%s"%(self.modelName , self.parameter)
