from PackageLoader import packageReader
from HashMap import HashMap
from AddressDistanceLoader import distanceList, addressList, distanceToAddress
from Truck import Truck
from Package import Package

# Load data and populate the hashmap
file = 'WGUPS Package File.csv'
PackageInfo = packageReader(file)
hashMap = HashMap(PackageInfo)

#Create 3 trucks with packages loaded
truck1 = Truck ([PackageInfo[0], PackageInfo[12], PackageInfo[13], PackageInfo[14], PackageInfo[15], PackageInfo[19], PackageInfo[28], PackageInfo[29], PackageInfo[30], PackageInfo[33], PackageInfo[36], PackageInfo[39]])
truck2 = Truck ([PackageInfo[2], PackageInfo[5], PackageInfo[11], PackageInfo[16], PackageInfo[17], PackageInfo[18], PackageInfo[20], PackageInfo[21], PackageInfo[22], PackageInfo[23], PackageInfo[25], PackageInfo[26], PackageInfo[34], PackageInfo[35], PackageInfo[37], PackageInfo[38]])
truck3 = Truck ([PackageInfo[1], PackageInfo[3], PackageInfo[4], PackageInfo[5], PackageInfo[6], PackageInfo[7], PackageInfo[8], PackageInfo[9], PackageInfo[10], PackageInfo[24], PackageInfo[27], PackageInfo[31], PackageInfo[32]])
#Start delivery
truck1.startDelivery()
truck2.startDelivery()
truck3.startDelivery()

print(hashMap.get_all_Packages())
print(f"Total miles driven of all trucks: {truck1.milesDriven + truck2.milesDriven + truck3.milesDriven}")