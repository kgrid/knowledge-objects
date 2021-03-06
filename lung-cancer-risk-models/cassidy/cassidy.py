# Cassidy, The LLP risk model: an individual risk prediction model for lung cancer
# Created by: Kristen McGarry, KGrid
# Last Updated: May 4th, 2017

from math import exp
def getAlpha(sex,age):
    sex = sex.lower()
    if sex == "male":
        alpha_ref = {"40-44":-9.06,"45-49":-8.16,"50-54":-7.31,"55-59":-6.63,"60-64":-5.97,"65-69":-5.56,"70-74":-5.31,"75-79":-4.83,"80-84":-4.68}
    elif sex == "female":
        alpha_ref = {"40-44":-9.90,"45-49":-8.06,"50-54":-7.46,"55-59":-6.50,"60-64":-6.22,"65-69":-5.99,"70-74":-5.49, "75-79":-5.23,"80-84":-5.42}
    else:
        return "invalid sex"

    # take midpoint of every age
    age = age + 0.5

    if ((age >= 40) & (age < 45)):
        alpha_1 = alpha_ref["40-44"]
        multi_1 = 45-age
    elif ((age >= 45) & (age < 50)):
        alpha_1 = alpha_ref["45-49"]
        multi_1 = 50-age
    elif ((age >= 50) & (age < 55)):
        alpha_1 = alpha_ref["50-54"]
        multi_1 = 55-age
    elif ((age >= 55) & (age < 60)):
        alpha_1 = alpha_ref["55-59"]
        multi_1 = 60-age
    elif ((age >= 60) & (age < 65)):
        alpha_1 = alpha_ref["60-64"]
        multi_1 = 65-age
    elif ((age >= 65) & (age < 70)):
        alpha_1 = alpha_ref["65-69"]
        multi_1 = 70-age
    elif ((age >= 70) & (age < 75)):
        alpha_1 = alpha_ref["70-74"]
        multi_1 = 75-age
    elif ((age >= 75) & (age < 80)):
        alpha_1 = alpha_ref["75-79"]
        multi_1 = 80-age
    elif ((age >= 80) & (age < 85)):
        alpha_1 = alpha_ref["80-84"]
        multi_1 = 85-age
    else:
        return "invalid age or age outside of 40-84 range"



    multi_2 = 5-multi_1
    age = age + multi_1
    if ((age >= 40) & (age < 45)):
        alpha_2 = alpha_ref["40-44"]
    elif ((age >= 45) & (age < 50)):
        alpha_2 = alpha_ref["45-49"]
    elif ((age >= 50) & (age < 55)):
        alpha_2 = alpha_ref["50-54"]
    elif ((age >= 55) & (age < 60)):
        alpha_2 = alpha_ref["55-59"]
    elif ((age >= 60) & (age < 65)):
        alpha_2 = alpha_ref["60-64"]
    elif ((age >= 65) & (age < 70)):
        alpha_2 = alpha_ref["65-69"]
    elif ((age >= 70) & (age < 75)):
        alpha_2 = alpha_ref["70-74"]
    elif ((age >= 75) & (age < 80)):
        alpha_2 = alpha_ref["75-79"]
    elif ((age >= 80) & (age <= 85)):
        alpha_2 = alpha_ref["80-84"]
    else:
        return "invalid age or age outside of 40-84 range"

    alpha = (multi_1*(alpha_1/5)) + (multi_2*(alpha_2/5))
    return alpha

# Beta = sum(Bi * xi), if risk factor is listed, x = 1
def getBeta(listOfRiskFactors):
    total = 0
    # Model Coefficients, Table 2
    logOddsRatio = {"pneum":0.602,"asbestos":0.634,"cancHx":0.675,"famHxCanc, early onset":0.703,"famHxCanc, late onset":0.168,"smoking duration, 1-20 years":0.769,"smoking duration, 21-40 years":1.452,"smoking duration, 41-60 years":2.507,"smoking duration, >= 60 years":2.724}
    for riskFactor in listOfRiskFactors:
        if riskFactor not in logOddsRatio.keys():
            return "invalid risk factor"
        value = logOddsRatio[riskFactor]
        total += value
    return total


def execute(inputs):
    sex = inputs["sex"]
    age = inputs["age"]
    listOfRiskFactors = inputs["riskFactors"]

    alpha = getAlpha(sex,age)
    if type(alpha) != float:
        return alpha
    beta = getBeta(listOfRiskFactors)
    if type(beta) != float:
        return beta

    prob = 1/(1+exp(-(alpha+beta)))
    prob = (prob *100)
    prob = round(prob,2)
    interpretation = "This individual has a " + str(prob) + "% probability of developing lung cancer in the next 5 years."
    return {"result":prob,"interpretation":interpretation}



def test():
    if str(getAlpha("male",68)) != "-5.385":
        return "error."
    if str(getAlpha("female",74)) != "-5.256":
        return "error."
    if str(getAlpha("female",64)) != "-6.013":
        return "error."
    if str(getAlpha("male",51)) != "-7.106":
        return "error."
    if str(getBeta({"smoking duration, 21-40 years":1})) != "1.452":
        return "error."
    if execute({"sex":"male","age":77,"riskFactors":["famHxCanc, early onset","asbestos"]}) != {'interpretation': 'This individual has a 3.17% probability of developing lung cancer in the next 5 years.', 'result': 3.17}:
        return "error."
    if execute({"sex":"male","age":51,"riskFactors":["smoking duration, 21-40 years"]}) != {'interpretation': 'This individual has a 0.35% probability of developing lung cancer in the next 5 years.', 'result': 0.35}:
        return "error."
    if execute({"sex":"female","age":65,"riskFactors":["smoking duration, 21-40 years","famHxCanc, late onset","pneum"]}) != {'interpretation': 'This individual has a 2.37% probability of developing lung cancer in the next 5 years.', 'result': 2.37}:
        return "error."
    if execute({"sex":"female","age":68,"riskFactors":["smoking duration, 21-40 years"]})!= {'interpretation': 'This individual has a 1.49% probability of developing lung cancer in the next 5 years.', 'result': 1.49}:
        return  "error."
    if execute({"sex":"male","age":66,"riskFactors":["smoking duration, 41-60 years","asbestos"]}) != {'interpretation': 'This individual has a 8.75% probability of developing lung cancer in the next 5 years.', 'result': 8.75}:
        return "error."
    if execute({"sex":"male","age":90,"riskFactors":[]}) != "invalid age or age outside of 40-84 range":
        return "error."
    if execute({"sex":"child","age":10,"riskFactors":[]}) != "invalid sex":
        return "error."
    if execute({"sex":"FEMALE","age":47,"riskFactors":["diabetic"]}) != "invalid risk factor":
        return "error."
    return "ok."
