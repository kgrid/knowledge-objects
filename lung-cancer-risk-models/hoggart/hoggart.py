import math
from math import exp
# **** TIME ZERO IS SET TO 35 YEARS OLD ****
def execute(inputs):
    smokerStatus = inputs["smokerStatus"]
    smokingDuration = inputs["smokingDuration"]
    covariates = inputs["covariates"]
    t = inputs["t"]

    survFuncCan = (calcSurvFunc(smokerStatus,"cancer",smokingDuration,t))
    exp_betaXCan = betaX(smokerStatus,covariates)
    P_Cancer = (1-exp(exp_betaXCan*survFuncCan))

    survFuncDea = (calcSurvFunc(smokerStatus,"death",smokingDuration,t))
    exp_betaXDea = betaX(smokerStatus,covariates)
    P_Death = (exp(exp_betaXCan*survFuncCan))

    P_diagnosis = (P_Cancer * P_Death)

    return "This individual has a " + str(round(P_diagnosis *100,2)) + "% probability of being diagnosed with lung cancer in 1 year from age t."


def betaX(smokerStatus,covariates):
    # sex: female = 1, male =0
    HR_current = {"sex":1.35,"BMI":0.963,"education level":0.944,"hay fever":0.593,"asthma":0.85,"family history of cancer":1.27,"chr15q25":1.13,"chr5p15":0.954,"silica":0.893,"pah":0.988,"metal":0.961,"asbestos":0.943}
    HR_former = {"sex":1.2,"BMI":0.96,"education level":0.436,"hay fever":0.901,"asthma":1.58,"family history of cancer":1.22,"chr15q25":1.14,"chr5p15":1.06,"silica":0.851,"pah":0.869,"metal":1.23,"asbestos":1.05}

    total = 0

    for covariate in covariates.keys():
        if smokerStatus == "current":
            HR_map = HR_current
        elif smokerStatus == "former":
            HR_map = HR_former
        HR = HR_map[covariate]
        beta = math.log(HR,10)

        x = covariates[covariate]
        if x == "female":
            x = 1


        if (x == 0) or (x=="male"):
            continue
        else:
            total= total + (beta*x)

    return (exp(total))

