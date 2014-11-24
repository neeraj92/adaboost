from bayesparameter import *
from classifier import *
from statisticutils import *

# class for Bayes classifier 
class BayesClassifier (Classifier):
	
	def __init__ (self , name):
		super (BayesClassifier , self).__init__ (name)
		self.parameter = BayesClassifierParameter ()
		self.classLabels = None
	
	def getDataForClass (self , data , labels , classLabel):
		retData = list ()
		for i in range (0 , len (labels)):
			if float(labels[i]) == float(classLabel):
				retData.append (data[i])
		return retData
	
	def train (self , dataset ):
		
		print "Bayes classifier: Training started"		
		# class labels to get conditional probability
		classLabels = list (set (dataset.labels))
		self.classLabels = classLabels
	
		classProb = dict ()
		for i in range ( 0 , len (classLabels)):
			classProb[classLabels[i]] = float(dataset.labels.count (classLabels[i])) / float(len (dataset.labels))

		self.parameter.setParameter ("ClassProbabilities" , classProb)


		# iterate over all the attributes
		for dimIter in range (0 , dataset.numberOfAttributes):
			print "Bayes classifier: Working on dimension:%s"%(dimIter)
			attribute = None
			# if number of unique values > 5 then treat as continuous
			if dataset.attributeType[dimIter] == 1:
				attribute = ContinuousAttributeParameter ()			

				# iterate over all the classes and get all mean and std
				for classIter in range (0 , len (classLabels)):
					classData = self.getDataForClass (zip(*dataset.data)[dimIter] , dataset.labels , classLabels[classIter])
					attribute.setMean (classLabels[classIter] , getMean(classData))
					attribute.setStd (classLabels[classIter] , getStd (classData))
			
			# treat as discreet
			else:
				attribute = DiscreteAttributeParameter ()	
				
				uniqueVals = set (zip(*dataset.data)[dimIter])		
				tpm = dict ()
				# iterate over all the classes and form the tpm
				for classIter in range (0 , len (classLabels)):
					classData = self.getDataForClass (zip(*dataset.data)[dimIter] , dataset.labels , classLabels[classIter])
					tpm[classLabels[classIter]] = dict()

					# iterate over all the unique values in attribute
					for valIter in range (0 , len (uniqueVals)):
						tpm[classLabels[classIter]][uniqueVals[valIter]] = classData.count (uniqueVals[valIter]) / len (classData)

				attribute.setTpm (tpm)

			self.parameter.setParameter (dimIter , attribute)

		error , truePositiveIndices , performance =  self.test (dataset)
		
		print "Bayes Classifier: Finished training"
		print "Performance:\n%s"% (performance)
		return truePositiveIndices
	
	def test (self , dataset):
		label = None
		predictedLabels = list ()

		# iterate over all the data points
		for dataIter in range (0 , len (dataset.labels)):

			maxProb = 0;
			#iterate over all the classes
			for classIter in range (0 , len (self.classLabels)):
				prob = self.parameter.getParameter ("ClassProbabilities")[self.classLabels[classIter]]
				
				# iterate over all the dimensions
				for dimIter in range (0 , len (zip(*dataset.data))):
		#			print "%s:Dimension iterator"%(dimIter)
					probabilityInput = list ()
					probabilityInput.append (self.classLabels[classIter])
					probabilityInput.append (dataset.data[dataIter][dimIter])
					prob = prob * self.parameter.getParameter (dimIter).getProbability(probabilityInput)
				
				# if a class has higher probability then set it as label
				if prob > maxProb : 
					maxProb = prob
					label = self.classLabels[classIter]

			predictedLabels.append (label)

		return self.getError (dataset.labels , predictedLabels , True)
	
	def classify (self , inputData):
		maxProb = 0;
		label = -1
		#iterate over all the classes
		for classIter in range (0 , len (self.classLabels)):
			prob = self.parameter.getParameter ("ClassProbabilities")[self.classLabels[classIter]]
				
			# iterate over all the dimensions
			for dimIter in range (0 , len (inputData)):
				prob = prob * self.parameter.getParameter (dimIter).getProbability([self.classLabels[classIter] , inputData[dimIter]])
			
			# if a class has higher probability then set it as label
			if prob > maxProb : 
				maxProb = prob
				label = self.classLabels[classIter]
		return label
	
	def getProbabilityForPoint (self , inputData):
		maxProb = 0;
		#iterate over all the classes
		for classIter in range (0 , len (self.classLabels)):
			prob = self.parameter.getParameter ("ClassProbabilities")[self.classLabels[classIter]]
				
			# iterate over all the dimensions
			for dimIter in range (0 , len (inputData)):
				prob = prob * self.parameter.getParameter (dimIter).getProbability([self.classLabels[classIter] , inputData[dimIter]])
			
			# if a class has higher probability then set it as label
			if prob > maxProb : 
				maxProb = prob

		return maxProb

			
	def getProbabilityValues (self , dataset ):
		probs = dict ()
		for i in range (0 , dataset.numberOfInstances ):
			probs[i] = self.getProbabilityForPoint ( dataset.getInstance (i) )

		return probs
