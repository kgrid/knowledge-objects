# Liverpool Lung Project Risk Prediction Model for Lung Cancer Incidence
Created: April 7, 2017


### Objective
This knowledge object (KO) estimates the lung cancer incidence through the Liverpool predictive model



### Description
The input is as follows: {"age":0,"gender":0,"smoking_duration":0,"copd":0,"prior_diag":0,"early_onset":0,"late_onset":0}  
- gender: 0-female, 1-male  
- smoking_duration: # of years smoking_duration  
- copd: 0-no, 1-yes  
- prior_diag: Prior diagnosis for malignant tumour, 0-no, 1-yes  
- early_onset: early onset (<60 years), 0-no, 1-yes  
- late_onset: late onset (>= 60 years), 0-no, 1-yes  


### Running
The script can be run by calling execute({"age":0,"gender":0,"smoking_duration":0,"copd":0,"prior_diag":0,"early_onset":0,"late_onset":0}). We have also included a test() function that we suggest running before running your data through.


### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import liverpool
3. liverpool.execute({"age":0,"gender":0,"smoking_duration":0,"copd":0,"prior_diag":0,"early_onset":0,"late_onset":0})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4x92gk0r**

1. To add to shelf: {{baseUrl}}/shelf/ark:/99999/fk4x92gk0r
2. To check shelf: {{baseUrl}}/shelf
3. To execute:
   - Add the following headers:
     - Content-Type:application/json
     - Accept:application/json
   - Enter input into "body" (i.e. {"age":50,"gender":1,"smoking_duration":30,"copd":1,"prior_diag":0,"early_onset":0,"late_onset":0})
   - Run the POST command. {{baseUrl}}/knowledgeObject/ark:/99999/fk4x92gk0r/result

### Literature
The documentation can be found at: https://www.ncbi.nlm.nih.gov/pubmed/25873368
