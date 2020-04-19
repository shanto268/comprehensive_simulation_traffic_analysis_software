class SpeedLimits:
    def __init__(self, speedLimits, maxSpeed): #SpeedLimits is an array
        self.speedLimits = speedLimits
        self.maxSpeed = maxSpeed

    def update(self):
        for speedLimit in self.speedLimits:
            speedLimit.update()

    def getLimit(self, pos):
        for speedLimit in self.speedLimits: 
            if speedLimit.active and speedLimit.inRange(pos):
                return speedLimit.speedLimit
        # limit not found, returnig max speed
        return self.maxSpeed

    def shouldStop(self, pos): #boolean --> true if speed limit is zero else false
     #   print(self.getLimit(pos) == 0)
        return self.getLimit(pos) == 0

class SpeedLimit:
    def createObstacle(pos):
        return SpeedLimit( ranges=(pos,pos), limit=0, ticks=0)
    def __init__(self, ranges, limit, ticks, active=True):
        self.lanes = (ranges[0][1], ranges[1][1])
        self.xPos = (ranges[0][0], ranges[1][0])
        self.speedLimit = limit
        self.ticks = ticks
        self.active = active
        self.acc = 0

    def inRange(self, pos):
      #  print(self.lanes[0])
        return (self.lanes[0] <= pos[1] <= self.lanes[1]) and (self.xPos[0] <= pos[0] <= self.xPos[1])

    def update(self):
        if self.ticks > 0:
            self.acc += 1
            if self.acc >= self.ticks:
                self.acc = 0
                self.active = not self.active

