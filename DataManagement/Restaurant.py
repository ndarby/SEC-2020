from DataManagement.Parser import parse
from DataManagement.Robot import Robot
from collections import deque


class Restaurant:
    def __init__(self, inPath):

        self.passTime, self.accidentTime, self.handoverTime, self.deliveryPoints, self.map, self.orders, self.avgAcc = parse(inPath)
        self.path = {}
        self.pathVals = {}
        self.table_positions = []
        self.get_table_positions()
        self.robot1 = Robot(self.passTime, self.accidentTime, self.handoverTime, self.robot_start, "1")
        self.robot2 = Robot(self.passTime, self.accidentTime, self.handoverTime, self.robot_start, "2")
        self.newOrders = []
        self.setupOrder()

        self.routing_setup()
        # column for every node
        # rows for desired node
        # -> value is next hop and weight

        return

    def setupOrder(self):

        self.newOrders = sorted([(int(order[0]) + int(order[2]), order[1]) for order in self.orders], key=lambda x: x[0])

        return

    def routing_setup(self):

        for tableNum in self.table_positions:
            tablePath = self.shortest_path(tableNum)
            vals = []
            for coord in tablePath:
                vals.append(self.map[coord[0]][coord[1]])

            self.pathVals[tableNum] = vals
            self.path[tableNum] = tablePath

        # print(self.pathVals)
        # print(self.path)

        return

    def shortest_path(self, tableNum):

        path = []
        shortest = {self.robot_start: (None, 0)}  # previous, weight

        dropoffs = self.get_neighbors(self.table_positions[tableNum])
        current = self.robot_start
        visited = set()

        while current not in dropoffs:
            visited.add(current)

            dests = self.get_neighbors([current])

            currWeight = shortest[current][1]

            for nextN in dests:
                weight = self.get_weight(nextN) + currWeight

                if nextN in shortest:

                    currShort = shortest[nextN][1]
                    if weight <= currShort:
                        shortest[nextN] = (current, weight)

                else:
                    shortest[nextN] = (current, weight)

            nextDest = {}
            for node in shortest:
                if node not in visited:
                    nextDest[node] = shortest[node]

            current = min(nextDest, key=lambda k: nextDest[k][1])

        path = []
        failCheck = 0
        while current is not None:
            path.append(current)
            next = shortest[current][0]
            current = next
            failCheck += 1
            if failCheck > 25:
                return Exception("Failure")

        return path[::-1]

    def get_neighbors(self, current):

        rowAdd = [-1, 1, 0, 0]
        colAdd = [0, 0, 1, -1]
        neighbors = []
        for coord in current:
            for i in range(4):
                n = (coord[0] + rowAdd[i], coord[1] + colAdd[i])
                if n[0] < 0 or n[0] > 7 or n[1] < 0 or n[1] > 7:
                    continue
                elif self.map[n[0]][n[1]] != '0' and self.map[n[0]][n[1]] != 'A':
                    continue
                if n not in neighbors:
                    neighbors.append(n)
        return neighbors

    def get_weight(self, current):

        value = self.map[current[0]][current[1]]
        if value == "0":
            return self.passTime
        if value == "A":
            return self.avgAcc

        return 0

    def get_table_positions(self):

        positions = {}

        for i, row in enumerate(self.map):
            for j, loc in enumerate(row):
                if loc == "0" or loc == "A":
                    continue

                if loc == "K":
                    self.kitchen_position = (i, j)
                    self.robot_start = self.get_neighbors([self.kitchen_position])[0]
                    continue

                if loc not in positions:
                    positions[loc] = [(i, j)]
                else:
                    positions[loc] = positions[loc].append((i, j))

        self.table_positions = positions

        return

    def checkOrders(self, currTime):

        if currTime >= self.newOrders[0][0]:
            order = self.newOrders.pop(0)
            return order
        return None

    def updateMap(self):

        return

    def update(self, currTime):

        status1 = self.robot1.ReadyForOrder()
        status2 = self.robot2.ReadyForOrder()

        if status1:
            order1 = self.checkOrders(currTime)
            if order1 is not None:
                path = self.path[order1[1]]
                pathVals = self.pathvals[order1[1]]
                self.robot1.SetOrder(path, pathVals)

        if status2:
            order2 = self.checkOrders(currTime)
            if order2 is not None:
                path = self.path[order2[1]]
                pathVals = self.pathvals[order2[1]]
                self.robot2.SetOrder(path, pathVals)

        self.robot1.Update()
        self.robot2.Update()

        self.checkOrders(currTime)

        textBlock = {}
        actions = []
        currState = []

        return textBlock, actions, currState
