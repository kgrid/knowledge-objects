# Lung Cancer Risk Models

### Knowledge Objects
  A total of 8 lung cancer models have been developed as knowledge objects. Within each subdirectory, you can find a (1) python payload, (2) input RDF, (3) output RDF,(4) README.md and (5) the corresponding research paper. The README.md contains more in depth information about each particularly knowledge object, but an overview is shown below. All of these knowledge objects are located on the dev library, and have been deployed to the KGrid sandbox activator (baseUrl: "http://kgrid.med.umich.edu/stack"). 
 
    1. Bach Model (Bach, et al, 2003)
          - Objective: calculate an individuals total lung caner risk within the next 10 years
          - Input: age, cpd, yrsSmok (years smoked), yrsQuit (years quit), asbestos (exposure y/n), sex, quit (quit smoking y/n)(i.e. {"age":55, "cpd":20, "yrsSmok":30, "yrsQuit":0, "asbestos":0, "sex":1, "quit":1})
          - Output: Risk percentage and interpretation (i.e. {'interpretation': 'This individual has a total lung cancer risk of 0.78% in the next 10 years.', 'result': 0.78})
          - ArkID: ark:/99999/fk4057tv7z
    2. Cassidy Model (Cassidy, et al, 2008)
          - Objective: estimates the lung cancer 5-year risk for an individual, by taking the age midpoint 
          - Input: sex, age, riskFactors (i.e. {"sex":"male","age":51,"riskFactors":["smoking duration, 21-40 years"]})
                - possible riskFactors include:
                          - "pneumonia"
                          - "asbestos"
                          - "prior cancer"
                          - "famHxCanc, early onset"
                          - "famHxCanc, late onset"
                          - "smoking duration, 1-20 years"
                          - "smoking duration, 21-40 years"
                          - "smoking duration, 41-60 years"
                          - "smoking duration, >= 60 years"
          - Output: Risk percentage and interpretation (i.e. {'interpretation': 'This individual has a 3.17% probability of developing lung cancer in the next 5 years.', 'result': 3.17})
          - ArkID: ark:/99999/fk4571pp25
    3. Etzel Model (Etzel, et al, 2008)
          - Objective: Calculate the absolute risk of an individual developing lung cancer within 5 years.
          - Input: smokerStatus, sex, riskFactors(i.e. {"smokerStatus":"current","age":13,"sex":"male","riskFactors":["duration>30y","numCigsDay>20","asbestos","dust","dryCleaning","pack-years>40","copd"]})
                - age is represented as a range, see README.md (i.e age = 13, >= 85 years old)
                - possible riskFactors include:
                          - "duration>30y"
                          - "numCigsDay>20"
                          - "pack-years>40"
                          - "yrsCessation" (years since cessation)
                          - "ageCessation>30y" (age at cessation >30 yrs)
                          - "mentholCigUse" (methanol cigarette us)
                          - "asbestos"
                          - "dust"
                          - "fiber"
                          - "svf"
                          - "benzene"
                          - "toluene/xylene"
                          - "dryCleaning"
                          - "vehicleExhaust"
                          - "pesticide"
                          - "gluesPlastic"
                          - "asthma"
                          - "copd"
                          - "hayFever"
                          - "lungCancFDR" (lung cancer in >= 1 first degree relative)
                          - "smokingRelatedCancFDR" (smoking related cancer in >=1 first degree relative)
          - Output: Risk percentage and interpretation (i.e. {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next 5 years and not dying is 90.47%.', 'result': 90.47})
          - ArkID: ark:/99999/fk4bg2zf1n
    4. Hoggart Model (Hoggart, et al, 2012)
          - Objective: Calculates the individuals probability of being diagnosed with lung cancer in 1 year from age t.
          - Input: smokerStatus, smokDurat, t (age with respect to time zero, 35 years old), riskFactors (i.e. {"smokerStatus":"former","smokDurat":10,"t":24,"riskFactors":{"sex":"female","bmi":28,"hayFever": 1}})
                 - possible riskFactors include:
                  	  - "sex"
                          - "bmi"
                          - "edLevel" (measured by level completed)
                          - "hayFever"
	                  - "asthma"
                          - "famHxCanc"
                          - "chr15q25" (presence of SNP)
                          - "chr5p15" (presence of SNP)
                          - "silica"
                          - "pah"
                          - "metal"
                          - "asbestos"
          - Output: Risk percentage and interpretation (i.e. {'interpretation': 'This individual has a 13.93% probability of being diagnosed with lung cancer in 1 year from age t.', 'result': 13.93})
          - ArkID: ark:/99999/fk45430b5m
    5. Marcus Model (Marcus, et al., 2015)
          - Objective: Estimates the lung cancer incidence
          - Input: age, sex, smokDurat, copd, priorDiag, earlyOnset, lateOnset (i.e. {"age":50,"sex":1,"smokDurat":30,"copd":1,"priorDiag":0,"earlyOnset":0,"lateOnset":0})
          - Output: Risk percentage and interpretation (i.e. {'interpretation': 'This individual has a 6.03% probability of developing lung cancer.', 'result': 6.03})
          - ArkID: ark:/99999/fk4x92gk0r
    6. Park Model (Park, et al, 2013)
          - Objective: Predicts an individuals lung cancer risk within 8 years, specifically for Korean men
          - Input: age, smokerStatus, asi, bmi, physActiv, fastingGluc (i.e. {"age":0,"smokerStatus":0,"asi":0,"bmi":0,"physActiv":0,"fastingGluc":0})
          - Output: Risk percentage and interpretation (i.e. {'interpretation': 'This individual has a 0.63% probability of developing lung cancer within 8 years.', 'result': 0.63})
          - ArkID: ark:/99999/fk4r49xd2g
    7. Spitz Model (Spitz, et al, 2007)
   	- Objective: Predicts the probability of being diagnosed with lung cancer in the next year and still being alive
	- Input: sex, age, smokerStatus, ets, emphysema, hayFever, dust, fumes, chemicals, asbestos, pesticides, woodDust, asthma, famHxCanc, famHxSmokeCanc, asi, ageQuit, asc, yrsCess, packYrs (i.e {"sex":"male","age":8,"smokerStatus":"former","ets":0,"emphysema":0,"hayFever":0,"dust":1,"fumes":1,"chemicals":1,"asbestos":0,"pesticides":1,"woodDust":0,"asthma":0,"famHxCanc":0,"famHxSmokeCanc":0,"asi":25,"ageQuit":30,"asc":0,"yrsCess":1,"packYrs":0})
	- Output: Risk percentage and interpretation (i.e. {'interpretation': 'The probability of this individual being diagnosed with lung cancer in the next year and not dying is 30.26%.', 'result': 30.26})
	- ArkID: ark:/99999/fk4k64rx3z
    8. Tammemamgi Model (Tammemamgi, et al,2013) 
    	- Objective: Calculates the 6-year lung cancer risk for a given individual
        - Input: age, edLevel, bmi, copd, hxLungCancer, famHxCanc, race, cigsPerDay, smokDurat, yrsQuit(i.e. {"age":70,"edLevel":0,"bmi":0,"copd":0,"hxLungCancer":1,"famHxCanc":1,"race":0,"cigsPerDay":0,"smokDurat":0,"yrsQuit":0})
        - Output: Risk percentage and interpretation (i.e. {'interpretation': "This individual's six year probability of developing lung cancer is 8.68%.", 'result': 8.68})
        - ArkID: ark:/99999/fk4jh3tk9s

### Other
To aid in testing and execution, a postman collection (lcrm.json) has been included. This collection includes basic PUT, GET, and POST commands for each lung cancer model.
