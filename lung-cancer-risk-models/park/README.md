# Park, Individualized Risk Prediction Model for Lung Cancer in Korean Men (Park et al, 2013)
Created: May 2, 2017


### Objective
This knowledge object (KO) predicts an individuals lung cancer risk within 8 years. This predictor is targeted for Korean men. The calculation is from Appendix S1 in Park et al, 2013. The Park model fits a survival model by predicting the absolute probability of diagnosis at a certain time point and not dying before that time point. This specific object will predict the baseline survival time of 8 years.

### Description
The input is as follows: {"age":0,"smokerStatus":0,"asi":0,"bmi":0,"physActiv":0,"fastingGluc":0})
- age
- smokerStatus
    - 0 = never smoker
    - 1 = past smoker
    - 2 = current smoker, <0.5 pack/day
    - 3 = current smoker, 0.5-0.99 pack/day
    - 4 = current smoker, >=1 pack/day
- asi (age at smoking initiation)
    - 0 age >= 40 at smoking initiation
    - 1 30<= age <40 at smoking initiation
    - 2 19<= age <30 at smoking initiation
    - 3 16<= age <19 at smoking initiation
    - 4 age <16 at smoking initiation
- bmi
    - 0 BMI 18.5–22.9
    - 1 BMI < 18.5
    - 2 BMI 23.0–24.9
    - 3 BMI ≥ 25.0
- physActiv (physical activity)
    - 0 none
    - 1 light
    - 2 moderate
    - 3 heavy
- fastingGluc (fasting glucose)
    - 0 glucose < 126
    - 1 glucose >= 126


### Running
The script can be run by calling execute({"age":50,"smokerStatus":3,"asi":1,"bmi":2,"physActiv":1,"fastingGluc":1}). We have also included a test() function that we suggest running before running your data through.


### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import park
3. park.execute({"age":50,"smokerStatus":3,"asi":1,"bmi":2,"physActiv":1,"fastingGluc":1})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4r49xd2g**

1. To add to shelf: {{baseUrl}}/shelf/ark:/99999/fk4r49xd2g
2. To check shelf: {{baseUrl}}/shelf
3. To execute:
   - Add the following headers:
     - Content-Type:application/json
     - Accept:application/json
   - Enter input into "body" (i.e. {"age":50,"smokerStatus":3,"asi":1,"bmi":2,"physActiv":1,"fastingGluc":1})
   - Run the POST command. {{baseUrl}}/knowledgeObject/ark:/99999/fk4r49xd2g/result

### Literature
The documentation can be found at: http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0054823
