arr = []
def lmultiple(num,length):
    for i in range (1,(length+1)):
        arrn = i * num
        arr.append(arrn)
    print (arr)



num = int(input("whats your multiple number"))
length = int(input("what length do u want"))
print (lmultiple(num,length))

