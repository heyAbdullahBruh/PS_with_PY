#Problem-29 ---> Reverse Contents of File (line-wise)



def reversedContentInFile(filename):
    # read file --->
    readFTxt =open(filename, 'r')
    fileData = readFTxt.read()
    txtToList = fileData.split('\n')
    reversedData=[d.strip()[::-1] for d in txtToList]
    
    # now write file --->
    writeF =open(filename, 'a')
    
    for nd in reversedData:
        writeF.write(f'{nd}\n\n')
    print('Done')
    

reversedContentInFile('file.txt')
