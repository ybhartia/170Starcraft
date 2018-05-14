from sklearn import svm
from sklearn.externals import joblib

#
# A function that given a data set of training data creates models for replays
# We use three basic models for SVMs
# Addtionally xTrainData should be a (R x N) matrix and yTrainData should be 1d array with length N
# N = input layer
# R = Number of Replays for training purposes
#
def trainReplays(xTrainData, yTrainData):

	#
	# Polynomial model with degree 1
	#
	clfPoly = svm.SVC(kernel='poly', degree=1) # Since input layer should be small
	clfPoly.fit(xTrainData, yTrainData)
	joblib.dump(clfPoly, 'clfPoly.pkl')

	#
	# Linear Model
	#
	clfLinear = svm.SVC(kernel='linear') 
	clfLinear.fit(xTrainData, yTrainData)
	joblib.dump(clfLinear, 'clfLinear.pkl')

	#
	# Sigmoid Model
	#
	clfSigmoid = svm.SVC(kernel='linear')
	clfSigmoid.fit(xTrainData, yTrainData) 
	joblib.dump(clfSigmoid, 'clfSigmoid.pkl')