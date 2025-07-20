# Problem-15 ---> find Anagrams in list 
#An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
# "listen" --> "silent"
# "evil" --> "vile"
# "angel" --> "glean"
# "rail safety" --> "fairy tales

randWords =['listen','evil','silent','text','extt',"vile"]
 
# anagrams.va 
def anagramsVal (strList):
    result = {}
    
    for w in strList :
        sortedWord = ''.join(sorted(w))

        if sortedWord in result :
            result[sortedWord].append(w)
        else : 
            result[sortedWord] =[w]
    return list(result.values())

print(anagramsVal(randWords)) #[['listen', 'silent'], ['evil', 'vile'], ['text', 'extt']]
