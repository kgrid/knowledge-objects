from math import exp
def execute(inputs):
    smokerStatus = inputs["smokerStatus"]
    smokingDuration = inputs["smokingDuration"]
    age = inputs["age"]

    b = beta_1 * x
    a = (1-exp(exp(b*c)))
    # i.e. calcC("current","cancer",20)
    c = calcC(smokerStatus,survivorStatus,smokingDuration,age)

def calcB():
    # sex: female = 1, male =0
    covariates = ["sex","BMI","education level","hay fever","asthma","family history of cancer","chr15q25","chr5p15","silica","pah","metal","asbestos"]
    print "temp"

def calcC(smokerStatus,survivorStatus,smokingDuration,age):
    s = smokingDuration
    lam = 0
    gamma = 0
    lam = 0
    gamma = 0
    # current smoker, cancer
    if (smokerStatus == "current") & (survivorStatus == "cancer"):
        if (age <= 18):
            lam = 3.819
            gamma = 0.9999
        elif ((age > 18) & (age <=20)):
            lam = 4.056
            gamma = 1.071
        elif ((age > 20) & (age <=22)):
            lam = 4.230
            gamma = 1.298
        elif ((age > 22) & (age <=24)):
            lam = 4.339
            gamma = 1.518
        elif ((age > 24) & (age <=26)):
            lam = 4.380
            gamma = 1.679
        elif ((age > 26) & (age <=28)):
            lam = 4.567
            gamma = 1.517
        elif ((age > 28) & (age <=30)):
            lam = 4.506
            gamma = 1.615
        elif (age > 30):
            lam = 4.504
            gamma = 1.684


    # current smoker, death
    if (smokerStatus == "current") & (survivorStatus == "death"):
        if (age <= 18):
            lam = 3.690
            gamma = 1.220
        elif ((age > 18) & (age <=20)):
            lam = 3.774
            gamma = 1.312
        elif ((age > 20) & (age <=22)):
            lam = 3.859
            gamma = 1.560
        elif ((age > 22) & (age <=24)):
            lam = 3.944
            gamma = 1.775
        elif ((age > 24) & (age <=26)):
            lam = 3.979
            gamma = 1.925
        elif ((age > 26) & (age <=28)):
            lam = 4.049
            gamma = 1.854
        elif ((age > 28) & (age <=30)):
            lam = 4.096
            gamma = 1.838
        elif (age > 30):
            lam = 4.069
            gamma = 1.912

    # former smoker, cancer
    if (smokerStatus == "former") & (survivorStatus == "cancer"):
        if (age <= 22):
            if (s<= 20):
                lam = 4.987
                gamma = 0.750
            if ((s>=30) & (s >20)):
                lam = 4.723
                gamma = 0.819
            if (s>30):
                lam = 4.321
                gamma = 1.032

        if (age <= 26 & age >22):
            if (s<= 20):
                lam =5.179
                gamma = 0.750
            if ((s<=30) & (s >20)):
                lam = 4.786
                gamma = 1.353
            if ((s>30) & (s <= 36)):
                lam = 4.651
                gamma = 1.460
            if ((s>36) & (s <= 42)):
                lam = 4.654
                gamma = 1.318
            if (s>42):
                lam = 4.366
                gamma = 1.662

        if (age >26):
            if (s<= 20):
                lam =5.563
                gamma =1.088
            if ((s<=30) & (s >20)):
                lam = 4.680
                gamma = 1.705
            if ((s>30) & (s <= 36)):
                lam = 4.491
                gamma = 1.879
            if ((s>36) & (s <= 42)):
                lam = 4.241
                gamma = 2.336
            if (s>42):
                lam = 4.177
                gamma = 2.574

    # former smoker, death
    if (smokerStatus == "former") & (survivorStatus == "death"):
        if (age <= 22):
            if (s<= 20):
                lam = 3.754
                gamma = 1.210
            if ((s>=30) & (s >20)):
                lam = 3.750
                gamma = 1.511
            if (s>30):
                lam = 3.8
                gamma = 1.669

        if (age <= 26 & age >22):
            if (s<= 20):
                lam =4.008
                gamma = 1.621
            if ((s<=30) & (s >20)):
                lam = 3.975
                gamma = 1.742
            if ((s>30) & (s <= 36)):
                lam = 3.954
                gamma = 1.835
            if ((s>36) & (s <= 42)):
                lam = 3.928
                gamma = 2.129
            if (s>42):
                lam = 3.982
                gamma = 2.150

        if (age >26):
            if (s<= 20):
                lam =4.123
                gamma =1.769
            if ((s<=30) & (s >20)):
                lam = 4.058
                gamma = 1.865
            if ((s>30) & (s <= 36)):
                lam = 4.020
                gamma = 2.148
            if ((s>36) & (s <= 42)):
                lam = 3.999
                gamma = 2.360
            if (s>42):
                lam = 4.041
                gamma = 2.490

    print lam
    print gamma

    c = (((age/lam)**gamma) - (((age+1)/lam)**gamma))
    return c


def test():
    if str(calcC("former","death",40,48)) != "-17.5759666625":
        return "error."
    return "ok."

execute({"smokerStatus":"former","smokingDuration":40,"age":48})
