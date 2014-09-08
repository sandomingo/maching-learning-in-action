'''
Text classification
'''
sentences = ['my dog has flea problems help please', 'maybe not take hime to dog park stupid', 'my dalmation is so cute I love him', 'stop posting stupid worthless garbage', 'mr licks ate my steak how to stop him', 'quit buying worthless dog food stupid']
classVec = [0, 1, 0, 1, 0, 1] # 0 represents negative sentence while 1 represents positive

def loadDataSet():
    postingList=[]
    for sentence in sentences:
        postingList.append(sentence.split())
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set()
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWord2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in createVocabList:
            returnVec[createVocabList.index(word)] = 1
    return returnVec

def trainNB0(trainMatrix, trainCategory):
