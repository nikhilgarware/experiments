def isOdd(input):
    return input * 3 + 1


def isEven(input):
    return input / 2


for i in range(20):
    data = 7
    if(data % 2 == 0):
        isEven(data)
    isOdd(data)
