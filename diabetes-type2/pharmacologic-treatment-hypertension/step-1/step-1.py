# Step 1. Elevated BP (systolic BP >= 140 and/or diastolic BP>= 90) uncontrolled by prior lifestyle.
# https://www.kidney.org/atoz/content/albuminuria < 30mg/24hrs normal, 30-300mg/24hrs microalbuminuria, >300mgs/24hrs macroalbuminuria

def execute(inputs):
    systolic = inputs["systolic"]
    diastolic = inputs["diastolic"]
    albuminLevel = inputs["albuminLevel"]
    # Check for high BP
    high_bp = bloodPressureCheck(systolic,diastolic)
    if high_bp != True:
        #print high_bp
        return high_bp

    diagnosis = albuminDiagnosis(albuminLevel)

    if diagnosis == "normal":
        #print ("Without microalbuminuria-" + "\n" + "initiate therapy with either: " + "\n" + "(1) Thiazide diuretic - initiate therapy. " + "\n" + "(a) Chlorthalidone 25mg/day. Titrate by doubling dose in 2-4 weeks if BP goal NOT met. (max dose: 50mg daily)" + "\n" + "(b) Hydrochlorothiazide 12.5mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT met. (max dose: 25mg daily)."+ "\n" + "(2) ACE inhibitor (Angiotensin-Converting Enzyme) Inhibitor- initiate therapy unless contraindication (hypersensitivity reaction, angioedema) or documented persistent cought."+ "\n" +"(a) Lisinopril 10mg daily. Titrate by doubling dose every 2-4 weeks until the BP goal is met (max dose: 40mg)."+ "\n" + "(3) If ACE inhibitory contraindicated: Angiotensin II Receptor Blocker (ARB)."+ "\n" +"(a) Losartan 24-50mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT med (max dose: 100mg)")
        return ("Without microalbuminuria-" + "\n" + "initiate therapy with either: " + "\n" + "(1) Thiazide diuretic - initiate therapy. " + "\n" + "(a) Chlorthalidone 25mg/day. Titrate by doubling dose in 2-4 weeks if BP goal NOT met. (max dose: 50mg daily)" + "\n" + "(b) Hydrochlorothiazide 12.5mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT met. (max dose: 25mg daily)."+ "\n" + "(2) ACE inhibitor (Angiotensin-Converting Enzyme) Inhibitor- initiate therapy unless contraindication (hypersensitivity reaction, angioedema) or documented persistent cought."+ "\n" +"(a) Lisinopril 10mg daily. Titrate by doubling dose every 2-4 weeks until the BP goal is met (max dose: 40mg)."+ "\n" + "(3) If ACE inhibitory contraindicated: Angiotensin II Receptor Blocker (ARB)."+ "\n" +"(a) Losartan 24-50mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT med (max dose: 100mg)")
    elif diagnosis == "macroalbuminuria":
        return "Albumin levels indicate macroalbuminuria."
    elif diagnosis == "microalbuminuria":
        #print ("With microalbiminuria-" + "\n" + "(1) ACE Inhibitor- initiate therapy unless contraindication (hypersensitivity reaction, angioedema) or documented persistent cough." + "\n" + "(a) Lisinopril 10mg daily. Titrate by doubling dose every 2-4 weeks until the BP goal is met (max dose: 40mg)" + "\n" + "(2) If ACE inhibitor contraindicated: Angiotensin II Receptor BLOCKER (ARB)" + "\n" + "(a) Losartan 25-50mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT met (max dose: 100mg)")
        return ("With microalbiminuria-" + "\n" + "(1) ACE Inhibitor- initiate therapy unless contraindication (hypersensitivity reaction, angioedema) or documented persistent cough." + "\n" + "(a) Lisinopril 10mg daily. Titrate by doubling dose every 2-4 weeks until the BP goal is met (max dose: 40mg)" + "\n" + "(2) If ACE inhibitor contraindicated: Angiotensin II Receptor BLOCKER (ARB)" + "\n" + "(a) Losartan 25-50mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT met (max dose: 100mg)")
    else:
        return diagnosis

# Check for high BP
def bloodPressureCheck(systolic,diastolic):
        if (systolic == 0) & (diastolic ==0):
            #print "No systolic or diastolic information provided. Cannot calculate."
            return "No systolic or diastolic information provided. Cannot calculate."
        elif systolic >= 140:
            high_bp = True
        elif diastolic >= 90:
            high_bp = True
        else:
            high_bp = False

        if high_bp == False:
            #print "Not applicable, patient doesn't have high blood pressure."
            return "Not applicable, patient doesn't have high blood pressure."
        return high_bp

# Albumin level interpretation
def albuminDiagnosis(albuminLevel):
    if albuminLevel == 0:
        return "No albumin level information provided. Cannot calculate."
    elif albuminLevel <30:
        diagnosis = "normal"
    elif (albuminLevel >= 30) & (albuminLevel<= 300):
        diagnosis = "microalbuminuria"
    elif albuminLevel > 300:
        diagnosis = "macroalbuminuria"
    else:
        diagnosis = "cannot calculate"
    return diagnosis


# Test function. Run before use.
def test():
    if execute({"systolic":0,"diastolic":0,"albuminLevel":20}) != "No systolic or diastolic information provided. Cannot calculate.":
        return "error."
    if execute({"systolic":10,"diastolic":0,"albuminLevel":230}) != "Not applicable, patient doesn't have high blood pressure.":
        return "error."
    if execute({"systolic":150,"diastolic":90,"albuminLevel":230}) != ("With microalbiminuria-" + "\n" + "(1) ACE Inhibitor- initiate therapy unless contraindication (hypersensitivity reaction, angioedema) or documented persistent cough." + "\n" + "(a) Lisinopril 10mg daily. Titrate by doubling dose every 2-4 weeks until the BP goal is met (max dose: 40mg)" + "\n" + "(2) If ACE inhibitor contraindicated: Angiotensin II Receptor BLOCKER (ARB)" + "\n" + "(a) Losartan 25-50mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT met (max dose: 100mg)"):
        return "error."
    if execute({"systolic":0,"diastolic":110,"albuminLevel":20}) != ("Without microalbuminuria-" + "\n" + "initiate therapy with either: " + "\n" + "(1) Thiazide diuretic - initiate therapy. " + "\n" + "(a) Chlorthalidone 25mg/day. Titrate by doubling dose in 2-4 weeks if BP goal NOT met. (max dose: 50mg daily)" + "\n" + "(b) Hydrochlorothiazide 12.5mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT met. (max dose: 25mg daily)."+ "\n" + "(2) ACE inhibitor (Angiotensin-Converting Enzyme) Inhibitor- initiate therapy unless contraindication (hypersensitivity reaction, angioedema) or documented persistent cought."+ "\n" +"(a) Lisinopril 10mg daily. Titrate by doubling dose every 2-4 weeks until the BP goal is met (max dose: 40mg)."+ "\n" + "(3) If ACE inhibitory contraindicated: Angiotensin II Receptor Blocker (ARB)."+ "\n" +"(a) Losartan 24-50mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT med (max dose: 100mg)"):
        return "error."
    if execute({"systolic":300,"diastolic":0,"albuminLevel":400}) != "Albumin levels indicate macroalbuminuria.":
        return "error."
    if execute({"systolic":300,"diastolic":0,"albuminLevel":0}) != "No albumin level information provided. Cannot calculate.":
        return "error."
    return "ok."
