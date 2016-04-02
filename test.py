import os
import math

class Partition:
    total = 0
    free = 0
    used = 0
    path = ""
    
    def __init__(self, path):
        self.path = path
        self.update()

    def update(self):
        st = os.statvfs(self.path)
        self.total = st.f_blocks * st.f_frsize
        self.free = st.f_bfree * st.f_frsize
        self.used = self.total - self.free;

    def getFreeSpace(self):
        return self.free

    def getTotalSpace(self):
        return self.total

    def getUsedSpace(self):
        return self.used

    def getCapacity(self):
        return math.ceil(( self.used / self.total ) * 100)

if __name__ == '__main__':
    p = Partition("/Volumes/NO NAME/")
    print(p.getTotalSpace())
    print(p.getFreeSpace())
    print(p.getUsedSpace())
    print(p.getCapacity())