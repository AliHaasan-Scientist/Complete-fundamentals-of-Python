import platform
import datetime
#x=platform.system();
x=dir(platform)
#print(x)
dt=datetime.datetime.now();
print(dt.strftime("%b"))