# problem-17----> Remove punctuation from String---->


punc =['.',',','?','!',"’"]

# way --1
def removePunc (text):
    text2List=[l for l in text]
    for l in text2List :
        if l in punc:
            text2List.remove(l)

    print(''.join(text2List))

#way --2---> 
def removePunc (text):
    text2List=[l for l in text if l not in punc]
    print(''.join(text2List))
removePunc('Hello!!! What’s up??? ???? How are you .')
removePunc('Hello!!! What’s up??? ? How are you .')