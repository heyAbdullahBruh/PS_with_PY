#Problem-23 ---> Read File and count word



def fileWordCount(filename):
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
    return wordCount

totalWord =fileWordCount('file.txt')
print(totalWord)
