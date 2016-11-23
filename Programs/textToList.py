strList = input("Enter string in list format to be converted into list: ")
strList = strList[1:-1]
for x in strList:
	if x == ",":
		strList = strList.replace(x, '')
	if x == "'":
		strList = strList.replace(x, '')
	list = strList.split(" ")
print(list)