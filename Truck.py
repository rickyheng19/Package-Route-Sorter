import datetime
import math
from AddressDistanceLoader import distanceToAddress, distanceList, addressList
from Package import Package

class Truck:
    def __init__(self, packagesInLoad: list, currentTime, userTime):
        self.packagesInLoad = packagesInLoad
        self.reciept = packagesInLoad
        self.milesDriven = 0
        self.currentLocation = addressList[0]
        self.currentTime = currentTime
        self.endTime = None
        self.backHomeStatus = False
        self.userTime = userTime

    #Time complexity of this method is O(n^2)
    def startDelivery(self):
        
        #Mark all packages in load enroute time, O(n)
        for package in self.packagesInLoad:
            package.enrouteTime = self.currentTime

        # unvisited is a list of places where we need to drop off packages, O(n)
        unvisited = []
        for package in self.packagesInLoad:
            unvisited.append(package.getAddress())

        # Using nearest neighbor greedy algorithm, we visit the closest location from our current location
        # Loop through unvisited places as long as it's not empty, O(n^2) due to there being another for loop
        # In the distanceToAddress method which also has a for loop.
        while unvisited:
            min_distance = float('inf')
            nearestStreet = None

            #O(n), but since distanceTo address is also O(n), makes this method O(n^2)
            for address in unvisited:
                #O(n)
                distance = distanceToAddress(self.currentLocation, address)
                if distance < min_distance:
                    min_distance = distance
                    nearestStreet = address
                    

            #Update current location, unvisited list, and miles driven
            self.currentLocation = nearestStreet
            unvisited.remove(nearestStreet)
            self.milesDriven += min_distance
            self.currentTime += datetime.timedelta(hours=min_distance / 18) 
            # Drop off packages if they match our current location
            for package in self.packagesInLoad:
                if package.getAddress() == self.currentLocation:
                    package.deliveryTime = self.currentTime
                    self.packagesInLoad.remove(package)  # Remove package from list
                   
        #Go back home once load is empty
        if len(self.packagesInLoad) == 0:
            home = addressList[0]
            backHome = distanceToAddress(self.currentLocation, home)
            self.currentLocation = home
            self.milesDriven += backHome
            self.endTime = self.currentTime + datetime.timedelta(hours=backHome / 18)
            self.backHomeStatus = True