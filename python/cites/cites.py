import pandas as pd
from pprint import pprint
from schools import schoolList

for x in schoolList:

    schoolFileName = x[0]
    substringTuple = x[1]
    schoolName = x[1][0]

    pubFile = '../../../drive/' + schoolFileName + '.xls'
    citeFile = '../../../drive/' + schoolFileName + '-cite.xls'

    #pubData = pd.read_excel(pubFile, index_col=0)
    #hData = pd.read_excel(citeFile, index_col=0)

    paperData = pd.read_excel(pubFile, usecols="B, I, W")
    citeData = pd.read_excel(citeFile, usecols="A, T", header=10)

    articleTitles = []
    authorAddress = []
    totalPubs = 0
    totalCites = 0

    for index, row in paperData.iterrows():
        #find first author name

        breaker = False

        authorNames = row['Authors']
        anIndex = authorNames.find(',')
        authorNameSub = authorNames[0:(anIndex)]

        address = row['Addresses']
        indexStart = address.find(authorNameSub)
        index = address.find(']', indexStart)
        for nameList in substringTuple:
            if breaker == False:
                schoolIndex = address.find(nameList)

                if ((index+2) == schoolIndex):
                    articleTitles.append(row['Article Title'])
                    authorAddress.append(row['Addresses'])
                    breaker = True
        #print(row['Article Title'])
        #print ("x")

    totalPubs = len(articleTitles)

    for index, row in citeData.iterrows():
        checkCite = row['Title']
        if checkCite in articleTitles:
            numCites = row['Total Citations']
            numCite = int(numCites)
            totalCites = totalCites + numCite

    #print(citeData.head())
    print (schoolName + " papers: " + str(totalPubs))
    print(schoolName + " cites: " + str(totalCites))
    #print(paperData.head(entries))
    #pprint(articleTitles[0])
    #pprint (authorAddress[0])
