import pandas as pd
from master import masterU

file2 = open('newNamesMod.txt', 'w')

schoolDemo = []

file2.writelines("[\n")

for x in masterU:

    print ("SCHOOL: " + x)

    currentList = []

    if (x == "IuB" or x == "UCL" or x == "UCLA" or x == "UCSD" or x == "ethZurich" or x == "files" or x == "kuLeuven" or x == "uWashington" or x == "warwick"):
        #print (x)
        str = '(\"' + x + '\", \"' + x + '\"),\n'
        #file2.writelines(str)

    else:
        pubFile = '../../../drive/' + x + '.xls'

        paperData = pd.read_excel(pubFile, usecols="W")

        #print(paperData)

        for index, row in paperData.iterrows():

            address = row['Addresses']

        #rowX = paperData.iloc[0]

        #address = rowX.loc['Addresses']

            indexStart = address.find(']')
            indexEnd = address.find(',', indexStart)

            schoolNameSub = address[(indexStart+2):indexEnd]

            if schoolNameSub not in currentList:
                #string = '(\"' + x + '\", \"' + currentList + '\"),\n'
                currentList.append(schoolNameSub)
                str = schoolNameSub

            #str = '(\"' + x + '\", \"' + schoolNameSub + '\"),\n'

        file2.write('(\"' + x + '\", [')
        varBool = True

        for all in currentList:
            if (varBool == False):
                file2.write(', ')
                file2.write('\"' + all + '\"')
            else:
                file2.write('\"' + all + '\"')
                varBool = False

        file2.write(']), \n')
        #str = '(\"' + x + '\", ' + currentList + '),\n'

            #print (str)

        #file2.writelines(str)

        #print ("SCHOOL: " + x + " DATA: " + rowX.loc['Addresses'])
        print (str)


file2.writelines("]")
file2.close()


'''
    paperData = pd.read_excel(pubFile, usecols="W")

    for index, row in paperData.iterrows():
        #find first author name
        print (row['Addresses'])

        address = row['Addresses']
        print ("SCHOOL: " + x + address)
        indexStart = address.find(']')
        index = address.find(',', indexStart)

        schoolNameSub = address[indexStart:index]

        print (schoolNameSub)
    '''
