#Your task is to make a function that can take any non-negative integer as a argument 
#and return it with its digits in descending order. 
#Essentially, rearrange the digits to create the highest possible number.

#Examples:
#Input: 21445 Output: 54421

#Input: 145263 Output: 654321

#Input: 1254859723 Output: 9875543221

def Descending_Order(num):
    temp = [int(i) for i in str(num)]
    temp.sort(reverse=True)
    temp = ''.join(str(e) for e in temp)
    return int(temp)