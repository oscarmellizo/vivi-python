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
    z2 = pow(z, 2)
    
    plus = x2 + y2 + z2
    print(plus)

    text = myFile.readline()
myFile.close()