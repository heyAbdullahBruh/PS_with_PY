# Problem-10 ---> Make a word counter --> 


text = "python is easy and python is fun"

def wordCountChecker (sentence):
    wordsCount ={}
    textToList = sentence.split(" ")
    
    w=0
    while w< len(textToList):
        if w==" ":
            return
        if wordsCount.get(textToList[w]) :
            wordsCount[f"{textToList[w]}"] = wordsCount.get(textToList[w])+1
        if wordsCount.get(textToList[w]) ==None :
            wordsCount[f"{textToList[w]}"] = 1
        w=w+1
    print(wordsCount)

wordCountChecker(text) #{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'fun': 1}   
wordCountChecker("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Laudantium voluptas nisi cumque sed expedita eligendi voluptates nostrum? Autem sapiente maxime dolorem earum! Cum laboriosam aliquid tempora itaque aspernatur necessitatibus debitis dicta, maiores nisi perferendis quaerat eligendi corporis veniam quas nobis fugit sed quisquam quia velit dignissimos ipsam non voluptatum! Soluta quidem qui dolor nihil veritatis maiores at inventore aliquid voluptas possimus. Deserunt illo voluptate explicabo soluta doloribus saepe cumque rem possimus corporis, sit nostrum delectus nisi excepturi itaque rerum odit quas labore laboriosam fuga distinctio? Maiores repudiandae vel blanditiis minus modi inventore unde ipsum excepturi nam eos ipsa, eum atque?") 
#{'Lorem': 1, 'ipsum': 2, 'dolor': 2, 'sit,': 1, 'amet': 1, 'consectetur': 1, 'adipisicing': 1, 'elit.': 1, 'Laudantium': 1, 'voluptas': 2, 'nisi': 3, 'cumque': 2, 'sed': 2, 'expedita': 1, 'eligendi': 2, 'voluptates': 1, 'nostrum?': 1, 'Autem': 1, 'sapiente': 1, 'maxime': 1, 'dolorem': 1, 'earum!': 1, 'Cum': 1, 'laboriosam': 2, 'aliquid': 2, 'tempora': 1, 'itaque': 2, 'aspernatur': 1, 'necessitatibus': 1, 'debitis': 1, 'dicta,': 1, 'maiores': 2, 'perferendis': 1, 'quaerat': 1, 'corporis': 1, 'veniam': 1, 'quas': 2, 'nobis': 1, 'fugit': 1, 'quisquam': 1, 'quia': 1, 'velit': 1, 'dignissimos': 1, 'ipsam': 1, 'non': 1, 'voluptatum!': 1, 'Soluta': 1, 'quidem': 1, 'qui': 1, 'nihil': 1, 'veritatis': 1, 'at': 1, 'inventore': 2, 'possimus.': 1, 'Deserunt': 1, 'illo': 1, 'voluptate': 1, 'explicabo': 1, 'soluta': 1, 'doloribus': 1, 'saepe': 1, 'rem': 1, 'possimus': 1, 'corporis,': 1, 'sit': 1, 'nostrum': 1, 'delectus': 1, 'excepturi': 2, 'rerum': 1, 'odit': 1, 'labore': 1, 'fuga': 1, 'distinctio?': 1, 'Maiores': 1, 'repudiandae': 1, 'vel': 1, 'blanditiis': 1, 'minus': 1, 'modi': 1, 'unde': 1, 'nam': 1, 'eos': 1, 'ipsa,': 1, 'eum': 1, 'atque?': 1