def calcSurvFunc(smokerStatus,survivorStatus,smokingDuration,t):
    s = smokingDuration
    lam = 0
    gamma = 0
    lam = 0
    gamma = 0
    # current smoker, cancer
    if (smokerStatus == "current") and (survivorStatus == "cancer"):
        if (t <= 18):
            lam = 3.819
            gamma = 0.9999
        elif ((t > 18) and (t <=20)):
            lam = 4.056
            gamma = 1.071
        elif ((t > 20) and (t <=22)):
            lam = 4.230
            gamma = 1.298
        elif ((t > 22) and (t <=24)):
            lam = 4.339
            gamma = 1.518
        elif ((t > 24) and (t <=26)):
            lam = 4.380
            gamma = 1.679
        elif ((t > 26) and (t <=28)):
            lam = 4.567
            gamma = 1.517
        elif ((t > 28) and (t <=30)):
            lam = 4.506
            gamma = 1.615
        elif (t > 30):
            lam = 4.504
            gamma = 1.684
    # current smoker, death
    if (smokerStatus == "current") and (survivorStatus == "death"):
        if (t <= 18):
            lam = 3.690
            gamma = 1.220
        elif ((t > 18) and (t <=20)):
            lam = 3.774
            gamma = 1.312
        elif ((t > 20) and (t <=22)):
            lam = 3.859
            gamma = 1.560
        elif ((t > 22) and (t <=24)):
            lam = 3.944
            gamma = 1.775
        elif ((t > 24) and (t <=26)):
            lam = 3.979
            gamma = 1.925
        elif ((t > 26) and (t <=28)):
            lam = 4.049
            gamma = 1.854
        elif ((t > 28) and (t <=30)):
            lam = 4.096
            gamma = 1.838
        elif (t > 30):
            lam = 4.069
            gamma = 1.912
    # former smoker, cancer
    if (smokerStatus == "former") and (survivorStatus == "cancer"):
        if (t <= 22):
            if (s<= 20):
                lam = 4.987
                gamma = 0.750
            if ((s>=30) and (s >20)):
                lam = 4.723
                gamma = 0.819
            if (s>30):
                lam = 4.321
                gamma = 1.032
        if (t <= 26) and (t >22):
            if (s<= 20):
                lam =5.179
                gamma = 1.165
            if ((s<=30) and (s >20)):
                lam = 4.786
                gamma = 1.353
            if ((s>30) and (s <= 36)):
                lam = 4.651
                gamma = 1.460
            if ((s>36) and (s <= 42)):
                lam = 4.654
                gamma = 1.318
            if (s>42):
                lam = 4.366
                gamma = 1.662
        if (t >26):
            if (s<= 20):
                lam =5.563
                gamma =1.088
            if ((s<=30) and (s >20)):
                lam = 4.680
                gamma = 1.705
            if ((s>30) and (s <= 36)):
                lam = 4.491
                gamma = 1.879
            if ((s>36) and (s <= 42)):
                lam = 4.241
                gamma = 2.336
            if (s>42):
                lam = 4.177
                gamma = 2.574
    # former smoker, death
    if (smokerStatus == "former") and (survivorStatus == "death"):
        if (t <= 22):
            if (s<= 20):
                lam = 3.754
                gamma = 1.210
            if ((s>=30) and (s >20)):
                lam = 3.750
                gamma = 1.511
            if (s>30):
                lam = 3.8
                gamma = 1.669
        if (t <= 26 and t >22):
            if (s<= 20):
                lam =4.008
                gamma = 1.621
            if ((s<=30) and (s >20)):
                lam = 3.975
                gamma = 1.742
            if ((s>30) and (s <= 36)):
                lam = 3.954
                gamma = 1.835
            if ((s>36) and (s <= 42)):
                lam = 3.928
                gamma = 2.129
            if (s>42):
                lam = 3.982
                gamma = 2.150
        if (t >26):
            if (s<= 20):
                lam =4.123
                gamma =1.769
            if ((s<=30) and (s >20)):
                lam = 4.058
                gamma = 1.865
            if ((s>30) and (s <= 36)):
                lam = 4.020
                gamma = 2.148
            if ((s>36) and (s <= 42)):
                lam = 3.999
                gamma = 2.360
            if (s>42):
                lam = 4.041
                gamma = 2.490

    temp = (((t/lam)**gamma) - (((t+1)/lam)**gamma))
    return temp


def test():
    if str(calcSurvFunc("former","death",40,48)) != "-17.5759666625":
        return "error."
    if execute({"smokerStatus":"former","smokingDuration":10,"t":24,"covariates":{"sex":"female","BMI":28,"hay fever": 1}}) != "This individual has a 13.93% probability of being diagnosed with lung cancer in 1 year from age t.":
        return "error."
    if execute({"smokerStatus":"current","smokingDuration":10,"t":10,"covariates":{"sex":"male","BMI":34,"asbestos": 1}}) != "This individual has a 11.76% probability of being diagnosed with lung cancer in 1 year from age t.":
        return "error."
    if execute({"smokerStatus":"current","smokingDuration":15,"t":30,"covariates":{"sex":"male","BMI":38,"asbestos": 0,"family history of cancer": 1,"asthma":0}}) != "This individual has a 25.0% probability of being diagnosed with lung cancer in 1 year from age t.":
        return "error."
    if execute({"smokerStatus":"current","smokingDuration":15,"t":30,"covariates":{"sex":"male","BMI":38,"asbestos": 1,"family history of cancer": 1,"asthma":0}}) != "This individual has a 24.99% probability of being diagnosed with lung cancer in 1 year from age t.":
        return "error."
    return "ok."
