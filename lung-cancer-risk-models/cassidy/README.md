# LLP risk model: an individual 5-year risk prediction model for lung cancer (Cassidy, et.al., 2008)
Created: April 11, 2017


### Objective
This knowledge object (KO) estimates the lung cancer 5-year risk for an individual, given the age, sex, and risk factors. This models takes the midpoint of the age when calculating risk, making this calculator different than others.



### Description
The input is as follows: {"sex":"","age":0,"riskFactors":[]}
    riskFactors can include:
        - "pneumonia"
        - "asbestos"
        - "prior cancer"
        - "famHxCanc, early onset"
        - "famHxCanc, late onset"
        - "smoking duration, 1-20 years"
        - "smoking duration, 21-40 years"
        - "smoking duration, 41-60 years"
        - "smoking duration, >= 60 years"
    sex is automatically lower cased before beginning computation so can include any variation of male or female.
    Age must be type integer, but 0.5 will be added to the age before beginning computation for a more accurate risk.


### Running
The script can be run by calling execute({"sex":"","age":0,"riskFactors":[]}). We have also included a test() function that we suggest running before running your data through.


### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import cassidy
3. cassidy.execute({"sex":"","age":0,"riskFactors":[]})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4571pp25**

1. To add to shelf: PUT {{baseUrl}}/shelf/ark:/99999/fk4571pp25
2. To check shelf: GET {{baseUrl}}/shelf
3. To execute:
   - Add the following headers:
     - Content-Type:application/json
     - Accept:application/json
   - Enter input into "body" (i.e. {"sex":"male","age":51,"riskFactors":["smoking duration, 21-40 years"]})
   - Run the POST command. {{baseUrl}}/knowledgeObject/ark:/99999/fk4571pp25/result

### Literature
The documentation can be found at: https://www.ncbi.nlm.nih.gov/pubmed/18087271
