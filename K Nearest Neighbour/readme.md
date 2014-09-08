# kNN(k-Nearest Neighbour Algorithm)

kNN is used for classification problem.

## Features
Pros:
	* High precision
	* Not sensitive of the outlier
Cons:
	* Computation complex is high
	* Cost a lot of space bacause of store all the data set in memory.
	* There is no model for this algorithm(no training progress neither). It's not easy to give a summary of the predict data.

## Preprocessing
1. Feature extraction
2. Feature normalization(because all the features contribute to the distance). We need to scale the feature's value to 0-1.

## Steps
1. Calculate the a given sample's distances between all samples in the data set.
2. Sort the distances in descending order.
3. Select the top-K samples.
4. All these k samples vote for the given sample's class label.
	4.1 Calculate each class label's frequence by these k samples.
	4.2 Select to class label with the most frequence.