# Remove Duplicates from a List
# Input: [1,2,2,3,4,4,5] → Output: [1,2,3,4,5]

def cutDuplicates(numsList) :
    pureList =[]
    for n in numsList :
        if n not in pureList :
            pureList.append(n) 
    print(pureList)
    
dups1= [1,2,3,5,2,8,3,9,1,4,5]    
dups2= [11,23,34,5,22,8,23,9,1,34,5] 
dups3= ['Sabed',"Naved","Javed","Sabed",'Naved',"Khabed","Javed"] 

cutDuplicates(dups1) #[1, 2, 3, 5, 8, 9, 4]
cutDuplicates(dups2)#[11, 23, 34, 5, 22, 8, 9, 1]
cutDuplicates(dups3)#['Sabed', 'Naved', 'Javed', 'Khabed']
