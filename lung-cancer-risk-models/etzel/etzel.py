# Etzel, Development and Validation of a Lung Cancer Risk Prediction Model for African-Americans (Etzel, et al,2008)
# Author: Kristen McGarry
# April 21st, 2017


# ODDS RATIOS
smokingStatus= {"former":3.38,"current":6.20}
currentSmokers = {"duration>30y":1.97,"numCigsDay>20":3.94,"pack-years>40":3.44,"mentholCigUse":0.69}
formerSmokers = {"duration>30y":2.43,"numCigsDay>20":1.75,"pack-years>40":2.74,"yrsCessation":0.42,"ageCessation>30y":2.60,"mentholCigUse":0.99}
envirExp = {"asb":1.58,"dust":1.50,"fiber":1.33,"svf":2.27,"benzene":1.17,"toluene/xylene":1.40,"dryCleaning":1.60,"vehicleExhaust":1.01,"pesticide":1.36,"gluesPlastic":1.22}
comorbid = {"asthma":1.11,"copd":6.38,"hayFever":0.68}
famHist = {"lungCancFDR":1.11,"smokingRelatedCancFDR":1.02}
