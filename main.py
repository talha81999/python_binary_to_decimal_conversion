
binaryNumber = input("Enter Binary Value: ")
newList = []
power = 0
for i in range(len(binaryNumber) - 1, -1, -1):
    temp = 2 ** power
    newTemp = int(binaryNumber[i]) * temp
    newList.insert(0, int(newTemp))
    power += 1

decimalValue = sum(newList)
print(f"A Binary base number \"{binaryNumber}\" is equivalent to \"{decimalValue}\" in Base Decimal ")


