
# class that holds the data and labels along with the details about the continuous and discrete data
class DataSet (object):
	
	def __init__ (self):
		# data
		self.data = list ()
		# labels
		self.labels = list ()
		# list containing a value corresponding to each attribute. Represents if the data is continuous or discrete
		self.attributeType = None

		self.numberOfAttributes = 0
		self.numberOfInstances = 0
	
	# getters and setters
	def getData (self):
		return self.data
	
	def getLabels (self):
		return self.labels
	
	def getAttributeType (self):
		return self.attributeType

	def setData (self , data):
		self.data = data
	
	def setLabels (self , labels):
		self.labels = labels

	def setAttributeType (self , attributeType):
		self.attributeType = attributeType

	def setNumberOfInstances (self , numberOfInstances):
		self.numberOfInstances = numberOfInstances
	
	def setNumberOfAttributes (self , numberOfAttributes):
		self.numberOfAttributes = numberOfAttributes
	
	def getNumberOfAttributes (self ):
		return self.numberOfAttributes
	
	def getNumberOfInstances (self):
		return self.numberOfInstances

	def addInstance (self , data):
		self.data.append (data)
		self.numberOfInstances += 1
	
	def getInstance (self , index):
		return self.data[index]
	
	def getLabelForIndex (self , index):
		return self.labels[index]

	def addLabel (self , label):
		self.labels.append (label)

