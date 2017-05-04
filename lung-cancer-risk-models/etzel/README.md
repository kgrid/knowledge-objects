# Etzel, Development and Validation of a Lung Cancer Risk Prediction Model for African-Americans (Etzel et al, 2008)
Author: Kristen McGarry
Created: April 21, 2017

### Objective
This object predicts the absolute risk of an individual developing lung cancer within 5 years.

### Description
The inputs is as follows (i.e. {"smokerStatus":"former","sex":"female","riskFactors":[]}):
      - smokerStatus
          - current
          - former
      - sex
          - female
          - male
      - age
          - 0: 20-24 yrs
          - 1: 25-29 yrs
          - 2: 30-34 yrs
          - 3: 35-39 yrs
          - 4: 40-44 yrs
          - 5: 45-49 yrs
          - 6: 50-54 yrs
          - 7: 55-59 yrs
          - 8: 60-64 yrs
          - 9: 65-69 yrs
          - 10: 70-74 yrs
          - 11: 75-79 yrs
          - 12: 80-84 yrs
          - 13: >= 85 yrs
      - riskFactors:
          - duration>30y
          - numCigsDay>20
          - pack-years>40
          - yrsCessation (years since cessation)
          - ageCessation>30y (age at cessation >30 yrs)
          - mentholCigUse (methanol cigarette us)
          - asbestos
          - dust
          - fiber
          - svf
          - benzene
          - toluene/xylene
          - dryCleaning
          - vehicleExhaust
          - pesticide
          - gluesPlastic
          - asthma
          - copd
          - hayFever
          - lungCancFDR (lung cancer in >= 1 first degree relative)
          - smokingRelatedCancFDR (smoking related cancer in >=1 first degree relative)


### Running
The script can be run by calling execute({"smokerStatus":"former","sex":"female","riskFactors":[]}). We have also included a test() function that we suggest running before running your data through.

### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
          1. python
          2. import etzel
          3. etzel.execute({"smokerStatus":"former","sex":"female","riskFactors":[]})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4bg2zf1n**

          1. To add to shelf: PUT {{baseUrl}}/shelf/ark:/99999/fk4bg2zf1n
          2. To check shelf: GET {{baseUrl}}/shelf
          3. To execute:
             - Add the following headers:
               - Content-Type:application/json
               - Accept:application/json
             - Enter input into "body" (i.e. {"smokerStatus":"current","age":13,"sex":"male","riskFactors":["duration>30y","numCigsDay>20","asbestos","dust","dryCleaning","pack-years>40","copd"]})
             - Run the POST command. {{baseUrl}}/knowledgeObject/ark:/99999/fk4bg2zf1n/result

### Literature
The documentation can be found at: https://www.ncbi.nlm.nih.gov/pubmed/19138969
