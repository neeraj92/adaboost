from thresholdParameter import ThresholdBasedClassifierParameter as Parameter
from thresholdParameter import comparePositive , compareNegative
from classifier import Classifier

# Class for threshold based classifier

class ThresholdClassifier (Classifier):
	
	def __init__ (self , name):
		super (ThresholdClassifier , self).__init__ (name)
		self.parameter = Parameter ()
	
	# function to set parameter values
	def setParameterValue (self , attribute , threshold , compareFunc ):	
		self.parameter.attribute = attribute
		self.parameter.threshold = threshold
		self.parameter.compareFunc = compareFunc


	def train (self , dataset):
		
		print "Threshold classifier:Training started"
		minError =  (dataset.numberOfInstances)

		truePositiveLabels = list ()

		# iterate over the dimensions
		for dimIter in range ( 0 , len (zip(*dataset.data)) ):
			print "Threshold classifier: Working on Dimension:%s"%(dimIter)
			sortedValues = sorted (zip(*dataset.data)[dimIter])
			
			# iterate over each value for threshold checking
			for valIter in range ( 0 , len (sortedValues)):
				if valIter == 0 or valIter == len (sortedValues) - 1:
					threshold = sortedValues[valIter] / 2
				else:
					threshold = ( sortedValues [valIter] + sortedValues[valIter - 1] )/2
			
				# check for greater than
				compareFunc = comparePositive
				newLabels = list ()
			
				# find the error for current settings
				for compareIter in range (0,2):
					for i in range (0 , dataset.numberOfInstances):
						if compareFunc (dataset.data[i][dimIter] , threshold):
							newLabels.append (1)
						else:
							newLabels.append (2)

					error , tempTPLabels , tempPerformance = self.getError ( dataset.labels , newLabels )
					# if the error is less than the already existing error then set new model
					if error < minError:
						self.setParameterValue (dimIter , threshold , compareFunc)
						minError = error
						truePositiveLabels = tempTPLabels
					
					# check for less than
					compareFunc = compareNegative	
		
		print "Threshold classifier:Finished training"
		return truePositiveLabels
		
	# classify a single instance fed in as a list
	def classify (self , inputData):
		if self.parameter.compareFunc (inputData[self.parameter.attribute] , self.parameter.threshold):
			return 1
		return 2
	
	# test and give the stats of a set of inputs
	def test (self , dataset):
		classifiedLabels = list ()

		for i in range (0 , len(zip(*dataset.data)[self.parameter.attribute])):
			if self.parameter.compareFunc (dataset.data[i][self.parameter.attribute] , self.parameter.threshold):
				classifiedLabels.append (1)
			else:
				classifiedLabels.append (2)

		return self.getError (dataset.labels , classifiedLabels)

