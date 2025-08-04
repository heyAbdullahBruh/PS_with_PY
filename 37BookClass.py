#Problem -37, Make A book managed system With python class -->

class Book : 
    def __init__(self,bname=str,author=str,price=int):
        self.bname=bname
        self.author=author
        self.price=price
    def discount (self,percent=float):
        cutPrice = self.price * (percent/100)
        self.price=self.price - cutPrice 
    def bookInfo (self):
        return {"name":self.bname,"Price":self.price,"Author":self.author}


book1 = Book('Sell Like Crazy','Sarbi Surbi',500)
print(book1.bookInfo())# {'name': 'Sell Like Crazy', 'Price': 500, 'Author': 'Sarbi Surbi'}
book1.discount(13.5)
print(book1.bookInfo()) # {'name': 'Sell Like Crazy', 'Price': 432.5, 'Author': 'Sarbi Surbi'}

