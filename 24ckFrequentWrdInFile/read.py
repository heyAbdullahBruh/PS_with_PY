#Problem-23 ---> Find the Most Frequent Word in a Text File



def findMostFrequentWordInfile(filename):
    fileTxt =open(filename, "r")
    fileData = fileTxt.read()
    txtToList = fileData.split()
    wordCount ={}
    
    for w in txtToList :
        if w=='':
            return
        if w in wordCount:
            wordCount[w] =wordCount[w]+1
        else :
            wordCount[w] =1
    frequentWord={}
    mx=0
    for i in wordCount :
        if wordCount[i] > mx:
            mx=wordCount[i]
            frequentWord.clear()
            frequentWord[i]=wordCount[i]
    return frequentWord

totalWord =findMostFrequentWordInfile('file.txt')
print(totalWord)
