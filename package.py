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
        self.status = status

    #Print info about package
    def packageInfo(self):
        print(f"ID: {self.package_id}, Address: {self.address}, {self.city} {self.state} {self.zip_code}. Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}")

    #Return an address from list of addresses
    def getAddress(self):
        for row in range(len(addressList)):
            if self.address == addressList[row]:
                return addressList[row]