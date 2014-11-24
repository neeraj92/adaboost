from parser import Parser
from dataset import DataSet
import csv
from bayesclassifier import *
from thresholdclassifier import *

# class for csv parser
class CsvParser (Parser):
	
	def parse (self , filePath):
		inputFile = open (filePath , "r")
		reader = csv.reader (inputFile , delimiter = "\t")
		
		dataset = DataSet ()
		isInitialised = False
		for row in reader:
			if not isInitialised :
				dataset.attributeType = [float (row[i]) for i in range (0 , len (row[0:-1]))]
				dataset.numberOfAttributes = len (dataset.attributeType)
				isInitialised = True
			else:
				dataset.data.append ([float (row[i]) for i in range (0 ,  (dataset.numberOfAttributes))])
				dataset.labels.append (row[-1])

				dataset.numberOfInstances += 1;


		return dataset



if __name__=="__main__":
	parser = CsvParser ()
	dataset = parser.parse ("/home/chikku/Downloads/UK-2011Webspamdataset.csv")			
	classifier = BayesClassifier ("temp")
	classifier.train (dataset)
	print classifier.parameter

