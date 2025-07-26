# Problem -34 ---> Create a Library Management Project -->
# Borrow Book, Return Book, Available Books

class Library :
    books = []
    
    def __init__(self,bId=str,b_name=str,BorrowBook=int,ReturnBook=int,AvailableBooks=int):
        newBooks ={
            "bId":bId,
            "b_name":b_name,
            "BorrowBook":BorrowBook,
            "ReturnBook":ReturnBook,
            "AvailableBooks":AvailableBooks,
        }
        self.books.append(newBooks)

    def BorrowBook (self,bId=str,pices=int):
        try:
            book = next(b for b in self.books if b['bId']==bId)
            
            if pices > book['AvailableBooks']:
                return f"We have just only {book['AvailableBooks']} pices book"
            
            book['BorrowBook']=pices
            book['AvailableBooks']=book['AvailableBooks']-pices
        except StopIteration:
            return {"error":"This Book Are not available right now"}
        
    def ReturnBook (self,bId=str,pices=int):
        try:
            book = next(b for b in self.books if b['bId']==bId)
            if pices > book['BorrowBook']:
                return
            book['ReturnBook']=pices
            book['BorrowBook']=book['BorrowBook']-pices
            book['AvailableBooks']=book['AvailableBooks']+pices
        except StopIteration:
            return {"error":"This Book Are not available right now"}
        
    def AvailableBooks (self,bId=str):
        try:
            book = next(b for b in self.books if b['bId']==bId)
            return f"{book['b_name']} book have only {book['AvailableBooks']} pices. This book reader borrowed {book['BorrowBook']} pices"
        except StopIteration:
            return {"error":"This Book Are not available right now"}
