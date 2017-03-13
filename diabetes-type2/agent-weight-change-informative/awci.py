# Input drug name (generic name and brand name), output weight change information
def execute(inputs):
    agent = inputs["agent"]
    agent = agent.lower()
    result = "cannot calculate"

    # agent categories including generic names and brand names
    biguanide = ["metformin","glucophage","metformin extended release","glucophage xr"]
    sulfonylureas = ["glimepiride","amaryl","glipizide","glucotrol","glipizide xl","glucotrol xl","glyburide","diabeta, micronase","glyburide, micronized","glynase"]
    thiazolidinedione = ["pioglitazone","actos"]
    alpha_glucosidase_inhibitor = ["acarbose","precose","miglitol","glyset"]
    non_sulfonylurea_insulin_secretogogues = ["repaglinide","prandin","nateglinide","starlix"]
    dpp4_inhibitor = ["sitagliptin","januvia","saxaglipton","onglyza","lingaliptin","tradjenta","alogliptin","nesina"]
    sglt2_inhibitor = ["canagliflozin","invokana","dapagliflozin","farxiga","empagliflozin","jardiance"]
    incretin_mimetic = ["exenatide","byetta","exenatide extended-release","bydureon","liraglutide","victoza","dulaglutide","trulicity","albiglutide","tanzeum"]
    amylinomimetic = ["pramlintide","symlin"]
    rapid_acting_insulin = ["lispro","humalog","aspart","novolog","glulisine","apidra"]
    short_acting_insulin = ["regular","nph"]
    intermediate_acting_insulin = ["determir","levemir"]
    long_acting_insulin = ["glargine","lantus"]


    # find which agent category the agent belongs to, and assign weight change result
    if (agent in biguanide) or (agent in sglt2_inhibitor):
        result = "likelihood of weight loss"

    elif (agent in sulfonylureas) or (agent in non_sulfonylurea_insulin_secretogogues) or (agent in rapid_acting_insulin) or (agent in short_acting_insulin) or (agent in intermediate_acting_insulin) or (agent in long_acting_insulin):
        result = "likelihood of weight gain"

    elif (agent in alpha_glucosidase_inhibitor) or (agent in dpp4_inhibitor):
        result = "likelihood of no weight change"

    elif agent in thiazolidinedione:
        result = "high likelihood of weight gain"

    elif (agent in incretin_mimetic) or (agent in amylinomimetic):
        result = "high likelihood of weight loss"


    return result

# test function to make sure code is working properly
def test():
    if execute({"agent":"Glucophage XR"}) != "likelihood of weight loss":
        return "error."
    if execute({"agent":"GLYNASE"})!= "likelihood of weight gain":
        return "error."
    if execute({"agent":"Pioglitazone"})!= "high likelihood of weight gain":
        return "error."
    if execute({"agent":"glyset"}) != "likelihood of no weight change":
        return "error."
    if execute({"agent":"nateglinide"}) != "likelihood of weight gain":
        return "error."
    if execute({"agent":"saxaglipton"}) != "likelihood of no weight change":
        return "error."
    if execute({"agent":"farxiga"}) != "likelihood of weight loss":
        return "error."
    if execute({"agent":"exenatide extended-release"}) != "high likelihood of weight loss":
        return "error."
    if execute({"agent":"pramlintide"}) != "high likelihood of weight loss":
        return "error."
    if execute({"agent":"novolog"}) != "likelihood of weight gain":
        return "error."
    if execute({"agent":"nph"}) != "likelihood of weight gain":
        return "error."
    if execute({"agent":"determir"}) != "likelihood of weight gain":
        return "error."
    if execute({"agent":"GLARGINE"}) != "likelihood of weight gain":
        return "error."
    if execute({"agent":""}) != "cannot calculate":
        return "error."
    return "ok."
