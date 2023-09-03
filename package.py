import datetime
from AddressDistanceLoader import addressList

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = "At Hub"
        self.hubTime = datetime.timedelta(hours=8)
        self.enrouteTime = None
        self.deliveryTime = None

    #Print info about package
    def packageInfo(self):
        if self.status == "At Hub":
            return f"ID: {self.package_id}, Address: {self.address}, {self.city} {self.state} {self.zip_code}. Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status} @{self.hubTime}"
        elif self.status == "En route":
            return f"ID: {self.package_id}, Address: {self.address}, {self.city} {self.state} {self.zip_code}. Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status} @{self.enrouteTime}"
        elif self.status == "Delivered":
            return f"ID: {self.package_id}, Address: {self.address}, {self.city} {self.state} {self.zip_code}. Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status} @{self.deliveryTime}"




    #Return an address from list of addresses
    def getAddress(self):
        for row in range(len(addressList)):
            if self.address == addressList[row]:
                return addressList[row]
            
    def updateStatus(self, userTime):
        if self.deliveryTime is None:
            pass
        elif self.deliveryTime < userTime:
            self.status = "Delivered"
        elif self.enrouteTime < userTime:
            self.status = "En route"
        else:
            self.status = "At Hub"