class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    def getCity(self):
        return self.__city

    def getStreet(self):
        return self.__street

    def getNumber(self):
        return self.__number


addr1 = Address(city="Sofia", street="Gotse Delchev", number=1)

print("city " + addr1.getCity())
print("street " + addr1.getStreet())
print("number " + str(addr1.getNumber()))

addr1._Address__city = "Varna"
print("city " + addr1.getCity())
