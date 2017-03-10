# Input drug name (generic name and brand name), output weight change information
def weightChangeInformative(inputs):
    agent = inputs["agent"]
    agent = agent.lower()

    biguanide = ["metformin","glucophage", "metaformin extended release","glucophage xr","glimepiride"]
    sulfonylureas = ["glimepiride","amaryl","glipizide","glucotrol","glipizide xl","glucotrol xl","glyburide","diabeta","micronase","glyburide, micronized","glynase"]
    thiazolidinedione = ["pioglitazone","actos"]
    alpha_glucosidaseInhibitor = ["acarbose","precose","miglitol","glyset"]
    non_sulfonylurea_insulin_secretagogues =["repaglinide","prandin","nateglinide","starlix"]


    if agent in biguanide:
        return "likelihood of weight loss"

    if agent in sulfonylureas:
        return "likelihood of weight gain"

    if agent in thiazolidinedione:
        return "high likelihood of weight gain"

    if agent in alpha_glucosidaseInhibitor:
        return "no likelihood of weight change"

    if agent in non_sulfonylurea_insulin_secretagogues:
        return "likelihood of weight gain"





print weightChangeInformative({"agent":"metformin"})
print weightChangeInformative({"agent":"glyburide, micronized"})
print weightChangeInformative({"agent":"pioglitazone"})
print weightChangeInformative({"agent":"miglitol"})
print weightChangeInformative({"agent":"starlix"})
