# Problem -41 ---> simple Passsword Validator--->
# At least 8 chars
# 1 uppercase, 1 lowercase, 1 digit


import re


def checkPassValid (passInp):
    pattern = r"\b[a-zA-Z0-9]{8}\b"
    result =re.match(pattern,passInp)
    if result :
       print('Password Is valid')
    else : 
       print('Password Is invalid')

checkPassValid('12jsjAdj') #Password Is valid
checkPassValid('12jsjAd') #Password Is invalid