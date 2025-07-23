# Problem-20 --->Print Number in Words
# Like -->  123 -> Output: "One Two Three"
wordNums={1:"One",2:"two",3:"Three",4:"four",5:"five",6:"six",7:"Seven",8:"Eight",9:"Nine",0:"Zero",}

def NumToWord(num):
    result = ""
    for n in str(num):
        result+=wordNums.get(int(n))+' '
    return result
print(NumToWord(13021241))#One Three Zero two One two four One 
