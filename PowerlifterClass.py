## a class defining the proportions of a powerlifter 
class Powerlifter():
    # shared variables amongst all lifters
    barDistance = 0.21 ## distance from the floor to the bar with weight loaded (meters)

    # The constructor of the powerlifter
    # self - refering to the class 
    # height - the height of the powerlifter 
    # arm - the arm length of the powerlifter from the top of the shoulder to the center of the closed fist (can be divided into humeri and forearm length for bench)
    # femur - the femur length of the powerlifter from the top of the knee to the center of the hip 
    # torso - the torso length of the powerlfiter from the top of the hip crease to the top of the trap
    # lowerLeg - the length from the top of the knee to the floor (lower leg)
    def __init__(self, height, arm, femur, torso, lowerLeg, mass):
       self.height = height
       self.arm = arm
       self.femur = femur
       self.torso = torso
       self.lowerLeg = lowerLeg
       self.mass = mass
       self.head = height / 7.5
       self.neck = 0.05
    
    ## fu
    def shoulderHeight(self):
        totalHeight = self.lowerLeg + self.femur + self.torso
        return totalHeight

    ## the distance between the bar and the floor when the lifter is standing upright 
    ## and has the bar in their hands with arms straightened out 
    def distanceToFloor(self):
        totalDistance = self.shoulderHeight() - self.arm - self.barDistance
        return totalDistance

    def getProportions(self):
        proportions = 'The body proportions of this powerlifter are: '
        proportions += "" + str(round(self.height,2)) + " m, " + str(round(self.arm,2)) + " m, " + str(round(self.femur,2)) + " m, " + str(round(self.torso,2)) + " m, and " + str(round(self.lowerLeg,2))
        proportions += " m for the lengths of height, arm, femur, torso, and lowerLeg, respectively."
        return proportions
    
    def getCalculatedHeight(self):
        height = self.head + self.neck + self.torso + self.femur + self.lowerLeg
        return height
    
    def workDone(self):
        work = 9.81 * self.distanceToFloor() * self.mass
        return work
    
powerlifter = Powerlifter(1.85, .79, .49, .50, .54, 100) 
print(powerlifter.barDistance)
print(powerlifter.shoulderHeight())
print(powerlifter.distanceToFloor())
print(powerlifter.getProportions())
print(powerlifter.workDone())

    
