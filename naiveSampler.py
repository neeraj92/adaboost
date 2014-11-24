import copy
import random
from sampler import Sampler
from dataset import DataSet

class naiveSampler(Sampler):
	def __init__(self):
		pass

	def sample(self,inputDataSet,sampleWeights):
		""" sampels a given data set with respect to the given sample weights"""        
		print "sampling started"
		sampledDataSet=DataSet()
		indexMap= dict()
		cumulativeWeights=copy.deepcopy(sampleWeights)

		sampledDataSet.numberOfAttributes = inputDataSet.numberOfAttributes
		sampledDataSet.attributeType = inputDataSet.attributeType

		#calculate the cumulative weights 
		for i in range(len(sampleWeights)):
			if(i!=0):
				cumulativeWeights[i]=cumulativeWeights[i-1]+cumulativeWeights[i];
		#generate a sample of the same size as the input dataset
		for i in range(len(sampleWeights)):
			rand=random.random()
			#generate a random number and find which bin it belongs to and add the instance corresponding to that bin to the new data set
			for j in range(len(sampleWeights)):
				if j < len (sampleWeights) - 1:
					if(cumulativeWeights[j] < rand and cumulativeWeights[j+1] > rand):
						sampledDataSet.addInstance(inputDataSet.getInstance(j-1));
						sampledDataSet.addLabel (inputDataSet.getLabelForIndex(j-1))
						indexMap[sampledDataSet.numberOfInstances - 1]=j-1;
#						print "Adding point %s to sample"%(j)
					else:
						continue
				else:
					if(cumulativeWeights[j] < rand ):
						sampledDataSet.addInstance(inputDataSet.getInstance(j-1));
						sampledDataSet.addLabel (inputDataSet.getLabelForIndex(j-1))
						indexMap[sampledDataSet.numberOfInstances - 1]=j-1;
#						print "Adding point %s to sample"%(j)

		print "Size of sample:%s"%(sampledDataSet.numberOfInstances)
		print "sampling finished"
		return [sampledDataSet,indexMap];

    
