import copy
import numpy 
from classifier import Classifier

class adaBoostClassifier(Classifier):
    
	def __init__(self,noOfWeakLearners,classifierList,sampler):
		"""constructs a adaBoost Classifier with a specified number of weaklearners and classifier type and sampling algorithm"""
		self.noOfWeakLearners=noOfWeakLearners
		self.classifierTypeList=classifierList
		self.sampler=sampler
		self.weakLearners=[]
    
    
	def train(self,dataSet):
		"""Trains this adaBoost Classifier on the given data set"""
		weakLearners=[];
		sampleWeights=numpy.ones(dataSet.numberOfInstances)*1/dataSet.numberOfInstances;
		#Trains  the individual weak learners and pick the one with minimum error

		
		for learnerindex in range(self.noOfWeakLearners):
			minError=dataSet.numberOfInstances;
			minErrorClassifier=''
			minErrorSampleWeights=copy.deepcopy(sampleWeights);

			[sampledDataSet,indexMap]=self.sampler.sample(dataSet,sampleWeights)
			#for each weak learners trains an no of cnadidate classifiers and picks the best
			for learnerType in range(len(self.classifierTypeList)):
				print "Training started"
				tempSampleWeights=numpy.ones(dataSet.numberOfInstances)*1/dataSet.numberOfInstances;
				temClassifier=copy.deepcopy(self.classifierTypeList[learnerType]);
				trueClassifiedIndex=temClassifier.train(sampledDataSet);
				errorRate=float((sampledDataSet.numberOfInstances-len(trueClassifiedIndex)))/float(sampledDataSet.numberOfInstances)

				print "training finished"

				eps=0.00001
				if errorRate==1:
					errorRate=1-eps;
#				else:
#					errorRate=eps;
                
				print "Error rate:%s"%errorRate

#				print "True classified labels:%s"%(trueClassifiedIndex)

#				print "Index Map:%s"%(indexMap)
                
				updateIndex=set()
				# finds the correctly classified instances index in the full dataSet
				for index in trueClassifiedIndex:
					updateIndex.add(indexMap[index]);

				#update the true classified sample weights
				for index in updateIndex:
					tempSampleWeights[index]=tempSampleWeights[index]*(errorRate/(1-errorRate))

				if minError>errorRate*sampledDataSet.numberOfInstances:
					minError=errorRate*sampledDataSet.numberOfInstances;
					minErrorClassifier=temClassifier;
					minErrorSampleWeights=tempSampleWeights

			self.weakLearners.append(minErrorClassifier)
			print minErrorClassifier
			sampleWeights=minErrorSampleWeights

		for classifier in self.weakLearners:
			print classifier

	def test(self, inputDataSet):
		labels=[]
		for i in range(inputDataSet.numberOfInstances):
			labels.append(self.classify(inputDataSet.getInstance(i)))
		error , correctLabels , performance  = self.getError(inputDataSet.labels , labels , True);
		print "TP:%s\nFP:%s\nTN:%s\nFN:%s"%(performance.truePositive , performance.falsePositive , performance.trueNegative , performance.falseNegative)
		print "Performance of Adaboost:%s"% (performance)

	def classify(self, instance):
		count1=0;
		count2=0;
		for i in self.weakLearners:
			classifiedLabel = i.classify(instance)
			if float (classifiedLabel) ==float (1):
				count1=count1+1;
			else:
				count2=count2+1;
		if(count1>count2):
			return 1;
		else:
			return 2;

