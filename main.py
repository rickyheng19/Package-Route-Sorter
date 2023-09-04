# Name: Kenna Heng
# Student ID: 011050292 
# Class: C950
from PackageLoader import packageReader
from HashMap import HashMap
from AddressDistanceLoader import distanceList, addressList, distanceToAddress
from Truck import Truck
from Package import Package
import datetime

# Load data and populate the hashmap
file = 'WGUPS Package File.csv'
PackageInfo = packageReader(file)
hashMap = HashMap(PackageInfo)

#Opening message
print("WGU Parcel Service")

#Time where route is finished
userTime = datetime.timedelta(hours=13, minutes=12)
#Create 3 trucks with packages loaded
truck1 = Truck ([PackageInfo[0], PackageInfo[12], PackageInfo[13], PackageInfo[14], PackageInfo[15], PackageInfo[18], PackageInfo[19], PackageInfo[29], PackageInfo[30], PackageInfo[33], PackageInfo[36], PackageInfo[39]], datetime.timedelta(hours=8), userTime)
truck2 = Truck ([PackageInfo[2], PackageInfo[8], PackageInfo[11], PackageInfo[16], PackageInfo[17], PackageInfo[28], PackageInfo[20], PackageInfo[21], PackageInfo[22], PackageInfo[23], PackageInfo[25], PackageInfo[26], PackageInfo[34], PackageInfo[35], PackageInfo[37], PackageInfo[38]], datetime.timedelta(hours=10, minutes=20), userTime)
truck3 = Truck ([PackageInfo[1], PackageInfo[3], PackageInfo[4], PackageInfo[5], PackageInfo[6], PackageInfo[7], PackageInfo[9], PackageInfo[10], PackageInfo[24], PackageInfo[27], PackageInfo[31], PackageInfo[32]], datetime.timedelta(hours=9, minutes=5), userTime)

#Start Truck 1
if truck1.currentTime < userTime:
    print("Truck 1:")
    truck1.startDelivery()

#Start truck 2 at this time
if truck2.currentTime < userTime:
    print("Truck 2:")
    truck2.startDelivery()
    #Change package info for package 9:
    PackageInfo[8].address = "410 S State St"
    PackageInfo[8].zip_code = "84111"

#Start truck 3 when either truck 1 or 2 make it back to base
if truck1.backHomeStatus == True:
    truck3.currentTime = truck1.endTime
    if truck3.currentTime < userTime: # type: ignore
        print("Truck 3:")
        truck3.startDelivery()
elif truck2.backHomeStatus == True:
    truck3.currentTime = truck2.endTime
    if truck3.currentTime < userTime: # type: ignore
        print("Truck 3:")
        truck3.startDelivery()

#Output the total miles driven
print(f"Total miles driven of all trucks: {round(truck1.milesDriven + truck2.milesDriven + truck3.milesDriven, 2)} miles")

#Input time to see status of package
try:
    # Input time to see status of package
    userInput = input("Please enter a time to check the status of package(s). Please use HH:MM military time format. Invalid entry will exit program: ")
    (h, m) = userInput.split(":")
    userTimeInput = datetime.timedelta(hours=int(h), minutes=int(m))

    #Package 9 address is different depending on time
    if userTimeInput < datetime.timedelta(hours=10, minutes=20):
        PackageInfo[8].address = "300 State St"
        PackageInfo[8].zip_code = "84103"

    #Update all packages with status of inputted time
    for i in range(len(PackageInfo)):
        PackageInfo[i].updateStatus(userTimeInput)

# Ask to see status of single or all packages
    userInputSingleOrAll = input("If you would like to see the status of one package, please enter 'single', or enter 'all'. Invalid entry will exit program: ")
    if userInputSingleOrAll == "all":
        for i in range(len(PackageInfo)):
            print(PackageInfo[i].packageInfo())
    elif userInputSingleOrAll == "single":
        userSingleLookUp = int(input("Enter package ID: ")) - 1
        print(PackageInfo[userSingleLookUp].packageInfo())
    else:
        print("Invalid input. Please enter 'single' or 'all'.")
except ValueError as e:
    print("Invalid input format. Please use HH:MM military time format for time input.")

print("Exiting program...")





