# Risk Module of Type II Diabetes
Created: December 20, 2016

UMMG Clinical Value and Innovations

Clinical Alignment & Performance Excellence

University of Michigan

### Objective
This knowledge object takes in the diagnostic test and the glucose level, and returns the type 2 diabetes diagnosis (normal, pre-diabetes, diabetes).

This KO is derived from Table 1: Diagnosis of Diabetes: Diagnostic tests and Glucose Levels. See Literature section for more information.


### Description
The inputs for this KO are diagnosticTest and glucoseLevel and must be formatted as follows, with diagnosticTest and glucoseLevel representing keys that should not be changed:

execute(
  {"diagnosticTest":"",
  "glucoseLevel":0)


glucoseLevel can be any float. diagnosticTest can be one of the following. These strings are also keys and should not be changed:

- hemoglobin A1c
- fasting plasma glucose (mg/dL)
- random plasma glucose (mg/dL)
- oral glucose tolerance test (OGTT)(mg/dL)

The KO outputs the type 2 diabetes diagnosis:
- normal
- pre-diabetes
- diabetes

If the diagnosticTest does not match one of the keys, the following string will be returned:

"Incorrect diagnostic test. Diagnostic test can be:
* hemoglobin A1c
* fasting plasma glucose (mg/dL)
* random plasma glucose (mg/dL)
* oral glucose tolerance test (OGTT)(mg/dL)"

If the glucoseLevel was not entered (glucoseLevel = 0), the following string will be returned:

"glucoseLevel = 0, No glucose level provided"

### Running
The script can be run by calling execute("diagnosticTest":"","glucoseLevel":0). We have also included a test() function that we suggest running before running your data through.


### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import dd
3. dd.execute({"diagnosticTest":"","glucoseLevel":0))

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4w09b99w**

1. To add to shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf/ark:/99999/fk4w09b99w
2. To check shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf
3. To execute:
  - Add the following headers:
    - Content-Type:application/json
    - Accept:application/json
  - Enter input into "body" (i.e. {"diagnosticTest":"hemoglobin A1c","glucoseLevel":6})
  - Run the POST command. http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/knowledgeObject/ark:/99999/fk4w09b99w/result

### Related Objects/Future Development
This KO was created with other diabetes KO in hopes to create a collection of KO helpful for the diabetes community.

### Literature
The documentation can be found at: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf
