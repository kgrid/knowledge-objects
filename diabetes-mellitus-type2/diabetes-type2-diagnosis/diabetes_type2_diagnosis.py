'''
Risk Module of Type II Diabetes
Created: December 20, 2016
This KO is derived from table 1: Diagnosis of Diabetes: Diagnostic tests and Glucose Levels.
'''
#diabetesDiagnosis({"diagnosticTest":"hemoglobin A1c","glucoseLevel":6})

def diabetesDiagnosis(inputs):
    diagnosticTest = inputs["diagnosticTest"]
    glucoseLevel = inputs["glucoseLevel"]

    if glucoseLevel == 0:
        #print ("glucoseLevel = 0, No glucose level provided")
        return ("glucoseLevel = 0, No glucose level provided")

    diagnosis = ""
    if diagnosticTest == "hemoglobin A1c":
        if glucoseLevel < 5.7:
            diagnosis = "normal"
        elif glucoseLevel > 5.7 and glucoseLevel < 6.4:
            diagnosis = "pre-diabetes"
        elif glucoseLevel >= 6.5:
            diagnosis = "diabetes"

    elif diagnosticTest == "fasting plasma glucose (mg/dL)":
        if glucoseLevel < 100:
            diagnosis = "normal"
        elif glucoseLevel >100 and glucoseLevel < 125:
            diagnosis = "pre-diabetes"
        elif glucoseLevel >= 126:
            diagnosis = "diabetes"

    elif diagnosticTest == "random plasma glucose (mg/dL)":
        if glucoseLevel < 130:
            diagnosis = "normal"
        elif glucoseLevel > 130 and glucoseLevel < 199:
            diagnosis = "pre-diabetes"
        elif glucoseLevel >= 200:
            diagnosis = "diabetes"

    elif diagnosticTest == "oral glucose tolerance test (OGTT)(mg/dL)":
        if glucoseLevel < 140:
            diagnosis = "normal"
        elif glucoseLevel > 10 and glucoseLevel < 199:
            diagnosis = "pre-diabetes"
        elif glucoseLevel >= 200:
            diagnosis = "diabetes"

    else:
        #print ("Incorrect diagnostic test. Diagnostic test can be: " + "\n" + "* hemoglobin A1c" + "\n" + "* fasting plasma glucose (mg/dL)" + "\n" + "* random plasma glucose (mg/dL)" + "\n" + "* oral glucose tolerance test (OGTT)(mg/dL)")
        return ("Incorrect diagnostic test. Diagnostic test can be: " + "\n" + "* hemoglobin A1c" + "\n" + "* fasting plasma glucose (mg/dL)" + "\n" + "* random plasma glucose (mg/dL)" + "\n" + "* oral glucose tolerance test (OGTT)(mg/dL)")

    #print diagnosis
    return diagnosis



def test():
    if diabetesDiagnosis({"diagnosticTest":"hemoglobin A1c","glucoseLevel":6}) == "pre-diabetes":
        print "ok"
    else:
        print "error"

    if diabetesDiagnosis({"diagnosticTest":"fasting plasma glucose (mg/dL)","glucoseLevel":180}) == "diabetes":
        print "ok"
    else:
        print "error"

    if diabetesDiagnosis({"diagnosticTest":"random plasma glucose (mg/dL)","glucoseLevel":120}) == "normal":
        print "ok"
    else:
        print "error"

    if diabetesDiagnosis({"diagnosticTest":"oral glucose tolerance test (OGTT)(mg/dL)","glucoseLevel":190}) == "pre-diabetes":
        print "ok"
    else:
        print "error"

    if diabetesDiagnosis({"diagnosticTest":"","glucoseLevel":190}) == "Incorrect diagnostic test. Diagnostic test can be: " + "\n" + "* hemoglobin A1c" + "\n" + "* fasting plasma glucose (mg/dL)" + "\n" + "* random plasma glucose (mg/dL)" + "\n" + "* oral glucose tolerance test (OGTT)(mg/dL)":
        print "ok"
    else:
        print "error"

    if diabetesDiagnosis({"diagnosticTest":"","glucoseLevel":0}) == "glucoseLevel = 0, No glucose level provided":
        print "ok"
    else:
        print "error"


test()
