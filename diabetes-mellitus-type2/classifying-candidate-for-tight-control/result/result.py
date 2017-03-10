def surveyResults(inputs):
    #factors limiting benefit of tight control
    comorbidities = inputs["comorbidities"]
    advanced_complications = inputs["advanced-complications"]
    treatment_safety = inputs["treatment-safety"]
    life_expectancy = inputs["life-expectancy"]

    # factors heightening risk of tight control
    hypoglycemia_history = inputs["hypoglycemia-history"]
    hypoglycemia_unawareness = inputs["hypoglycemia-unawareness"]
    vascular_disease = inputs["vascular-disease"]
    autonomic_neuropathy = inputs["autonomic-neuropathy"]
    hypoglycemia_comorbidities = inputs["hypoglycemia-comorbidities"]
    poor_support = inputs["poor-support"]


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
    if surveyResults({"comorbidities":"1","advanced-complications":"1","treatment-safety":"1","life-expectancy":"1","hypoglycemia-history":"1","hypoglycemia-unawareness":"1","vascular-disease":"1","autonomic-neuropathy":"1","hypoglycemia-comorbidities":"1","poor-support":"1"}) != "no":
        return "error."
    if surveyResults({"comorbidities":"0","advanced-complications":"0","treatment-safety":"0","life-expectancy":"0","hypoglycemia-history":"0","hypoglycemia-unawareness":"0","vascular-disease":"0","autonomic-neuropathy":"0","hypoglycemia-comorbidities":"0","poor-support":"0"}) != "yes":
        return "error."
    if surveyResults({"comorbidities":"1","advanced-complications":"1","treatment-safety":"0","life-expectancy":"0","hypoglycemia-history":"0","hypoglycemia-unawareness":"0","vascular-disease":"0","autonomic-neuropathy":"1","hypoglycemia-comorbidities":"1","poor-support":"1"}) != "maybe- factors limiting benefits: 2, factors heightening risk: 3":
        return "error."
    if surveyResults({"comorbidities":"","advanced-complications":"","treatment-safety":"","life-expectancy":"","hypoglycemia-history":"","hypoglycemia-unawareness":"","vascular-disease":"","autonomic-neuropathy":"","hypoglycemia-comorbidities":"","poor-support":""}) != "cannot calculate":
        return "error."
    return "ok."
