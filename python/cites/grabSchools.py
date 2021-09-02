file1 = open('../../files.txt', 'r')
file2 = open('newFiles.txt', 'w')
Lines = file1.readlines()

count = 0

for line in Lines:
    test = line.find('-cite')
    if (test>0):
        count = count +1
    else:
        #line.removesuffix('.xls')
        #if line.endswith('.xls'):
        line = line[:-5]
        print (line)
        lineU = '\"' + line + '\",\n'
        file2.writelines(lineU)

file1.close()
file2.close()
