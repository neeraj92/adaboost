#class that holds the performance metrics for a model

class PerformanceMetrics (object):
	
	def __init__(self):
		# values to be updated based on the test results
		self.truePositive = 0
		self.trueNegative = 0
		self.falsePositive = 0
		self.falseNegative = 0
	
	def incrementTP (self):
		self.truePositive = self.truePositive + 1
	
	def incrementFP (self):
		self.falsePositive = self.falsePositive + 1
	
	def incrementTN (self):
		self.trueNegative = self.trueNegative + 1
	
	def incrementFN (self):
		self.falseNegative = self.falseNegative + 1
	
	def getAccuracy (self):
		return float (self.truePositive + self.trueNegative) / float ( self.truePositive + self.trueNegative + self.falsePositive + self.falseNegative )

	def getPrecision (self):
		return	float (self.truePositive) / float (self.truePositive + self.falsePositive)
	
	def getRecall (self):
		return float (self.truePositive) / float (self.truePositive + self.falseNegative)
	
	def getFMeasure (self):
		return float ( 2 * self.getPrecision () * self.getRecall () ) / float(self.getPrecision() + self.getRecall ())

	def __str__ (self):
		return "Accuracy:%s\nPrecision:%s\nRecall:%s\nFMeasure:%s"%(self.getAccuracy () , self.getPrecision () , self.getRecall () , self.getFMeasure ())
