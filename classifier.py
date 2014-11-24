from performancemetrics import PerformanceMetrics 
# Base class for classifier
class Classifier (object):
	def __init__ (self , name):
		self.name = name
		self.parameter = None
	
	# function trains the model and sets and then returns the parameter values
	def train (self , dataset ):
		pass
	
	# function tests the model and on a set of test data and returns the test statistics
	def test (self , dataset):
		pass
	
	# function classifies the input data into a class
	def classify ( self , inputData ):
		pass

	# get error given actual labels and classified labels
	def getError (self , labels , classifiedLabels , addPerformance = False):
		error = 0
		performance = PerformanceMetrics ()

		truePositiveIndices = list ()
#		print "length of labels:%s classifiedlabels:%s"%(len (labels) , len (classifiedLabels))
		for i in range (0 , len (labels)):
			
			if float(labels[i]) !=  float (classifiedLabels[i]):
				error += 1
			else:
				truePositiveIndices.append (i)
			
			if addPerformance:
				if float (classifiedLabels[i]) == 1:
					if float (labels[i]) == float (classifiedLabels[i]):
						performance.incrementTP ()
					else:
						performance.incrementFP ()
				else:
					if float (labels[i]) == float (classifiedLabels[i]):
						performance.incrementTN ()
					else:
						performance.incrementFN ()

		return error, truePositiveIndices , performance
	
	def __str__ (self):
		return "Name:%s\nParametres:%s"%(self.name , self.parameter)
