# Will be creating the restrictions for the powerlifter 
# First restriction will be arm length or wingspan 
# There haven't been any specific studies in terms of the restrictions that we 
# have seen in body proportions so I will 

# Create nested for loops to change each body proportion 
# we still start at the shortest height with the shortest (restricted)
# body proportions

# Psuedocode: 
# for each inch of height starting at 5 feet tall (60 inches) (convert to meters)
    # for each femur length starting at smallest length proportional to body
        # for each torso length starting at smallest length proportional to body 
            # for each arm length starting at smallest length proportional to body
                # for each lower leg length starting at smallest length proportional to body 
                    # create instance for Powerlifter and save it to an array 

# we can see that these amounts of for loops are horrible but with the restrictions, there are only 
# so many different body proportions that exist so it is not terrible in terms of computation

# must import Powerlifter class
from PowerlifterClass import Powerlifter

# Defining the simulation that takes the minimum and maximum heights in centimeters
# Variables we will use:
# h: height 
# a: arm
# f: femur
# t: torso 
# l: lower leg
# after creating the for loops and creating instances of a Powerlifter with specific 
# body proportions and all lifting the same weight, we must save these instances in 
# some data structure to easily access them
def simulatePowerlifters(minHeight, maxHeight):
    arrayHeights = []
    arrayProp = []
    arrayBest = []
    heightIndex = -1
    for h in range(minHeight, maxHeight + 1): 
        if heightIndex != -1:
            arrayHeights.append(arrayProp)
        indexBest = 0                                                   # the dummy powerlifter is considered "best"
        i = 1                                                          # we start at index 1 because there is already something at 0
        #print(i)
        arrayBest.append(indexBest)
        arrayProp = []
        heightIndex += 1
        ### adding a dummy Powerlifter at the beginning of each arrayProp 
        arrayProp.append(Powerlifter(999,1,999,999,999,100))
        # specifying the bounds of the arm lengths 
        armLengthLower = int((h - h/5)/2 - h*0.05)
        armLengthUpper = int((h - h/5)/2 + h*0.05)
        for a in range(armLengthLower, armLengthUpper):
            # Specifying the bounds of the femur lengths 
            femurLengthLower = int(h/4 - 0.05*h)
            femurLengthUpper = int(h/4 + 0.05*h)
            for f in range(femurLengthLower, femurLengthUpper):
                # specifying the bounds of the torso lengths
                torsoLengthLower = int(f - 0.05*h)
                torsoLengthUpper = int(f + 0.05*h)
                for t in range(torsoLengthLower, torsoLengthUpper):
                    # specifying the lower leg
                    lowerLegLengthLower = int(h/3.25 - 0.05*h)
                    lowerLegLengthUpper = int(h/3.25 + 0.05*h)
                    for l in range(lowerLegLengthLower, lowerLegLengthUpper):
                        height = h * 0.01                               # converting centimeters to meters 
                        arm = a * 0.01
                        femur = f * 0.01
                        torso = t * 0.01
                        lowerLeg = l * 0.01
                        # creating specific instance of a powerlifter
                        pL = Powerlifter(height, arm, femur, torso, lowerLeg, 100)
                        if(indexBest < len(arrayProp)): # specifying index bound
                            pLBest = arrayProp[indexBest]
                        # verifying that the body proportions add up the height within a 1% difference
                        if(pL.getCalculatedHeight() > height - height*0.01 and pL.getCalculatedHeight() < height + height*0.01):
                            if(pL.lowerLeg > 0.97*femur and pL.lowerLeg < 1.12*femur):
                                # checking to see if this new instance of a powerlifter is more advantageous than our previous 
                                # best powerlifter
                                # if it is, save current index as best index
                                if (pL.workDone() < pLBest.workDone()):
                                    arrayBest[heightIndex] = i
                                    indexBest = i
                                # add current VALID powerlifter to the list of powerlifters within a specific height 
                                # and move on to the next index
                                arrayProp.append(pL)
                                i = i + 1
    arrayHeights.append(arrayProp)
                        
                        
    return arrayHeights, arrayBest


#arrayHeights, arrayBest = simulatePowerlifters(152, 183) # from 5 feet to 6 feet in height with more precision
#print(arrayHeights[0]) # this will give me the empty array that is automatically placed at the beginning 
#print(arrayHeights[1]) # this will give me the first array of the minimum heights of an individual
#print(len(arrayBest))
#print(arrayBest)
#print(len(arrayHeights))
#print(arrayHeights)
#print(len(arrayHeights[12]))

# Next up to implement will be getting the advantageous proportions 
# for each height. We will do that in a for loop

def getBestPowerlifters(arrayHeights, arrayBest):
    i = 0
    print(arrayBest)
    for bestIndex in arrayBest:
        heightOfLifters = arrayHeights[i]
        bestPL = heightOfLifters[bestIndex]
        print(bestPL.getProportions())
        i += 1
    #
    #

def totalNumberOfLifters(arrayHeights):
    total = 0
    for array in arrayHeights:
        total += len(array)
    return total

# perhaps create another method that simulates getting the best powerlifters 
# it would just call the two methods above 

def simulateBestPowerlifters(minHeight, maxHeight):
    print(f"We will now be simulating the best proportions across heights {minHeight} cm to {maxHeight} cm:")
    arrayHeights, arrayBest = simulatePowerlifters(minHeight, maxHeight)
    getBestPowerlifters(arrayHeights, arrayBest)
    total = totalNumberOfLifters(arrayHeights)
    totalHeights = maxHeight - minHeight
    print(f"The total number of powerlifters simulated is {total} across {totalHeights} different heights.")


# The method that calls everything together
simulateBestPowerlifters(160, 165)
