myFile = open('posiciones.csv')
text = myFile.readline()
while text != "end":
    numbers = text.split(',')
    x = numbers[0]
    y = numbers[1]
    z = numbers[2]
    print(x)
    print(y)
    print(z)
    #print("X = " + x + ", Y = " + y + ", Z = " + z)
    text = myFile.readline()
myFile.close()