# Step 4. If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90

def execute(inputs):
    systolic = inputs["systolic"]
    diastolic = inputs["diastolic"]
    high_bp = bloodPressureCheck(systolic,diastolic)

    if high_bp == False:
        #print "Not applicable, patient doesn't have high blood pressure."
        return "Not applicable, patient doesn't have high blood pressure."
    elif high_bp != True:
        return high_bp

    else:
        #print ("If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90" + "\n" + "Add a Beta-Blocker to the first two agents. Initiate therapy with either metoprolol (preferred) or atenolol:" + "\n" + "(a) Metroprolol tartate 25 to 50mg BID. Titrate by doubling dose every 2-4 weeks until BP goal met (max dose: 200mg)" + "\n" + "(b) Atenolol 25mg daily. Titrate by doubling dose every 2-4 weeks until BP goal met (max dose: 100mg)")
        return ("If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90" + "\n" + "Add a Beta-Blocker to the first two agents. Initiate therapy with either metoprolol (preferred) or atenolol:" + "\n" + "(a) Metroprolol tartate 25 to 50mg BID. Titrate by doubling dose every 2-4 weeks until BP goal met (max dose: 200mg)" + "\n" + "(b) Atenolol 25mg daily. Titrate by doubling dose every 2-4 weeks until BP goal met (max dose: 100mg)")

# Check for high BP
def bloodPressureCheck(systolic,diastolic):
        if (systolic == 0) and (diastolic) == 0:
            #print "No systolic or diastolic information provided. Cannot calculate."
            return "No systolic or diastolic information provided. Cannot calculate."
        elif systolic >= 140:
            high_bp = True
        elif diastolic >= 90:
            high_bp = True
        else:
            high_bp = False

        return high_bp

# Test function. Run before use.
def test():
    if execute({"systolic":0,"diastolic":0}) != "No systolic or diastolic information provided. Cannot calculate.":
        return "error."
    if execute({"systolic":10,"diastolic":0}) != "Not applicable, patient doesn't have high blood pressure.":
        return "error."
    if execute({"systolic":150,"diastolic":90}) != ("If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90" + "\n" + "Add a Beta-Blocker to the first two agents. Initiate therapy with either metoprolol (preferred) or atenolol:" + "\n" + "(a) Metroprolol tartate 25 to 50mg BID. Titrate by doubling dose every 2-4 weeks until BP goal met (max dose: 200mg)" + "\n" + "(b) Atenolol 25mg daily. Titrate by doubling dose every 2-4 weeks until BP goal met (max dose: 100mg)"):
        return "error."
    if execute({"systolic":0,"diastolic":110}) !=  ("If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90" + "\n" + "Add a Beta-Blocker to the first two agents. Initiate therapy with either metoprolol (preferred) or atenolol:" + "\n" + "(a) Metroprolol tartate 25 to 50mg BID. Titrate by doubling dose every 2-4 weeks until BP goal met (max dose: 200mg)" + "\n" + "(b) Atenolol 25mg daily. Titrate by doubling dose every 2-4 weeks until BP goal met (max dose: 100mg)"):
        return "error."
    return "ok."
