from math import exp
import math


def getFiveYearHCCRisk(info):

    gender = info['gender']
    currentage = int(info['age'])
    paramALT = int(info['ALT'])
    paramHBeAg = int(info['HBeAg'])
    paramHBVDNAlevel = long(info['HBVDNAlevel'])

    paramGender = 0
    if gender == 'M' or gender == 'm': 
        paramGender = 1
    
    
    
    P0forFiveYearHCCRisk = 0.99650 
    
    maleCoef = 0.78798  
    ageCoef = 0.09859
    ALTCoef = 0 
    if paramALT >= 15 and paramALT <= 44 :
        ALTCoef = 0.38823
    elif  paramALT >= 45 :
            ALTCoef = 0.96311
            

    
    HBeAgCoef = 0; 
    if paramHBeAg > 0  :
        HBeAgCoef = 0.81308
        
    HBVDNAlevelCoef = 0 
    if paramHBVDNAlevel >= 300 and paramHBVDNAlevel <= 9999:
        HBVDNAlevelCoef = 0.11648
    elif paramHBVDNAlevel >= 10000 and paramHBVDNAlevel <= 99999:
        HBVDNAlevelCoef = 1.31467
    elif paramHBVDNAlevel >= 100000 and paramHBVDNAlevel <= 999999: 
        HBVDNAlevelCoef = 2.27028
    elif paramHBVDNAlevel >= 1000000 :
        HBVDNAlevelCoef = 2.09258
                    
    finalExValue =  maleCoef * paramGender + currentage * ageCoef +  ALTCoef + paramHBeAg * HBeAgCoef +  HBVDNAlevelCoef - 6.12796
    
    threeYearHCCRisk = 1 - math.pow( P0forFiveYearHCCRisk, math.exp(finalExValue) )
    
    return float(threeYearHCCRisk * 100 )
    
info = {'gender': 'M', 'age': 60, 'ALT': 47, 'HBeAg': 1, 'HBVDNAlevel': 99999 }  

print getFiveYearHCCRisk(info) 
