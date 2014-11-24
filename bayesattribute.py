from statisticutils import getMean , getStd , getNormalDistribution

# Class to hold the details of a continuous attribute
class Attribute (object):
	def __init__ (self):
		# to determine if it is continuous or discrete
		self.attributeType = None
	
	# getters and setters
	def setAttributeType (self , attributeType):
		self.attributeType = attributeType
	
	def getAttributeType (self):
		return self.attributeType
	
	# to get the probability associated with the model
	def getProbability(self , inputValue ):
		pass

class ContinuousAttributeParameter (Attribute):
	def __init__ (self):
		self.mean = dict ()
		self.std = dict ()
	
	# getters and setters

	def getMean (self , classType):
		if classType in self.mean.keys ():
			return self.mean[classType]
		return None
	
	def getStd (self , classType):
		if classType in self.std.keys ():
			return self.std
		return None
	
	def setMean (self , classType , mean):
		self.mean[classType] = mean

	def setStd (self , classType , std):
		self.std[classType] = std
	
	# to get the probability based on the normal distribution
	def getProbability (self , inputValue):
		return getNormalDistribution (self.mean[inputValue[0]] , self.std[inputValue[0]] , inputValue[1])
			
	# toString
	def __str__ (self):
		return "Continuous Attribute:\nMean:%s\nStandard Deviation:%s\n"%(self.mean , self.std)


# class to hold the details of discrete attribute
class DiscreteAttributeParameter (Attribute):
	def	__init__ (self):
		self.tpm = dict ()
	
	# getters and setters
	def setTpm ( self , tpm):
		self.tpm = tpm
	
	def getTpm (self):
		return self.tpm
	
	# to get the probability based on the tpm
	def getProbability (self , inputValue):
		return self.tpm[inputValue[0]][inputValue[1]]
	
	# toString 
	def __str__ (self):
		output = "Distcrete Attribute:\n"
		if len (self.tpm) == 0:
			output += "No tpm set"
		else:
			for i in range (0,len (self.tpm)):
				for j in range (0,len (self.tpm[0])):
					output += self.tpm[i][j] + " "
				output += "\n"

		return output


