from thresholdParameter import *
from adaBoost import adaBoostClassifier
from csvparser import CsvParser
from bayesclassifier import BayesClassifier
from thresholdclassifier import ThresholdClassifier
from naiveSampler import naiveSampler


if __name__=="__main__":
	parser = CsvParser ()
	dataset = parser.parse ("/home/chikku/Downloads/UK-2011Webspamdataset.csv")			
	
	thresholdClassifier = ThresholdClassifier ("Threshold")
	bayesClassifier = BayesClassifier ("Bayes")

	classifierList = list ()
	classifierList.append (thresholdClassifier)
	classifierList.append (bayesClassifier)

	sampler = naiveSampler ()

	boostClassifier = adaBoostClassifier (20 , classifierList , sampler)
	boostClassifier.train (dataset)
	boostClassifier.test (dataset)
