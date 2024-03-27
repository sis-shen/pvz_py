import image

class ObjectBase(image.Image):
    def __init__(self,pathFmt,pathIndex,pos,size = None ,pathIndexCount = 0):
        super(ObjectBase,self).__init__(self,pathFmt,pathIndex,pos,size,pathIndexCount)

    def update_(self):
        pass