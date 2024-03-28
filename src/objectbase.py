import image
import time

class ObjectBase(image.Image):
    def __init__(self,pathFmt,pathIndex,pos,size = None ,pathIndexCount = 0):
        super(ObjectBase,self).__init__(pathFmt,pathIndex,pos,size,pathIndexCount)
        self.preIndexTime = 0
        self.prevPositionTime = 0

    def update(self):
        self.checkImageIndex()
        self.checkPosition()
    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= 0.02:
            return
        self.preIndexTime = time.time()
        idx = self.pathIndex
        if(self.pathIndexCount != 0):
            idx= (self.pathIndex + 1) % self.pathIndexCount

        self.updateIndex(idx)

    def checkPosition(self):
        if time.time() - self.prevPositionTime <= 0.02:
            return
        self.prevPositionTime = time.time()

        self.doLeft()