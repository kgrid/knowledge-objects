# Park, Individualized Risk Prediction Model for Lung Cancer in Korean Men
# Author: Kristen McGarry
# Last Updated: May 2, 2017
from math import exp

def execute(inputs):
    age = inputs["age"]
    smokerStatus = inputs["smokerStatus"]
    asi = inputs["asi"]
    bmi = inputs["bmi"]
    physActiv = inputs["physActiv"]
    fastingGluc = inputs["fastingGluc"]

    # Predicting the probability of developing lung cancer within 8 years; equation on page 4
    A = calcA(age,smokerStatus,asi,bmi,physActiv,fastingGluc)
    E = exp(A)
    # for 8 years...
    P = 1-(0.9983894078**E)
    P_percent = round((P*100),2)
    interpretation ="This individual has a " +str(P_percent) +"% probability of developing lung cancer within 8 years."
    return {"result":P_percent,"interpretation":interpretation}


def calcA(age,smokerStatus,asi,bmi,physActiv,fastingGluc):
    meanAge = 45
    ageSq = (age-meanAge)**2
    ageA = (0.1668*((age-meanAge)-0)) -(0.0020*(ageSq-107.3007))

    binValues = []
    smokerTemp = [0,0,0,0]
    if smokerStatus != 0:
        smokerTemp[smokerStatus-1] = 1

    asiTemp = [0,0,0,0]
    if asi != 0:
        asiTemp[asi-1] = 1

    bmiTemp = [0,0,0]
    if bmi != 0:
        bmiTemp[bmi-1] = 1

    phaTemp = [0,0,0]
    if physActiv != 0:
        phaTemp[physActiv-1] = 1

    if fastingGluc == 1:
        gluTemp = [1]
    else:
        gluTemp = [0]

    # order = smoker status, asi, bmi, pha, glu
    # binValues = binary values
    binValues = smokerTemp + asiTemp + bmiTemp + phaTemp + gluTemp
    A = ageA  + (0.4180*((binValues[0]) - 0.1511))  + (0.4444*((binValues[1]) - 0.0905)) + (0.9414*((binValues[2]) - 0.3330)) + (1.3889*((binValues[3]) - 0.1390))  + (0.2194*((binValues[4]) - 0.1441)) + (0.2809*((binValues[5]) - 0.3570)) + (0.5249*((binValues[6]) - 0.0164)) + (0.7120*((binValues[7]) - 0.0064)) + (0.3306*((binValues[8]) - 0.0239))  - (0.2468*((binValues[9]) - 0.2837)) - (0.3386*((binValues[10]) - 0.2851)) - (0.0909*((binValues[11]) - 0.1590)) - (0.1412*((binValues[12]) -0.2952))-(0.0521*((binValues[13]) - 0.0676))+(0.0792*(((binValues[14]) - 0.0605)))

    return A

def test():
    if execute({"age":50,"smokerStatus":3,"asi":1,"bmi":2,"physActiv":1,"fastingGluc":1}) != {'interpretation': 'This individual has a 0.63% probability of developing lung cancer within 8 years.', 'result': 0.63}:
        return "error."
    if execute({"age":0,"smokerStatus":0,"asi":0,"bmi":0,"physActiv":0,"fastingGluc":0}) != {'interpretation': 'This individual has a 0.0% probability of developing lung cancer within 8 years.', 'result': 0.0}:
        return "error."
    else:
        return "ok."
