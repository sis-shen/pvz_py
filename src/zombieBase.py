import objectbase

class ZombieBase(objectbase.ObjectBase):
    def __init__(self,pathFmt,pathIndex,pos,size = None ,pathIndexCount = 0):
        super(ZombieBase,self).__init__(pathFmt,pathIndex,pos,size,pathIndexCount)