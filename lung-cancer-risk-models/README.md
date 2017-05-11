# Lung Cancer Risk Models

### Knowledge Objects
  A total of 8 knowledge objects have been developed. Within each subdirectory, you can find a (1) python payload, (2) input RDF, (3) output RDF,(4) README.md and (5) the corresponding research paper. The README.md contains more in depth information about each particularly knowledge object. All of these knowledge objects are located on the dev library, and have been deployed to the KGrid sandbox activator (baseUrl: "http://kgrid.med.umich.edu/stack"). 
 
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
          - Objective: 
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
          - Objective: 
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
          - ArkID:
    5. Marcus Model
          - Objective:
          - Input:
          - Output:
          - ArkID:
    6. Park Model
          - Objective:
          - Input:
          - Output:
          - ArkID:
    7. Spitz Model
          - Objective:
          - Input:
          - Output:
          - ArkID:
    8. Tammemamgi Model
          - Objective:
          - Input:
          - Output:
          - ArkID:

### Other
To aid in testing and execution, a postman collection (lcrm.json) has been included. This collection includes basic PUT, GET, and POST commands for each lung cancer model.
