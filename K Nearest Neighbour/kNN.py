from numpy import *
import operator

def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

def classify0(inX, dataSet, labels, k):
	'''k-Nearest Neighbour Alogrithm
	'''
	dataSetSize = dataSet.shape[0]
	# tile(A, reps) -> Construct an array by repeating A the number of times given by reps.
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet # make inX the same shape as dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqrt(sqDistances)
	# argsort(a, axis=-1, kind='quicksort', order=None) -> Returns the indices that would sort an array.
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True) # sort by count
	return sortedClassCount[0][0]

if __name__ == '__main__':
	group, labels = createDataSet()
	print classify0([0,0], group, labels, 3)

