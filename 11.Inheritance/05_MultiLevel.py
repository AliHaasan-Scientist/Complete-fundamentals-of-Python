# Class 1
class Hardware():
    general = "Digital of things"
    name = "Complex Circut"

    def canProcessing(self):
        print(f"Yes! it can process Hardware")

# Class 2


class Device(Hardware):
    name = "Telephone"

    def canProcessing(self):
        print(f"Yes can processing Device")

    def canCommunicate(self):
        print(f"Yes! can comm")

# Class 3


class SmartPhone(Device):
    name = 'Apple s6'

    def canCommunicate(self):
        print(f"Yes!")


# Object Instantciation;
h = Hardware()
d = Device()
s = SmartPhone()
#
print(s.general)
