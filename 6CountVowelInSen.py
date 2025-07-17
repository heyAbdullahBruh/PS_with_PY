#Problem -6 ---> Count Vowels in a Sentence
# Input: "I love Python" → Output: 4


vowels =['a','e','i','o','u']

sentence =input('Enter a sentence for count vowels : ')
vCount=0
w=0 
while w <len(sentence) :
    if sentence[w] in vowels :
        vCount=vCount+1
    w=w+1
print(vCount)            

# vowels ->2
# Lorem -> 2
# Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui laboriosam eius vero. Deleniti vitae placeat, repellat nulla iusto harum repellendus id? Doloremque dicta veritatis dolor libero quis ea, molestias alias. -> 84

