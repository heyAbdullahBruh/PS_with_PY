# Problem0-32 ---> Make a Inventory Manager Class ---> 
# 3 key method add --> Add product, remove product, update stock

class Product :
    products=[]
    def __init__(self,id='',pname='',price=0,rating=float(0)):
        create ={
            "id":id,
            "pname":pname,
            "price":price,
            "rating":rating,
        }
        self.products.append(create)
        
    def addProduct(self,id,pname,price,rating):
        newP ={
            "id":id,
            "pname":pname,
            "price":price,
            "rating":rating,
        }
        self.products.append(newP)
        return { "message":'New Product Added Successfully',"products":self.products }
    
    def updateProduct(self,id='',pname='',price='',rating=''):
        try :
            product=next(p for p in self.products if p["id"]==id)
            product["pname"] = pname if pname is not '' else product["pname"]
            product["price"] = price if price is not '' else product["price"]
            product["rating"] = rating if rating is not '' else  product["rating"]
            return { "message":'Product Updated Successfully',"products":self.products }
        except StopIteration:
            return {"error": "Product not found"}
    
    def removeProduct(self,id=''):
        try :
            self.products = [p for p in self.products if p["id"]!=id]
            return { "message":'Product Remove Successfully',"products":self.products}
        except StopIteration: 
             return {"error": "Product not found"}
    def getProducts(self):
        return {"products":self.products }
    def getSingleProducts(self,id):
        product =next(p for p in self.products if p['id']==id)
        return {"product": product }

product1=Product('12312412','Apple',40,4.5)
print(product1.getProducts()['products'][0]["pname"])#Apple
msg=product1.addProduct('12312413','mango',30,4.3)
print(msg['message'])# New Product Added Successfully

print(product1.getProducts()['products'][1]["pname"])#mango
product1.addProduct('12312143','Potato',20,4.7)

removeMsg = product1.removeProduct("12312413")

print(removeMsg) #{'message': 'Product Remove Successfully', 'products': [{'id': '12312412', 'pname': 'Apple', 'price': 40, 'rating': 4.5}, {'id': '12312143', 'pname': 'Potato', 'price': 20, 'rating': 4.7}]}

print(product1.getProducts())#{'products': [{'id': '12312412', 'pname': 'Apple', 'price': 40, 'rating': 4.5}, {'id': '12312143', 'pname': 'Potato', 'price': 20, 'rating': 4.7}]}

upMsg = product1.updateProduct('12312413','Mangose')
print(upMsg) #{'error': 'Product not found'}

upMsg2 = product1.updateProduct('12312412','Aplle')
print(upMsg2) #{'message': 'Product Updated Successfully', 'products': [{'id': '12312412', 'pname': 'Aplle', 'price': 40, 'rating': 4.5}, {'id': '12312143', 'pname': 'Potato', 'price': 20, 'rating': 4.7}]}

print(product1.getSingleProducts('12312143')) #{'product': {'id': '12312143', 'pname': 'Potato', 'price': 20, 'rating': 4.7}}
