# Step 3. If above agents are contraindicated or dose is optimized and patients BP remains >= 140/90
def therapyRecommendation3(inputs):
    systolic = inputs["systolic"]
    diastolic = inputs["diastolic"]
    high_bp = bloodPressureCheck(systolic,diastolic)
    if high_bp == False:
        return "Not applicable, patient doesn't have high blood pressure."
    elif high_bp != True:
        return high_bp
    else:
        #print ("If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90-" + "\n" + "Add a Dihydropyridine Calcium Channel Blocker - initiate therapy" + "\n" + "Amlodipine (Norvasc) 2.5-2mg daily. Titrate by doubling dose in 2-4 weeks if BP goal is NOT met (max dose: 10mg)")
        return ("If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90-" + "\n" + "Add a Dihydropyridine Calcium Channel Blocker - initiate therapy" + "\n" + "Amlodipine (Norvasc) 2.5-2mg daily. Titrate by doubling dose in 2-4 weeks if BP goal is NOT met (max dose: 10mg)")

# Check for high BP
def bloodPressureCheck(systolic,diastolic):
    if (systolic == 0) & (diastolic == 0):
        #print "No systolic or diastolic information provided. Cannot calculate."
        return "No systolic or diastolic information provided. Cannot calculate."
    elif systolic >= 140:
        high_bp = True
    elif (diastolic >= 90):
        high_bp = True
    else:
        high_bp = False
    return high_bp


# Test function. Run before use.
def test():
    if therapyRecommendation3({"systolic":0,"diastolic":0}) != "No systolic or diastolic information provided. Cannot calculate.":
        return "error."
    if therapyRecommendation3({"systolic":10,"diastolic":0}) != "Not applicable, patient doesn't have high blood pressure.":
        return "error."
    if therapyRecommendation3({"systolic":150,"diastolic":90}) != ("If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90-" + "\n" + "Add a Dihydropyridine Calcium Channel Blocker - initiate therapy" + "\n" + "Amlodipine (Norvasc) 2.5-2mg daily. Titrate by doubling dose in 2-4 weeks if BP goal is NOT met (max dose: 10mg)"):
        return "error."
    if therapyRecommendation3({"systolic":0,"diastolic":110}) != ("If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90-" + "\n" + "Add a Dihydropyridine Calcium Channel Blocker - initiate therapy" + "\n" + "Amlodipine (Norvasc) 2.5-2mg daily. Titrate by doubling dose in 2-4 weeks if BP goal is NOT met (max dose: 10mg)"):
        return "error."
    return "ok."
