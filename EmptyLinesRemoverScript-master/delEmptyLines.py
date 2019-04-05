
################
# - File to fix:
fileName = "testFile.txt"
################




list = open(fileName, 'r').readlines()
lenght = len(list)


cp = 0.0
i=0
element = 0
while i < lenght:
    string = list[element]
    if len(string) == 1:
        print "Deleting:", element
        del list[element]
        element = element - 1
    i+=1
    element += 1
    
    
lenght = len(list)
saveFile = open(fileName, 'w')
i=0
while i < lenght:
    saveFile.write(str(list[i]))
    i+=1
    
saveFile.close()






























