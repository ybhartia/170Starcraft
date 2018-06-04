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
	joblib.dump(clfPoly, 'SVM/clfPoly.pkl')

	#
	# Linear Model
	#
	clfLinear = svm.SVC(kernel='linear') 
	clfLinear.fit(xTrainData, yTrainData)
	joblib.dump(clfLinear, 'SVM/clfLinear.pkl')

	#
	# Sigmoid Model
	#
	clfSigmoid = svm.SVC(kernel='sigmoid')
	clfSigmoid.fit(xTrainData, yTrainData) 
	joblib.dump(clfSigmoid, 'SVM/clfSigmoid.pkl')


#
# A function that given a data test of testing picks out the best model from the replays
# We use the previously created models from the trainReplays and get a score
# The higher the score the better the model
#
def pickBestModel(xTestData, yTestData):
	
	bestFileName = "" # will store the string of the name of the best file 
	bestScore = 0 # will store the best score from the model

	#
	# Polynomial model with degree 1
	#
	clfPoly = joblib.load('SVM/clfPoly.pkl') 
	score = clfPoly.score(xTestData, xTrainData)

	if(score > bestScore):
		bestScore = score
		bestFileName = 'SVM/clfPoly.pkl'
	
	#
	# Linear model
	#
	clfLinear = joblib.load('SVM/clfLinear.pkl') 
	score = clfLinear.score(xTestData, xTrainData)

	if(score > bestScore):
		bestScore = score
		bestFileName = 'SVM/clfLinear.pkl'
	
	#
	# Sigmoid Model
	#
	clfSigmoid = joblib.load('SVM/clfSigmoid.pkl') 
	score = clfSigmoid.score(xTestData, xTrainData)

	if(score > bestScore):
		bestScore = score
		bestFileName = 'SVM/clfSigmoid.pkl'


	# returns the best score, aka - confidence, and the file name for the best model
	return bestFileName, bestScore


#
# A function that takes in input from the current going game (or Replay)
# and outputs whether they think if they will win or not
# 
def checkForWin(inputLayer, bestModel):

	#
	# this loads the best model recieved from the previous function and predict
	#
	clf = joblib.load(bestModel)
	prediction = clf.predict([inputLayer])

	return prediction[0]







