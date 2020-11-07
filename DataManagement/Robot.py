

class Robot(PassTime, AccientalWaitTime, HandoverTime):
    def __init__(self, PassTime, AccientalWaitTime, HandoverTime, RobotID):
        self.busy = false
        self.orderDelivered = false
        self.timeAvailable = 0
        self.passTime = PassTime
        self.accidentalWaitTime = AccientalWaitTime
        self.handoverTime = HandoverTime
        self.currentPath = []
        self.pathIndex = 1
        self.batteryLevel = 100
        self.currentOrderInfo = []
        self.currentPosition = (0, 0)
        self.distanceTravelled = 0
        self.log = "Robot " + RobotID


    def Update(self, time):
        if self.timeAvailable >= time or not self.busy:
            if self.AttemptMove():
                self.Move(time)
        else:
            pass

    def Move(self, time):
        self.currentPosition = currentPath[self.pathIndex]

        if not self.orderDelivered:
            self.pathIndex += 1
        else:
            self.pathIndex -+ 1

        self.timeAvailable = time + self.passTime
        self.distanceTravelled +=1
        #implement battery logic here as well



    def AttemptMove(self):
        return true

    def Wait(self):
        number = random.randint(0, 100)
        if number < 30:
            return true
        else:
            return false


    def Log(self, info):
        self.log += ("\n" + info)