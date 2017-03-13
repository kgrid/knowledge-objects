'''
Meal Planning for Glycemic Management Based on Medication
1/6/107

INPUT = wedication, weightloss
OUTPUT = Recommended Meal Planning
'''

def execute(inputs):
    medication = inputs["medication"]
    weightloss = inputs["weightloss"]

    if type(weightloss) != int:
        return "Weightloss must be of type int."

    if type(medication) == int or type(medication) == float:
        return "Medication must be of type string."

    if medication == "":
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
        return "No matching medication option."

    # 0 = no, 1 = yes
    if weightloss == 1:
        return (mealPlan + ". For weighloss, promote portion control and increased physical activity. Intensive lifestyle interventions (counseling, behavioral change, physical activity) with on-going support are needed for weight loss.")
    else:
        return mealPlan



def test():
    if execute({"medication":"","weightloss":0}) != "No medication information provided.":
        return "error."

    if execute({"medication":"fixed daily insulin","weightloss":1}) != "consistent injection time and carbohydrate intake (time and amount). For weighloss, promote portion control and increased physical activity. Intensive lifestyle interventions (counseling, behavioral change, physical activity) with on-going support are needed for weight loss.":
        return "error."

    if execute({"medication":"intensive flexible insulin program (basal/bolus)","weightloss":0.0}) != "Weightloss must be of type int.":
        return "error."

    if execute({"medication":1,"weightloss":0}) != "Medication must be of type string.":
        return "error."

    if execute({"medication":"secretagogues","weightloss":0}) != "carbohydrate at each meal":
        return "error."
    return "ok."
