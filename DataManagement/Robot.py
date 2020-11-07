import random


class Robot:
    def __init__(self, PassTime, AccidentalWaitTime, HandoverTime, PosStart, RobotID):
        """
        Constructor for the robot class
        :param PassTime: Constant time to take for each movement
        :param AccidentalWaitTime: Wait time if robot cannot move on a wait time spot
        :param HandoverTime: The time the robot needs to be at the table handing the meals to the customers
        :param PosStart: The starting position of the robot
        :param RobotID: The ID of the robot
        """
        self.busy = False   #if the robot has an order this is set to true, if no current order is assigned, false
        self.orderDelivered = True  #if the order has been delivered
        self.charging = True    #if the robot is charging
        self.canStartDelivery = True
        self.timeAvailable = 0
        self.passTime = PassTime
        self.accidentalWaitTime = AccidentalWaitTime
        self.handoverTime = HandoverTime
        self.currentPath = []
        self.pathInfo = []
        self.pathIndex = 1
        self.batteryLevel = 600
        self.totalBatteryUsage = 0
        self.currentPosition = PosStart
        self.distanceTravelled = 0
        self.totalDeliveryPoints = 0
        self.currentOrderDeliveryPoints = 0
        self.log = "Robot " + RobotID

    def CheckPathCost(self):

        """
        Total time is calculated as the return trip time for the robot- the one way trip is multiplied by 2 to get return trip.
        The amount of time taken to wait is done by calculating how many potential waiting periods and expected number of failed attempts
        The final time is then multiplied by 2 to get the battery life needed for the return trip
        :return: Cost in battery life units
        """
        totalTime = len(self.currentPath) * self.passTime
        totalTime += self.accidentalWaitTime * 0.43 * len(filter(lambda x: x == "A", self.pathInfo))
        return totalTime * 4

    def ReadyForOrder(self):
        """
        Checks if the robot is ready to be assigned an order
        :return: if the robot is ready to accept an order
        """
        return not self.busy and self.orderDelivered and self.charging

    def SetOrder(self, orderPath, orderPathInfo, deliveryPoints):
        """
        Sets the order information for the robot
        :param orderPath: The path the robot will take
        :param orderPathInfo: The details of the path (waiting blocks or not)
        :param deliveryPoints: The amount of delivery points for the order
        :return: Nothing
        """
        self.currentPath = orderPath
        self.pathInfo = orderPathInfo
        self.pathIndex = 0
        self.currentOrderDeliveryPoints = deliveryPoints
        self.orderDelivered = False
        self.busy = True
        if self.CheckPathCost() >= self.batteryLevel:
            self.canStartDelivery = False
        else:
            self.canStartDelivery = True

    def Update(self, time):
        """
        Updates the state and position of the robot if applicable
        :param time: The current time
        :return: Nothing
        """
        if self.timeAvailable >= time and self.busy:
            if self.canStartDelivery:
                if self.AttemptMove(time):
                    self.Move(time)
            else:
                if self.CheckPathCost() < self.batteryLevel:
                    self.canStartDelivery = True

        if self.charging and self.batteryLevel < 600:
            self.batteryLevel += 10
        else:
            self.batteryLevel -= 2
            self.totalBatteryUsage += 2

    def Move(self, time):
        self.currentPosition = self.currentPath[self.pathIndex]

        if not self.orderDelivered:
            self.pathIndex += 1
        else:
            self.pathIndex -= 1

        self.timeAvailable = time + self.passTime
        self.distanceTravelled +=1

    def AttemptMove(self, time):
        if self.pathIndex >= len(self.currentPath):
            self.orderDelivered = True
            self.totalDeliveryPoints += self.currentOrderDeliveryPoints
            self.timeAvailable = time + self.handoverTime
            self.pathIndex = len(self.currentPath)
            return False
        elif self.pathIndex <= 0:
            self.orderDelivered = False
            self.busy = False
            self.charging = True
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