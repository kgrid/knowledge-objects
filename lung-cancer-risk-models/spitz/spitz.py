# Spitz: A Risk Model for Prediction of Lung Cancer
# Lung Cancer Risk Prediction by smoking status
# Author: Kristen McGarry
# Last Updated: May 3, 2017


from math import exp
def execute(inputs):
    age = inputs["age"]
    sex = inputs["sex"]
    smokerStatus = inputs["smokerStatus"]
    ets = inputs["ets"]
    emphysema = inputs["emphysema"]
    hayFever = inputs["hayFever"]
    dust = inputs["dust"]
    fumes = inputs["fumes"]
    chemicals = inputs["chemicals"]
    asbestos = inputs["asbestos"]
    pesticides = inputs["pesticides"]
    woodDust = inputs["woodDust"]
    asthma = inputs["asthma"]
    famHxCanc = inputs["famHxCanc"]
    famHxSmokeCanc = inputs["famHxSmokeCanc"]
    asi = inputs["asi"]
    ageQuit = inputs["ageQuit"]
    asc = inputs["asc"]
    yrsCess = inputs["yrsCess"]
    packYrs = inputs["packYrs"]

    r = calcR(inputs)
    H1 = calcH1(inputs)
    H2 = calcH2(inputs)

    P = ((H1*r)/((H1*r)+H2))*(1-exp(-((H1*r)+H2)))
    prob = round(P*100,2)
    interpretation = "The probability of this individual being diagnosed with lung cancer in the next year and not dying is " + str(prob) + "%."
    return {"result":prob,"interpretation":interpretation}


def calcR(inputs):
    #Odds Ratios (OR) is approx equivalent to r
    OR = {
      "never": {"ets":1.77,"hayFever":0.90,"dust":1.48,"fumes":1.02,"chemicals":1.0,"asbestos":0.86,"pesticides":1.52,"woodDust":0.87,"asthma":1.43,"famHxCanc":[1.0,1.19,1.96],"famHxSmokeCanc":[1.0,1.17]},
      "former": {"ets":2.07,"emphysema":2.99,"hayFever":0.72,"dust":1.64,"fumes":1.32,"chemicals":1.25,"asbestos":1.25,"pesticides":1.22,"woodDust":1.23,"asthma":1.23,"famHxCanc":[1.0,1.16,1.84],"famHxSmokeCanc":[1.0,1.40],"asi":1.01,"ageQuit":1.57,"asc":1.03,"yrsCess":0.99,"packYrs":1.00},
      "current": {"emphysema":2.69,"hayFever":0.62,"dust":1.67,"fumes":1.31,"chemicals":1.34,"asbestos":1.78,"pesticides":1.0,"woodDust":1.20,"asthma":1.01,"famHxCanc":[1.0,1.24,1.68],"famHxSmokeCanc":[1.0,1.58],"asi":0.97,"packYrs":1.01}
    }
    r = 1
    smokerStatus = inputs["smokerStatus"]
    for covariate in inputs.keys():
        if (covariate != "smokerStatus") and (inputs[covariate] != 0) and (covariate != "age") and (covariate != "sex"):
            if covariate not in OR[smokerStatus].keys():
                print "Not applicable: " + str(covariate)
                continue
            if (covariate == "famHxCanc") or (covariate == "famHxSmokeCanc"):
                OR_temp = OR[smokerStatus][covariate][inputs[covariate]]
                r *= OR_temp
                continue
            if covariate in ["asi","asc","yrsCess","packYrs"]:
                OR_temp = (OR[smokerStatus][covariate]) * (inputs[covariate])
                r *= OR_temp
                continue
            OR_temp = OR[smokerStatus][covariate]
            r *= OR_temp
        else:
            continue
    return r

def calcH1(inputs):
    age = inputs["age"]
    sex = inputs["sex"]
    smokerStatus = inputs["smokerStatus"]

    v = {"male":[10.78,25.49,56.60,116.58,221.18,346.77,478.1,564.36,532.36,498.44],
         "female":[11.03,23.19,45.51,93.93,164.9,246.85,318.69,344.67,308.28,266.72]}
    s = {"never":0.4751,"former":0.45352,"current":0.51404}

    v_temp = ((v[sex][age])/100000)
    s_temp = s[smokerStatus]

    H1 = v_temp*(1-s_temp)
    return H1

def calcH2(inputs):
    age = inputs["age"]
    sex = inputs["sex"]

    # MR = Mortality Rate
    MR = {"male":[2.75,400.7,560.0,786.9,1210.2,1855.1,2947.4,4836.4,7980.7,15559.4],
         "female":[153.2,218.8,313.4,479.10,762.9,1197.0,1968.30,3306.10,5761.2,14016.2]}
    MR_temp = MR[sex][age]
    return (MR_temp/100000)


def test():
    if execute({"sex":"male","age":8,"smokerStatus":"former","ets":0,"emphysema":0,"hayFever":0,"dust":1,"fumes":1,"chemicals":1,"asbestos":0,"pesticides":1,"woodDust":0,"asthma":0,"famHxCanc":0,"famHxSmokeCanc":0,"asi":25,"ageQuit":30,"asc":0,"yrsCess":1,"packYrs":0}) != {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next year and not dying is 30.26%.', 'result': 30.26}:
        return "error."
    if execute({"sex":"female","age":5,"smokerStatus":"current","ets":0,"emphysema":1,"hayFever":0,"dust":0,"fumes":0,"chemicals":0,"asbestos":0,"pesticides":0,"woodDust":1,"asthma":0,"famHxCanc":2,"famHxSmokeCanc":0,"asi":76,"ageQuit":0,"asc":0,"yrsCess":0,"packYrs":0}) != {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next year and not dying is 37.89%.', 'result': 37.89}:
        return "error."
    if execute({"sex":"female","age":9,"smokerStatus":"never","ets":1,"emphysema":0,"hayFever":1,"dust":0,"fumes":0,"chemicals":0,"asbestos":0,"pesticides":0,"woodDust":1,"asthma":1,"famHxCanc":2,"famHxSmokeCanc":1,"asi":0,"ageQuit":0,"asc":0,"yrsCess":0,"packYrs":0}) != {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next year and not dying is 0.59%.', 'result': 0.59}:
        return "error."
    if execute({"sex":"male","age":2,"smokerStatus":"never","ets":0,"emphysema":0,"hayFever":0,"dust":0,"fumes":0,"chemicals":0,"asbestos":0,"pesticides":0,"woodDust":0,"asthma":1,"famHxCanc":0,"famHxSmokeCanc":0,"asi":0,"ageQuit":0,"asc":0,"yrsCess":0,"packYrs":0}) != {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next year and not dying is 0.04%.', 'result': 0.04}:
        return "error."
    return "ok."
