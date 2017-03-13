def execute(inputs):
    #factors limiting benefit of tight control
    comorbidities = inputs["comorbidities"]
    advanced_complications = inputs["advComplications"]
    treatment_safety = inputs["treatmentSafety"]
    life_expectancy = inputs["lifeExpectancy"]

    # factors heightening risk of tight control
    hypoglycemia_history = inputs["hypoglycemiaHistory"]
    hypoglycemia_unawareness = inputs["hypoglycemiaUnawareness"]
    vascular_disease = inputs["vascularDisease"]
    autonomic_neuropathy = inputs["autonomicNeuropathy"]
    hypoglycemia_comorbidities = inputs["hypoglycemiaComorbidities"]
    poor_support = inputs["poorSupport"]


    factorsLimitingBenefit=[comorbidities,advanced_complications,treatment_safety,life_expectancy]
    riskFactors = [hypoglycemia_history,hypoglycemia_unawareness,vascular_disease,autonomic_neuropathy,hypoglycemia_comorbidities,poor_support]

    limit_benefit = 0
    for result in factorsLimitingBenefit:
        if result == "1":
            limit_benefit +=1
        if result == "":
            return "cannot calculate"
        continue
    #print limit_benefit


    risk_increase = 0
    for result in riskFactors:
        if result == "1":
            risk_increase +=1
        if result == "":
            return "cannot calculate"
        continue
    #print risk_increase

    else_output = "maybe- factors limiting benefits: " + str(limit_benefit) + ", factors heightening risk: " + str(risk_increase)


    if (risk_increase == 0) and (limit_benefit == 0):
        return "yes"

    if (risk_increase == 6) and (limit_benefit) == 4:
        return "no"

    else:
        return else_output


def test():
    if execute({"comorbidities":"1","advComplications":"1","treatmentSafety":"1","lifeExpectancy":"1","hypoglycemiaHistory":"1","hypoglycemiaUnawareness":"1","vascularDisease":"1","autonomicNeuropathy":"1","hypoglycemiaComorbidities":"1","poorSupport":"1"}) != "no":
        return "error."
    if execute({"comorbidities":"0","advComplications":"0","treatmentSafety":"0","lifeExpectancy":"0","hypoglycemiaHistory":"0","hypoglycemiaUnawareness":"0","vascularDisease":"0","autonomicNeuropathy":"0","hypoglycemiaComorbidities":"0","poorSupport":"0"}) != "yes":
        return "error."
    if execute({"comorbidities":"1","advComplications":"1","treatmentSafety":"0","lifeExpectancy":"0","hypoglycemiaHistory":"0","hypoglycemiaUnawareness":"0","vascularDisease":"0","autonomicNeuropathy":"1","hypoglycemiaComorbidities":"1","poorSupport":"1"}) != "maybe- factors limiting benefits: 2, factors heightening risk: 3":
        return "error."
    if execute({"comorbidities":"","advComplications":"","treatmentSafety":"","lifeExpectancy":"","hypoglycemiaHistory":"","hypoglycemiaUnawareness":"","vascularDisease":"","autonomicNeuropathy":"","hypoglycemiaComorbidities":"","poorSupport":""}) != "cannot calculate":
        return "error."
    return "ok."

print test()
