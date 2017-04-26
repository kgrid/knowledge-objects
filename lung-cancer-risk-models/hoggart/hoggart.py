import math
from math import exp
# **** TIME ZERO IS SET TO 35 YEARS OLD ****
def execute(inputs):
    smokerStatus = inputs["smokerStatus"]
    smokDurat = inputs["smokDurat"]
    covariates = inputs["covariates"]
    t = inputs["t"]

    survFuncCan = (calcSurvFunc(smokerStatus,"cancer",smokDurat,t))
    exp_betaXCan = betaX(smokerStatus,covariates)
    P_Cancer = (1-exp(exp_betaXCan*survFuncCan))

    survFuncDea = (calcSurvFunc(smokerStatus,"death",smokDurat,t))
    exp_betaXDea = betaX(smokerStatus,covariates)
    P_Death = (exp(exp_betaXCan*survFuncCan))

    P_diagnosis = (P_Cancer * P_Death)

    return "This individual has a " + str(round(P_diagnosis *100,2)) + "% probability of being diagnosed with lung cancer in 1 year from age t."


def betaX(smokerStatus,covariates):
    # sex: female = 1, male =0
    HR_current = {"sex":1.35,"bmi":0.963,"edLevel":0.944,"hayFever":0.593,"asthma":0.85,"famHxCanc":1.27,"chr15q25":1.13,"chr5p15":0.954,"silica":0.893,"pah":0.988,"metal":0.961,"asb":0.943}
    HR_former = {"sex":1.2,"bmi":0.96,"edLevel":0.436,"hayFever":0.901,"asthma":1.58,"famHxCanc":1.22,"chr15q25":1.14,"chr5p15":1.06,"silica":0.851,"pah":0.869,"metal":1.23,"asb":1.05}

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

def calcSurvFunc(smokerStatus,survivorStatus,smokDurat,t):
    ref = {"current":{"cancer":{"lam":[3.819,4.056,4.23,4.339,4.38,4.567,4.506,4.504],"gamma":[0.999,1.071,1.298,1.518,1.679,1.517,1.615,1.684]},"death":{"lam":[3.69,3.774,3.859,3.944,3.979,4.049,4.096,4.069],"gamma":[1.22,1.312,1.569,1.775,1.925,1.854,1.838,1.912]}},"former":{"cancer":{"lam":[4.987,4.723,4.321,5.179,4.786,4.651,4.654,4.366,5.563,4.68,4.491,4.241,4.177],"gamma":[0.75,0.819,1.032,1.165,1.353,1.46,1.318,1.662,1.088,1.705,1.879,2.336,2.574]},"death":{"lam":[3.754,3.75,3.8,4.008,3.975,3.954,3.928,3.982,4.123,4.058,4.02,3.999,4.041],"gamma":[1.21,1.511,1.669,1.621,1.742,1.835,2.129,2.15,1.769,1.865,2.148,2.36,2.49]}}}

    s = smokDurat

    lam = 0
    gamma = 0

    if smokerStatus == "current":
        if (t <= 18):
            lam = ref[smokerStatus][survivorStatus]["lam"][0]
            gamma = ref[smokerStatus][survivorStatus]["gamma"][0]
        elif ((t > 18) and (t <=20)):
            lam = ref[smokerStatus][survivorStatus]["lam"][1]
            gamma = ref[smokerStatus][survivorStatus]["gamma"][1]
        elif ((t > 20) and (t <=22)):
            lam = ref[smokerStatus][survivorStatus]["lam"][2]
            gamma = ref[smokerStatus][survivorStatus]["gamma"][2]
        elif ((t > 22) and (t <=24)):
            lam = ref[smokerStatus][survivorStatus]["lam"][3]
            gamma = ref[smokerStatus][survivorStatus]["gamma"][3]
        elif ((t > 24) and (t <=26)):
            lam = ref[smokerStatus][survivorStatus]["lam"][4]
            gamma = ref[smokerStatus][survivorStatus]["gamma"][4]
        elif ((t > 26) and (t <=28)):
            lam = ref[smokerStatus][survivorStatus]["lam"][5]
            gamma = ref[smokerStatus][survivorStatus]["gamma"][5]
        elif ((t > 28) and (t <=30)):
            lam = ref[smokerStatus][survivorStatus]["lam"][6]
            gamma = ref[smokerStatus][survivorStatus]["gamma"][6]
        elif (t > 30):
            lam = ref[smokerStatus][survivorStatus]["lam"][7]
            gamma = ref[smokerStatus][survivorStatus]["gamma"][7]

    elif smokerStatus == "former":
        if (t <= 22):
            if (s<= 20):
                lam = ref[smokerStatus][survivorStatus]["lam"][0]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][0]
            if ((s>=30) and (s >20)):
                lam = ref[smokerStatus][survivorStatus]["lam"][1]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][1]
            if (s>30):
                lam = ref[smokerStatus][survivorStatus]["lam"][2]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][2]
        if (t <= 26) and (t >22):
            if (s<= 20):
                lam = ref[smokerStatus][survivorStatus]["lam"][3]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][3]
            if ((s<=30) and (s >20)):
                lam = ref[smokerStatus][survivorStatus]["lam"][4]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][4]
            if ((s>30) and (s <= 36)):
                lam = ref[smokerStatus][survivorStatus]["lam"][5]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][5]
            if ((s>36) and (s <= 42)):
                lam = ref[smokerStatus][survivorStatus]["lam"][6]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][6]
            if (s>42):
                lam = ref[smokerStatus][survivorStatus]["lam"][7]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][7]
        if (t >26):
            if (s<= 20):
                lam = ref[smokerStatus][survivorStatus]["lam"][8]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][8]
            if ((s<=30) and (s >20)):
                lam = ref[smokerStatus][survivorStatus]["lam"][9]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][9]
            if ((s>30) and (s <= 36)):
                lam = ref[smokerStatus][survivorStatus]["lam"][10]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][10]
            if ((s>36) and (s <= 42)):
                lam = ref[smokerStatus][survivorStatus]["lam"][11]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][11]
            if (s>42):
                lam = ref[smokerStatus][survivorStatus]["lam"][12]
                gamma = ref[smokerStatus][survivorStatus]["gamma"][12]

    temp = (((t/lam)**gamma) - (((t+1)/lam)**gamma))
    return temp


def test():
    if str(calcSurvFunc("former","death",40,48)) != "-17.5759666625":
        return "error."
    if execute({"smokerStatus":"former","smokDurat":10,"t":24,"covariates":{"sex":"female","bmi":28,"hayFever": 1}}) != "This individual has a 13.93% probability of being diagnosed with lung cancer in 1 year from age t.":
        return "error."
    if execute({"smokerStatus":"current","smokDurat":10,"t":10,"covariates":{"sex":"male","bmi":34,"asb": 1}}) != "This individual has a 11.74% probability of being diagnosed with lung cancer in 1 year from age t.":
        return "error."
    if execute({"smokerStatus":"current","smokDurat":15,"t":30,"covariates":{"sex":"male","bmi":38,"asb": 0,"famHxCanc": 1,"asthma":0}}) != "This individual has a 25.0% probability of being diagnosed with lung cancer in 1 year from age t.":
        return "error."
    if execute({"smokerStatus":"current","smokDurat":15,"t":30,"covariates":{"sex":"male","bmi":38,"asb": 1,"famHxCanc": 1,"asthma":0}}) != "This individual has a 24.99% probability of being diagnosed with lung cancer in 1 year from age t.":
        return "error."
    return "ok."
