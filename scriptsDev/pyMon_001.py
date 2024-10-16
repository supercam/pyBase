"""
.Synopsis
    Monitor applications with Python
.Description


    Example - https://umeey.medium.com/system-monitoring-made-easy-with-pythons-psutil-library-4b9add95a443
.Author
    James Lewis
.Date
    09/30/2024
"""


#import modules

try:
    import platform
except ImportError:
    print("failed to import platform")
try:
    import psutil
except ImportError:
    print("failed to import psutil")

try:
    import json
except ImportError:
    print("failed to import json")

try:
    import subprocess
except ImportError:
    print("failed to import subprocess")

try:
    import time
except ImportError:
    print("failed to import time")


#dictionary holds
osDict = {}
memDict = {}
cpuDict = {}
diskDict = {}
netDict = {}

#get OS info
os = platform.uname().system
node = platform.uname().node
release = platform.uname().release
osVer = platform.uname().version
machine = platform.uname().machine

#get mem info
ttlMem = psutil.virtual_memory().total / (1024.0 ** 3),
availMem = psutil.virtual_memory().total / (1024.0 ** 3),
usedMem = psutil.virtual_memory().used / (1024.0 ** 3),
memPercentage = psutil.virtual_memory().percent

#get sys uptime
bootTime = psutil.boot_time()
curTime = time.time()
upTimeSec = curTime - bootTime
upTimeMin = upTimeSec // 60
upTimeHrs = upTimeMin // 60
upTimeDays = upTimeHrs // 24
uptime = F"{node} uptime is: {int(upTimeDays)} days, {int(upTimeHrs % 24)} hours, {int(upTimeMin)} minutes, {int(upTimeSec)} seconds"

print(uptime)
print(ttlMem)


