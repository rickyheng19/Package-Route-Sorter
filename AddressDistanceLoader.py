import csv

#List for addresses
addressList = []

addressFile = 'WGUPS Address Table.csv'

#Reader for addresses
with open(addressFile, 'r') as addressCSV:
    addressReader = csv.reader(addressCSV)

    next(addressReader)

    for row in addressReader:
        addressList.append(row[0])

#List for distances
distanceList = []

distanceFile = 'WGUPS Distance Table.csv'

#Reader for distances
with open(distanceFile, 'r') as distanceCSV:
    distanceReader = csv.reader(distanceCSV)

    next(distanceReader)

    for row in distanceReader:
        distanceList.append(row)

def distanceToAddress(address1, address2):
    
    indexAddress1 = 0
    indexAddress2 = 0

    #get the indexes for both addresses
    for i in range(len(addressList)):
        if address1 == addressList[i]:
            indexAddress1 = i
    for j in range(len(addressList)):
        if address2 == addressList[j]:
            indexAddress2 = j
    
    #Sets the distance using indexs in distanceList
    distance = distanceList[indexAddress1][indexAddress2] 

    #Since it's a triangle array, will switch indexes if = ""
    if distance == "":
        distance = distanceList[indexAddress2][indexAddress1]

    return distance



