from decimal import Decimal

myFile = open('posiciones.csv')
text = myFile.readline()
while text != "end":
    numbers = text.split(',')
    x = Decimal(numbers[0])
    y = Decimal(numbers[1])
    z = Decimal(numbers[2])

    x2 = x**2
    y2 = pow(y, 2)
    z2 = pow(x, 2)
    print(x2)
    print(y2)
    print(z2)

    text = myFile.readline()
myFile.close()