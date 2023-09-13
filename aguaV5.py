from decimal import Decimal
import math

myFile = open('posiciones-xyz-agua.csv')
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
    r = math.sqrt(plus)
    print(r)

    text = myFile.readline()
myFile.close()