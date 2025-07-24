#Problem-24 ---> Merge Two Text Files Line by Line

file1 = open('file1.txt','r')
file2 = open('file2.txt','r')
mergeF=open('mergeF.txt',"a")

textLists=[]
for l in file1:
    textLists.append(l)
for l in file2:
    textLists.append(l)
for l in textLists:
    mergeF.write(f'{l}\n')
print('done')