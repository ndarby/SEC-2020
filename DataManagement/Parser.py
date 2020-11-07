import re
import array

def parse(filepath):


    with open(filepath, 'r' ) as file:
        passtime = int(file.readline())
        accidental_wait = int(file.readline())
        hand_over = int(file.readline())
        delivery_points = int(file.readline())
        Lines = file.readlines()
        map = []
        orders = []
        i = 0

        for line in Lines:
             map.append(line.strip().split())
             i+= 1
             if(i > 8):
                orders.append(line.strip().split())


        print(map)
        print(orders)

    averageWaitTime = 0.43 * accidental_wait
    return passtime, accidental_wait, hand_over, delivery_points, map, orders, averageWaitTime

