import csv

#List for addresses O(1)
addressList = []

addressFile = 'WGUPS Address Table.csv'

#Reader for addresses O(n)
with open(addressFile, 'r') as addressCSV:
    addressReader = csv.reader(addressCSV)

    #Skip first row
    next(addressReader)

    for row in addressReader:
        addressList.append(row[0])

#List for distances between addresses O(1)
distanceList = []

distanceFile = 'WGUPS Distance Table.csv'

#Reader for distances O(n)
with open(distanceFile, 'r') as distanceCSV:
    distanceReader = csv.reader(distanceCSV)

    #Skip first row
    next(distanceReader)

    for row in distanceReader:
        distanceList.append(row)

#Method to determine distance between two addresses. Uses two indexes to get a value in a
#Triangular array. O(n)
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

    #Return a float value
    fltDistance = float(distance)

    return fltDistance



