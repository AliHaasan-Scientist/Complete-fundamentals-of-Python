# Class 1
class Hardware():
    def __init__(self):
        print("Intializing Hardware....")
    general = "Digital of things"
    name = "Complex Circut"

    def canProcessing(self):
        print(f"Yes! it can process Hardware")

# Class 2


class Device(Hardware):
    name = "Telephone"
    def __init__(self):
        super().__init__();
        print("Intializing Device.....")
    def canProcessing(self):
        super(). canProcessing();
        print(f"Yes can processing Device")

    def canCommunicate(self):
        print(f"Yes! can comm")

# Class 3


class SmartPhone(Device):
    name = 'Apple s6'

    def canCommunicate(self):
        super().canCommunicate();
        print(f"Yes!")


# Object Instantciation;
#h = Hardware()
d = Device()
#s = SmartPhone()
#
d.canProcessing()
