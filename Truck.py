import math
from AddressDistanceLoader import distanceToAddress, distanceList, addressList
from Package import Package

class Truck:
    def __init__(self, packagesInLoad: list):
        self.packagesInLoad = packagesInLoad
        self.reciept = packagesInLoad
        self.milesDriven = 0
        self.currentLocation = addressList[0]
        #self.currentTime = currentTime
        #Set's the status to en route once loaded into truck
        for package in self.packagesInLoad:
            package.status = "en route"

    def startDelivery(self):
   
        # unvisited is a list of places where we need to drop off packages
        unvisited = []
        for package in self.packagesInLoad:
            unvisited.append(package.getAddress())

        # Loop through unvisited places as long as it's not empty
        while unvisited:
            min_distance = float('inf')
            nearestStreet = None

            for address in unvisited:
                distance = distanceToAddress(self.currentLocation, address)
                if distance < min_distance:
                    min_distance = distance
                    nearestStreet = address
                     # Increase miles driven

            #Update current location, unvisited list, and miles driven
            self.currentLocation = nearestStreet
            unvisited.remove(nearestStreet)
            self.milesDriven += min_distance

            # Drop off packages
            for package in self.packagesInLoad:
                if package.getAddress() == self.currentLocation:
                    package.status = "delivered"
                    self.packagesInLoad.remove(package)  # Remove package from not delivered list
            
        #Go back home
        home = addressList[0]
        backHome = distanceToAddress(self.currentLocation, home)
        self.currentLocation = home
        self.milesDriven += backHome
         
        print(f"Total mile driven: {self.milesDriven}")