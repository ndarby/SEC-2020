

class Robot(PassTime, AccientalWaitTime, HandoverTime):
    def __init__(self, PassTime, AccientalWaitTime, HandoverTime, RobotID):
        self.busy = False
        self.orderDelivered = True
        self.timeAvailable = 0
        self.passTime = PassTime
        self.accidentalWaitTime = AccientalWaitTime
        self.handoverTime = HandoverTime
        self.currentPath = []
        self.pathInfo = []
        self.pathIndex = 1
        self.batteryLevel = 100
        self.currentPosition = (0, 0)
        self.distanceTravelled = 0
        self.log = "Robot " + RobotID

    def ReadyForOrder(self):
        return not self.busy and self.orderDelivered

    def SetOrder(self, orderPath, orderPathInfo):
        self.currentPath = orderPath
        self.pathInfo = orderPathInfo
        self.pathIndex = 0
        self.orderDelivered = False
        self.busy = True


    def Update(self, time):
        if self.timeAvailable >= time or self.busy:
            if self.AttemptMove(time):
                self.Move(time)
        else:
            pass

    def Move(self, time):
        self.currentPosition = currentPath[self.pathIndex]

        if not self.orderDelivered:
            self.pathIndex += 1
        else:
            self.pathIndex -= 1

        self.timeAvailable = time + self.passTime
        self.distanceTravelled +=1
        #implement battery logic here as well



    def AttemptMove(self, time):
        if self.pathIndex >= len(self.currentPath):
            self.orderDelivered = True
            self.timeAvailable = time + self.handoverTime
            self.pathIndex = len(self.currentPath)
            return False
        elif self.pathIndex <= 0:
            self.orderDelivered = False
            self.busy = False
            self.timeAvailable = time
            return False


        if self.pathInfo[self.pathIndex] == "A":
            return self.Wait()
        else:
            return True

    def Wait(self):
        return random.randint(0, 100) < 30


    def Log(self, info):
        self.log += ("\n" + info)