myFile = open('posiciones.csv')
text = myFile.readline()
while text != "end":
    print(text)
    text = myFile.readline()
myFile.close()
