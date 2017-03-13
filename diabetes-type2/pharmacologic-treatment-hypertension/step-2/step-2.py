# Step 2. If dose is optimized on agent from Step 1 and patient BP remains >= 140/90

def therapyRecommendation2(inputs):
    systolic = inputs["systolic"]
    diastolic = inputs["diastolic"]
    high_bp = bloodPressureCheck(systolic,diastolic)
    if high_bp != True:
        return high_bp
    else:
        #print ("If dose is optimized on agent from Step 1 and patient BP remains >= 140/90-" + "\n" + "Add a Thiazide diuretic or ACE/ARB to the first agent." + "\n" + "Consider combination therapy to reduce cost (e.g., lisinopril/HCTZ, losartan/HCTZ, atenolol/chlorthalidone)" + "\n" + "Do not use ACE inhibitor in combination with ARB as combination may increase risk of renal failure.")
        return ("If dose is optimized on agent from Step 1 and patient BP remains >= 140/90-" + "\n" + "Add a Thiazide diuretic or ACE/ARB to the first agent." + "\n" + "Consider combination therapy to reduce cost (e.g., lisinopril/HCTZ, losartan/HCTZ, atenolol/chlorthalidone)" + "\n" + "Do not use ACE inhibitor in combination with ARB as combination may increase risk of renal failure.")

# Check for high BP
def bloodPressureCheck(systolic,diastolic):
        if (systolic == 0) & (diastolic == 0):
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


# Test function. Run before use.
def test():
    if therapyRecommendation2({"systolic":0,"diastolic":0}) != "No systolic or diastolic information provided. Cannot calculate.":
        return "error."
    if therapyRecommendation2({"systolic":10,"diastolic":0}) != "Not applicable, patient doesn't have high blood pressure.":
        return "error."
    if therapyRecommendation2({"systolic":150,"diastolic":90}) !=("If dose is optimized on agent from Step 1 and patient BP remains >= 140/90-" + "\n" + "Add a Thiazide diuretic or ACE/ARB to the first agent." + "\n" + "Consider combination therapy to reduce cost (e.g., lisinopril/HCTZ, losartan/HCTZ, atenolol/chlorthalidone)" + "\n" + "Do not use ACE inhibitor in combination with ARB as combination may increase risk of renal failure."):
        return "error."
    if therapyRecommendation2({"systolic":0,"diastolic":110}) != ("If dose is optimized on agent from Step 1 and patient BP remains >= 140/90-" + "\n" + "Add a Thiazide diuretic or ACE/ARB to the first agent." + "\n" + "Consider combination therapy to reduce cost (e.g., lisinopril/HCTZ, losartan/HCTZ, atenolol/chlorthalidone)" + "\n" + "Do not use ACE inhibitor in combination with ARB as combination may increase risk of renal failure."):
        return "error."
    return "ok."
