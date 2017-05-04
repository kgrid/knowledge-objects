# Etzel, Development and Validation of a Lung Cancer Risk Prediction Model for African-Americans (Etzel, et al,2008)
# Author: Kristen McGarry, KGrid
# Last Updated: May 3, 2017

from math import exp
def execute(inputs):
    age = inputs["age"]
    sex = inputs["sex"]
    smokerStatus = inputs["smokerStatus"]
    riskFactors = inputs["riskFactors"]


    r = calcR(smokerStatus,riskFactors)
    H1 = calcH1(age,sex,smokerStatus)
    H2 = calcH2(age,sex)

    P = ((H1*r)*((H1*r)+H2))*(1-exp(-5*((H1*r)+H2)))
    prob = round(P*100,2)
    interpretation = "The probability of this individual being diagnosed with lung cancer in the next 5 years and not dying is " + str(prob) + "%."
    return {"result":prob,"interpretation":interpretation}


def calcR(smokerStatus,covariates):
    # Odds ratios, Table 2
    OR = {"current":{"smokerStatus":6.20,"duration>30y":1.97,"numCigsDay>20":3.94,"pack-years>40":3.44,"mentholCigUse":0.69,"asbestos":1.58,"dust":1.50,"fiber":1.33,"svf":2.27,"benzene":1.17,"toluene/xylene":1.40,"dryCleaning":1.60,"vehicleExhaust":1.01,"pesticide":1.36,"gluesPlastic":1.22, "asthma":1.11,"copd":6.38,"hayFever":0.68,"lungCancFDR":1.11,"smokingRelatedCancFDR":1.02},
    "former":{"smokerStatus":3.38,"duration>30y":2.43,"numCigsDay>20":1.75,"pack-years>40":2.74,"yrsCessation":0.42,"ageCessation>30y":2.60,"mentholCigUse":0.99,"asbestos":1.58,"dust":1.50,"fiber":1.33,"svf":2.27,"benzene":1.17,"toluene/xylene":1.40,"dryCleaning":1.60,"vehicleExhaust":1.01,"pesticide":1.36,"gluesPlastic":1.22, "asthma":1.11,"copd":6.38,"hayFever":0.68,"lungCancFDR":1.11,"smokingRelatedCancFDR":1.02}}

    r = 1
    for covariate in covariates:
        OR_temp = OR[smokerStatus][covariate]
        r *= OR_temp
    return r

def calcH1(age,sex,smokerStatus):
    # v = Incidence rate, Table 4
    v = {"male":[0.2015,0.4540,1.1557,3.9880,19.2688,53.1998,114.9708,230.2280,336.7714,452.6758,572.0534,690.5254,647.7919,650.5089],
         "female":[0.2,0.4212,0.6739,4.9258,15.5789,33.6673,64.0670,108.8192,160.2701,236.0585,272.7912,302.7210,273.0735,229.61176]}
    s = {"male":0.79,"female":0.59}

    v_temp = ((v[sex][age])/100000)
    s_temp = s[sex]

    H1 = v_temp*(1-s_temp)
    return H1

def calcH2(age,sex):
    # MR = Mortality Rate, Table 4
    MR = {"male":[224.5,249.6,262.5,334.8,507.1,798.1,1220.7,1678.0,2437.0,33120.0,4818.6,6952.6,9796.1,14876.3],
         "female":[70.6,93.6,132.5,213.1,325.1,486.7,697.2,971.3,1445.8,2047.3,3020.5,4495.8,6654.1,13616.7]}
    MR_temp = MR[sex][age]
    return (MR_temp/100000)


def test():
    if execute({"smokerStatus":"current","age":13,"sex":"male","riskFactors":["duration>30y","numCigsDay>20","asbestos","dust","dryCleaning","pack-years>40","copd"]}) != {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next 5 years and not dying is 90.47%.', 'result': 90.47}:
        return "error."
    if execute({"smokerStatus":"former","age":13,"sex":"female","riskFactors":["duration>30y","asbestos","asthma","yrsCessation","mentholCigUse","ageCessation>30y","dust","fiber","svf"]}) != {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next 5 years and not dying is 0.17%.', 'result': 0.17}:
        return "error."
    if execute({"smokerStatus":"current","age":11,"sex":"male","riskFactors":["copd","duration>30y","pack-years>40","lungCancFDR"]}) != {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next 5 years and not dying is 0.49%.', 'result': 0.49}:
        return "error."
    return "ok."
