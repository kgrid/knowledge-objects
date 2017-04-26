from math import exp
import math

# PLCOm2012 model (Tammemagi,NEJM,2013)
# Author          Kevin ten Haaf
# Organization    Erasmus Medical Center Rotterdam
# Last adjusted: April 25, 2017
def execute(info):

    #age,edLevel,bmi,copd,hxLungCancer,famHxCanc,race,smokerStatus,cigsPerDay,smokDurat,yrsQuit)
    age = int(info['age'])
    edLevel = info['edLevel']
    bmi = float(info['bmi'])
    copd = int(info['copd'])
    hxLungCancer = int(info['hxLungCancer'])
    famHxCanc = int(info['famHxCanc'])
    race = int(info['race'])
    smokerStatus = 0 if info['yrsQuit'] else 1
    cigsPerDay = int(info['cigsPerDay'])
    smokDurat = int(info['smokDurat'])
    yrsQuit = int(info['yrsQuit'])

    #coeffs: age, edLevel, bmi, copd, personal history, family history, smoking status, cigsPerDay, smoking duration, years since cessation
    Coeffs=[-1, 0.0778868,-0.0812744,-0.0274194,0.3553063,0.4589971,0.587185,0.2597431,-1.822606,0.0317321,-0.0308572]
    Racecoeffs=[-1, 0,0.3944778,-0.7434744,-0.466585,0,1.027152]


    #First the center values for the variables are defined
    agecentervalue = 62.0
    edLevelcentervalue = 4.0
    bmicentervalue = 27.0
    cigsPerDaycentervalue =0.4021541613
    Smokingdurationcentervalue = 27.0
    Smokingcessationcentervalue = 10.0

    #Then each model parameter's contribution is calculated

    Modelconstant=-4.532506

    Agecontribution = (age-agecentervalue)*Coeffs[1]
    #print 'Agecontribution= %s' % Agecontribution

    edLevelcontribution = (edLevel-edLevelcentervalue)*Coeffs[2]
    #print 'edLevelcontribution= %s' % edLevelcontribution

    Bmicontribution = (bmi-bmicentervalue)*Coeffs[3]
    #print 'Bmicontribution= %s' % Bmicontribution

    Copdcontribution = copd*Coeffs[4]
    #print 'Copdcontribution= %s' % Copdcontribution

    hxLungCancercontribution = hxLungCancer*Coeffs[5]
    #print 'hxLungCancercontribution= %s' % hxLungCancercontribution

    famHxCanccontribution= famHxCanc*Coeffs[6]
    #print 'famHxCanccontribution= %s' % famHxCanccontribution

    Smokingstatuscontribution= smokerStatus*Coeffs[7]
    #print 'Smokingstatuscontribution= %s' % Smokingstatuscontribution

    if cigsPerDay:
        cigsPerDaycontribution = ( math.pow((cigsPerDay / 10.0), -1 )-cigsPerDaycentervalue)*Coeffs[8]
    else:
        cigsPerDaycontribution = (0-cigsPerDaycentervalue)*Coeffs[8]
    #print 'cigsPerDaycontribution= %s %s %s %s ' % ( cigsPerDaycontribution, cigsPerDay, cigsPerDaycentervalue, Coeffs[8])

    Smokingdurationcontribution = (smokDurat-Smokingdurationcentervalue )*Coeffs[9]
    #print 'Smokingdurationcontribution= %s' % Smokingdurationcontribution

    Smokingcessationcontribution = (yrsQuit-Smokingcessationcentervalue)*Coeffs[10]
    #print 'Smokingcessationcontribution= %s' % Smokingcessationcontribution

    Racecontribution = Racecoeffs[race]
    #print 'Racecontribution= %s' % Racecontribution

    #The individual contributions are summed and the 6-year probability is returned
    Sumvalues = Modelconstant+Agecontribution+edLevelcontribution+Bmicontribution+Copdcontribution+hxLungCancercontribution+famHxCanccontribution+Smokingstatuscontribution+cigsPerDaycontribution+Smokingdurationcontribution+Smokingcessationcontribution+Racecontribution
    #print 'Sumvalues= %s' % Sumvalues

    Sixyearprobabilitypercentage = 100 * exp(Sumvalues)/(1+exp(Sumvalues))
    Sixyearprobabilitypercentage = round(Sixyearprobabilitypercentage,2)
    #return float(Sixyearprobabilitypercentage)
    return "This individual's six year probability of developing lung cancer is " + str(float(Sixyearprobabilitypercentage)) + "%."



def test():
    if execute({"age":0,"edLevel":0,"bmi":0,"copd":0,"hxLungCancer":0,"famHxCanc":0,"race":0,"cigsPerDay":0,"smokDurat":0,"yrsQuit":0}) != "This individual's six year probability of developing lung cancer is 0.01%.":
        return "error."
    if execute({"age":70,"edLevel":0,"bmi":0,"copd":0,"hxLungCancer":1,"famHxCanc":1,"race":0,"cigsPerDay":0,"smokDurat":0,"yrsQuit":0}) != "This individual's six year probability of developing lung cancer is 8.68%.":
        return "error."
    if execute({"age":80,"edLevel":2,"bmi":0,"copd":1,"hxLungCancer":1,"famHxCanc":1,"race":0,"cigsPerDay":15,"smokDurat":0,"yrsQuit":0}) != "This individual's six year probability of developing lung cancer is 6.93%.":
        return "error."
    return "ok."
