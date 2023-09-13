from decimal import Decimal

myFile = open('posiciones.csv')
text = myFile.readline()
while text != "end":
    numbers = text.split(',')
    x = Decimal(numbers[0])
    y = Decimal(numbers[1])
    z = Decimal(numbers[2])
    print(x)
    print(y)
    print(z)
    #print("X = " + x + ", Y = " + y + ", Z = " + z)
    text = myFile.readline()
myFile.close()