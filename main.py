from PackageLoader import packageReader
from HashMap import HashMap
from AddressDistanceLoader import distanceList, addressList, distanceToAddress

# Load data and populate the hashmap
file = 'WGUPS Package File.csv'
PackageInfo = packageReader(file)
hashMap = HashMap(PackageInfo)
    
               


