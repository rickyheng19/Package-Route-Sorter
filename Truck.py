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

    def startDelivery(self):
        
        #Mark all packages in load enroute time
        
        for package in self.packagesInLoad:
            package.enrouteTime = self.currentTime
            #package.status = "En route"

        #Introductions
        startTime = self.currentTime
        print(f"Start Time: {startTime}")
   
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
                    

            #Update current location, unvisited list, and miles driven
            self.currentLocation = nearestStreet
            unvisited.remove(nearestStreet)
            self.milesDriven += min_distance
            self.currentTime += datetime.timedelta(hours=min_distance / 18) 
            # Drop off packages
            for package in self.packagesInLoad:
                if package.getAddress() == self.currentLocation:
                    package.deliveryTime = self.currentTime
                    self.packagesInLoad.remove(package)  # Remove package from not delivered list
            #if self.currentTime > self.userTime:
                #break
            
                   
        #Go back home
        if len(self.packagesInLoad) == 0:
            home = addressList[0]
            backHome = distanceToAddress(self.currentLocation, home)
            self.currentLocation = home
            self.milesDriven += backHome
            self.endTime = self.currentTime + datetime.timedelta(hours=backHome / 18)
            self.backHomeStatus = True
            
            print(f"Total miles driven: {self.milesDriven} miles")
            print(f"End Time: {self.endTime}")
            totalTime = self.endTime - startTime
            print(f"Total Time taken: {totalTime}")