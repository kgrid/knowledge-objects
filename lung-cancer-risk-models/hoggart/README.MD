# Hoggart, A Risk Model for Lung Cancer Incidence (Hoggart, et.al., 2012)
Author: Kristen McGarry
Organization: KGrid, University of Michigan, Michigan Medicine
April 20th, 2017

### Objective
This knowledge object takes in an individuals smoker status, smoking duration, age and covariates to calculate the individuals probability of being diagnosed with lung cancer in 1 year from age t.


### Description
Smoker status is either "current" or "former", smoking duration is years smoked, and t represents age with time zero being set to 35 years old (i.e. If someone is 62 years old, t will equal 27).

The following variables are the covariates with each respective value:
	1)	sex
  	-	female 1
  	-	male 0
	2)	BMI
	 -	actual value
	3)	education Level (measured by level completed)
  	-	other 1
  	-	university degree 0
	4)	hay fever
	  - yes 1
	  -	no 0
	5)	asthma
	  - yes 1
	  - no 0
	6)	family history of cancer
  	-	yes 1
  	-	no 0
	7)	chr15q25 (presence of SNP)
  	-	yes 1
  	-	no 1
	8)	chr5p15 (presence of SNP)
  	-	yes 1
  	-	no 1
	9)	silica
  	-	yes 1
  	-	no 0
  10)	pah
  	-	yes 1
  	-	no 0
	11)	metal
  	-	yes 1
  	-	no 0
	12)	asbestos
  	-	yes 1
  	-	no 0

### Running
The script can be run by calling execute({"smokerStatus":"","smokingDuration":0,"t":0,"covariates":{}}. We have also included a test() function that we suggest running before running your data through.

To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import hoggart
3. hoggart.execute({"smokerStatus":"former","smokingDuration":10,"t":24,"covariates":{"sex":"female","BMI":28,"hay fever": 1}})

### Running through SHELF REST API...
The ark ID for this object is: **ark:/99999/fk45430b5m**

1. To add to shelf: {{baseUrl}}/shelf/ark:/99999/fk45430b5m
2. To check shelf: {{baseUrl}}/shelf
3. To execute:
  - Add the following headers:
    - Content-Type:application/json
    - Accept:application/json
  - Enter input into "body" (i.e. {"smokerStatus":"former","smokingDuration":10,"t":24,"covariates":{"sex":"female","BMI":28,"hay fever": 1}})
  - Run the POST command. {{baseUrl}}/knowledgeObject/ark:/99999/fk45430b5m/result


### Literature
This documentation can be found at: https://www.ncbi.nlm.nih.gov/pubmed/22496387
