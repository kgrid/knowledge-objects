# input is an agent (generic or brand name), and output is a renal dose adjustment based on that agent
def agentRenalDoseAdjustment(inputs):
    agent = inputs["agent"].lower()

    result = "cannot calculate"

    amylinomimetic = ["pramlintide","symlin"]
    rapid_acting_insulin = ["lispro","humalog","aspart","novolog","glulisine","apidra"]
    short_acting_insulin = ["regular","nph"]
    intermediate_acting_insulin = ["determir","levemir"]
    long_acting_insulin = ["glargine","lantus"]


    if (agent == "metformin") or (agent == "glucophage") or (agent == "metformin extended relase") or (agent == "glucophage xr"):
        result = "Contraindicated in patients with an eGRF between 30-45 mL/minute/1.73 m^2 is not recommended"

    elif (agent == "glimepiride") or (agent == "amaryl") or (agent == "glyburide") or (agent == "diabeta, micronase") or (agent == "glyburide, micronized") or (agent == "glynase"):
        result = "Dose adjust for renal patients"

    elif (agent == "glipizide") or (agent == "glucotrol") or (agent == "glipizide xl") or (agent == "glucotrol xl"):
        result = "Preferred in class for renal patients given greater hepatic metabolism"

    elif (agent == "pioglitazone") or (agent == "actos") or (agent == "nateglinide") or (agent == "starlix") or (agent == "linagliptin") or (agent == "tradjenta"):
        result = "None"

    elif (agent == "acarbose") or (agent == "precose") or (agent == "miglitol") or (agent == "glyset"):
        result = "Contraindicated for CrCl <25 ml/min"

    elif (agent == "repaglinide") or (agent == "prandin"):
        result = "Dose adjustment for CrCl <40 ml/min"

    elif (agent == "sitagliptin") or (agent == "januvia") or (agent == "saxaglipton") or (agent == "onglyza"):
        result = "Dose adjustment for CrCl <50 ml/min"

    elif (agent == "alogliptin") or (agent == "nesina") or (agent == "canagliflozin") or (agent == "invokana"):
        result = "Dose adjustment for CrCl <60 ml/min"

    elif (agent == "dapagliflozin") or (agent == "farxiga") or (agent == "empagliflozin") or (agent == "jardiance"):
        result = "Not recommended for eGFR <45 mL/minute/1.73 m2"

    elif (agent == "exenatide") or (agent == "byetta") or (agent == "exenatide extended-release") or (agent == "bydureon"):
        result = "Contraindicated for CrCl <30 ml/min"

    elif (agent == "liraglutide") or (agent == "victoza"):
        result = "Limited data; use with caution"

    elif (agent == "dulaglutide") or (agent == "trulicity") or (agent == "albiglutide") or (agent == "tanzeum"):
        result = "None. Use caution when initiating or escalating doses"

    elif (agent in rapid_acting_insulin) or (agent in short_acting_insulin) or (agent in amylinomimetic) or (agent in intermediate_acting_insulin) or (agent in long_acting_insulin):
        result = "None"

    return result


# test function
def test():
    if agentRenalDoseAdjustment({"agent":"glucophage xr"}) != "Contraindicated in patients with an eGRF between 30-45 mL/minute/1.73 m^2 is not recommended":
        return "error."
    if agentRenalDoseAdjustment({"agent":"GLYBURIDE, MICRONIZED"}) != "Dose adjust for renal patients":
        return "error."
    if agentRenalDoseAdjustment({"agent":"glucotrol"}) != "Preferred in class for renal patients given greater hepatic metabolism":
        return "error."
    if agentRenalDoseAdjustment({"agent":"pioglitazone"}) != "None":
        return "error."
    if agentRenalDoseAdjustment({"agent":"miglitol"}) != "Contraindicated for CrCl <25 ml/min":
        return "error."
    if agentRenalDoseAdjustment({"agent":"starlix"}) != "None":
        return "error."
    if agentRenalDoseAdjustment({"agent":"Repaglinide"}) != "Dose adjustment for CrCl <40 ml/min":
        return "error."
    if agentRenalDoseAdjustment({"agent":"ALOGLIPTIN"}) != "Dose adjustment for CrCl <60 ml/min":
        return "error."
    if agentRenalDoseAdjustment({"agent":"Dapagliflozin"}) != "Not recommended for eGFR <45 mL/minute/1.73 m2":
        return "error."
    if agentRenalDoseAdjustment({"agent":"bydureon"}) != "Contraindicated for CrCl <30 ml/min":
        return "error."
    if agentRenalDoseAdjustment({"agent":""}) != "cannot calculate":
        return "error."
    if agentRenalDoseAdjustment({"agent":"levemir"}) != "None":
        return "error."
    return "ok."

print test()
