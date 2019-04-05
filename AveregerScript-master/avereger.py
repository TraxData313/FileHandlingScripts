



###############################
# - Set the fileToAverage name:
fileToAverage = "SetTheFileName.txt"
###############################




entriesToAverage = input("How much entries to average [int]?")
outputFile = "ave_" + str(entriesToAverage) + "_" + fileToAverage
current_list = open(fileToAverage, 'r').readlines()
output_list = []

print
print
print
print "Input file:", fileToAverage
print "Averaging input file with lenght", len(current_list), "..."

i=0
while i < len(current_list):
    j=0
    temp_sum = 0
    while j < entriesToAverage:
        try:
            current_element = float(current_list[i+j].split()[0])
        except:
            pass
        temp_sum += current_element
        j+=1
    entry = temp_sum / float(entriesToAverage)
    output_list.append(entry)
    i+=entriesToAverage


print "Output file lenght:", len(output_list)
print "Saving to file:", outputFile

saveFile = open(outputFile, 'w')
i=0
while i < len(output_list):
    saveFile.write(str(output_list[i]))
    saveFile.write('000')
    saveFile.write('\n')
    i+=1
saveFile.close()

print "- Done!"
print