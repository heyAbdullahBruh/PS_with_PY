# Problem-21 ---> Binary To decimal and Decimal To Binary

def DecToBin (n):
    res=[]
    while n > 0:
        res.append(str(n % 2))  # store remainder
        n = n // 2

    if len(res) < 4 :
        for a in range(0,4-len(res)):
            res.append('0')
    return list(reversed(res))

print(DecToBin(1000))#['1', '1', '1', '1', '1', '0', '1', '0', '0', '0']

def BinToDec (bin):
    decNum =0
    for b in bin :
        decNum = decNum*2 + int(b)
    return decNum

print(BinToDec(DecToBin(10000)))#10000
