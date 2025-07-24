#Problem-26 ---> Search for a Word in a File and Print Line Numbers



def findWordLineNumformFile(filename,word):
    fileTxt =open(filename, "r")
    fileData = fileTxt.read()
    txtToList = fileData.split('\n')
    lineNumb=0
    for l in txtToList:
        if word in l :
              lineNumb=txtToList.index(l)+1
    return lineNumb
   
print(findWordLineNumformFile('file.txt',"blanditiis")) # 6
print(findWordLineNumformFile('file.txt',"expedita")) # 2
print(findWordLineNumformFile('file.txt',"nostrum")) # 5

