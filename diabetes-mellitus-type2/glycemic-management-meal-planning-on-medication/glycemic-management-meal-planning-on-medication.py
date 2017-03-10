'''
Meal Planning for Glycemic Management Based on Medication
1/6/107

INPUT = wedication, weightloss
OUTPUT = Recommended Meal Planning
'''

def MealPlanOnMed(inputs):
    medication = inputs["medication"]
    weightloss = inputs["weightloss"]

    if type(weightloss) != int:
        #print "Weightloss must be of type int."
        return "Weightloss must be of type int."

    if type(medication) == int or type(medication) == float:
        #print "Medication must be of type string."
        return "Medication must be of type string."

    if medication == "":
        #print "No medication information provided."
        return "No medication information provided."

    elif medication == "no medication or oral medication":
        mealPlan = "Portion control of healthful choices"

    elif medication == "secretagogues":
        mealPlan = "carbohydrate at each meal"

    elif medication == "fixed daily insulin":
        mealPlan = "consistent injection time and carbohydrate intake (time and amount)"

    elif medication == "premixed insulin":
        mealPlan = "consistent injection times and meal times"

    elif medication == "intensive flexible insulin program (basal/bolus)":
        mealPlan = "carbohydrate counting and dosage adjustments including carb:insulin ratios and correction doses"

    else:
        #print "No matching medication option."
        return "No matching medication option."

    # 0 = no, 1 = yes
    if weightloss == 1:
        #print (mealPlan + ". For weighloss, promote portion control and increased physical activity. Intensive lifestyle interventions (counseling, behavioral change, physical activity) with on-going support are needed for weight loss.")

        return (mealPlan + ". For weighloss, promote portion control and increased physical activity. Intensive lifestyle interventions (counseling, behavioral change, physical activity) with on-going support are needed for weight loss.")
    else:
        #print mealPlan
        return mealPlan



def test():
    if MealPlanOnMed({"medication":"","weightloss":0}) == "No medication information provided.":
        print "ok."
    else:
        print "error."
        return "error."

    if MealPlanOnMed({"medication":"fixed daily insulin","weightloss":1}) == "consistent injection time and carbohydrate intake (time and amount). For weighloss, promote portion control and increased physical activity. Intensive lifestyle interventions (counseling, behavioral change, physical activity) with on-going support are needed for weight loss.":
        print "ok."
    else:
        print "error."
        return "error."

    if MealPlanOnMed({"medication":"intensive flexible insulin program (basal/bolus)","weightloss":0.0}) == "Weightloss must be of type int.":
        print "ok."
    else:
        print "error."
        return "error."

    if MealPlanOnMed({"medication":1,"weightloss":0}) == "Medication must be of type string.":
        print "ok."
    else:
        print "error."
        return "error."

    if MealPlanOnMed({"medication":"secretagogues","weightloss":0}) == "carbohydrate at each meal":
        print "ok."
    else:
        print "error."
        return "error."
#test()
