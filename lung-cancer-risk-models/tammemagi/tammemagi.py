from math import exp
import math

# PLCOm2012 model (Tammemagi,NEJM,2013)
# Author          Kevin ten Haaf
# Organization    Erasmus Medical Center Rotterdam
#Last adjusted: June 19 2014
def getSixyearprobability(info):

    #currentage,education,bmi,copd,personalhistory,familyhistory,race,currentsmokingstatus,averageCPD,currentsmokingduration,currentyearsquit)
    currentage = int(info['age'])
    education = info['edLevel']
    bmi = float(info['bmi'])
    copd = int(info['hxNonLungCancerDz'])
    personalhistory = int(info['hxLungCancer'])
    familyhistory = int(info['hxLungCancerFam'])
    race = int(info['ethnicity'])
    currentsmokingstatus = 0 if info['yrsQuit'] else 1
    averageCPD = int(info['cigsPerDay'])
    currentsmokingduration = int(info['yrsSmoker'])
    currentyearsquit = int(info['yrsQuit'])

    #coeffs: age, education, bmi, copd, personal history, family history, smoking status, cpd, smoking duration, years since cessation
    Coeffs=[-1, 0.0778868,-0.0812744,-0.0274194,0.3553063,0.4589971,0.587185,0.2597431,-1.822606,0.0317321,-0.0308572]
    Racecoeffs=[-1, 0,0.3944778,-0.7434744,-0.466585,0,1.027152]


    #First the center values for the variables are defined
    agecentervalue = 62.0
    educationcentervalue = 4.0
    bmicentervalue = 27.0
    CPDcentervalue =0.4021541613
    Smokingdurationcentervalue = 27.0
    Smokingcessationcentervalue = 10.0

    #Then each model parameter's contribution is calculated

    Modelconstant=-4.532506

    Agecontribution = (currentage-agecentervalue)*Coeffs[1]
    #print 'Agecontribution= %s' % Agecontribution

    Educationcontribution = (education-educationcentervalue)*Coeffs[2]
    #print 'Educationcontribution= %s' % Educationcontribution

    Bmicontribution = (bmi-bmicentervalue)*Coeffs[3]
    #print 'Bmicontribution= %s' % Bmicontribution

    Copdcontribution = copd*Coeffs[4]
    #print 'Copdcontribution= %s' % Copdcontribution

    Personalhistorycontribution = personalhistory*Coeffs[5]
    #print 'Personalhistorycontribution= %s' % Personalhistorycontribution

    Familyhistorycontribution= familyhistory*Coeffs[6]
    #print 'Familyhistorycontribution= %s' % Familyhistorycontribution

    Smokingstatuscontribution= currentsmokingstatus*Coeffs[7]
    #print 'Smokingstatuscontribution= %s' % Smokingstatuscontribution

    if averageCPD:
        CPDcontribution = ( math.pow((averageCPD / 10.0), -1 )-CPDcentervalue)*Coeffs[8]
    else:
        CPDcontribution = (0-CPDcentervalue)*Coeffs[8]
    #print 'CPDcontribution= %s %s %s %s ' % ( CPDcontribution, averageCPD, CPDcentervalue, Coeffs[8])

    Smokingdurationcontribution = (currentsmokingduration-Smokingdurationcentervalue )*Coeffs[9]
    #print 'Smokingdurationcontribution= %s' % Smokingdurationcontribution

    Smokingcessationcontribution = (currentyearsquit-Smokingcessationcentervalue)*Coeffs[10]
    #print 'Smokingcessationcontribution= %s' % Smokingcessationcontribution

    Racecontribution = Racecoeffs[race]
    #print 'Racecontribution= %s' % Racecontribution

    #The individual contributions are summed and the 6-year probability is returned
    Sumvalues = Modelconstant+Agecontribution+Educationcontribution+Bmicontribution+Copdcontribution+Personalhistorycontribution+Familyhistorycontribution+Smokingstatuscontribution+CPDcontribution+Smokingdurationcontribution+Smokingcessationcontribution+Racecontribution
    #print 'Sumvalues= %s' % Sumvalues

    Sixyearprobabilitypercentage = 100 * exp(Sumvalues)/(1+exp(Sumvalues))

    return float(Sixyearprobabilitypercentage)