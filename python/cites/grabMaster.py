import pandas as pd
from master import masterU

file2 = open('newNames.txt', 'w')

schoolDemo = []

file2.writelines("[\n")

for x in masterU:

    if (x == "IuB" or x == "UCL" or x == "UCLA" or x == "UCSD" or x == "ethZurich" or x == "files" or x == "kuLeuven" or x == "uWashington" or x == "warwick"):
        print (x)
        str = '(\"' + x + '\", \"' + x + '\"),\n'
        file2.writelines(str)

    else:
        pubFile = '../../../drive/' + x + '.xls'

        paperData = pd.read_excel(pubFile, usecols="W")

        rowX = paperData.iloc[0]

        address = rowX.loc['Addresses']

        indexStart = address.find(']')
        index = address.find(',', indexStart)

        schoolNameSub = address[(indexStart+2):index]

        str = '(\"' + x + '\", \"' + schoolNameSub + '\"),\n'

        print (str)

        file2.writelines(str)

        #print ("SCHOOL: " + x + " DATA: " + rowX.loc['Addresses'])



file2.writelines("]")
#file1.close()
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
