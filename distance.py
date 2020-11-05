from math import sqrt

botPos = [0,0]
distList = []
def moveBot(x,y):
    distance= sqrt(((x-botPos[0])**2)+((y-botPos[1])**2))
    distList.append(distance)
    botPos[0]=x
    botPos[1]=y

def getDist():
    totalDistance = 0
    for i in distList:
        totalDistance += i
    return totalDistance

while True:
    posString = input("Where do you want to move? (x,y) and type 999 for total distance traveled")
    stripPos = 0
    dist = 0
    try:
        stripPos = posString.replace("(","").replace(")","").split(",")
        moveBot(int(stripPos[0]),int(stripPos[1]))
    
    except:
        if(posString == "999"):
            dist = getDist()
            print(dist)
        else:
            print("make sure to put your cooridinates in (x,y) form")
