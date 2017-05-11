# Spitz, A Risk Model for Prediction of Lung Cancer (Spitz et al, 2007)
Author: Kristen McGarry
Created: May 3, 2017
Consultant: Phil Boonstra

### Objective
The Spitz model predicts the probability of being diagnosed with lung cancer in the next year and not dying before that point.

### Description
The input is as follows:
- sex
    - female
    - male
- age
    - 0: 40-44 yrs
    - 1: 45-49 yrs
    - 2: 50-54 yrs
    - 3: 55-59 yrs
    - 4: 60-64 yrs
    - 5: 65-69 yrs
    - 6: 70-74 yrs
    - 7: 75-79 yrs
    - 8: 80-84 yrs
    - 9: >=85 yrs
- smokerStatus
    - never
    - former
    - current
- ets (environmental tobacco smoke)
    - 0: no exposure
    - 1: exposure
- emphysema
    - 0: no exposure
    - 1: exposure
- hayFever
    - 0: no exposure
    - 1: exposure
- dust
    - 0: no exposure
    - 1: exposure
- fumes
    - 0: no exposure
    - 1: exposure
- chemicals
    - 0: no exposure
    - 1: exposure
- asbestos
    - 0: no exposure
    - 1: exposure
- pesticides
    - 0: no exposure
    - 1: exposure
- woodDust
    - 0: no exposure
    - 1: exposure
- asthma
    - 0: no exposure
    - 1: exposure
- famHxCanc (family history of cancer)
    - 0: no family history
    - 1: 1 first-degree relative with cancer
    - 2: >=2 first-degree relatives with cancer
- famHxSmokeCanc (family history of smoking-related cancers (i.e. lung, upper aerodigestive tract, esophagus, pancreas, bladder and cervix))
    - 0: no family history
    - 1: 1 first-degree relative with smoking-related cancer
- asi (age at smoking initiation)
    - continuous
- ageQuit (age stopped smoking)
    - 0: <= 38 yrs
    - 1: >39 yrs
- asc (age at smoking cessation)
    - continuous
- yrsCess (years of cessation)
    - continuous
- packYrs (pack-years smoked)
    - continuous

### Running
The script can be run by calling execute(inputs). We have also included a test() function that we suggest running before running your data through.

### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
    1. python
    2. import spitz
    3. spitz.execute({"sex":"male","age":8,"smokerStatus":"former","ets":0,"emphysema":0,"hayFever":0,"dust":1,"fumes":1,"chemicals":1,"asbestos":0,"pesticides":1,"woodDust":0,"asthma":0,"famHxCanc":0,"famHxSmokeCanc":0,"asi":25,"ageQuit":30,"asc":0,"yrsCess":1,"packYrs":0})

### Running through SHELF REST API...  
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4k64rx3z**

    1. To add to shelf: PUT {{baseUrl}}/shelf/ark:/99999/fk4k64rx3z
    2. To check shelf: GET {{baseUrl}}/shelf
    3. To execute:
       - Add the following headers:
         - Content-Type:application/json
         - Accept:application/json
       - Enter input into "body" (i.e. {"sex":"male","age":8,"smokerStatus":"former","ets":0,"emphysema":0,"hayFever":0,"dust":1,"fumes":1,"chemicals":1,"asbestos":0,"pesticides":1,"woodDust":0,"asthma":0,"famHxCanc":0,"famHxSmokeCanc":0,"asi":25,"ageQuit":30,"asc":0,"yrsCess":1,"packYrs":0})
       - Run the POST command. {{baseUrl}}/knowledgeObject/ark:/99999/fk4k64rx3z/result

### Literature
The documentation can be found at: https://www.ncbi.nlm.nih.gov/pubmed/17470739
