# Meal Planning for Glycemic Management Based on Medication
Created: January 6th, 2017

UMMG Clinical Value and Innovations

Clinical Alignment & Performance Excellence

University of Michigan

### Objective
This knowledge object takes in a medication and weight loss intention, and returns the recommended meal plan.

This KO is derived from Table 4: Meal Planning for Glycemic Management Based on Medication. See Literature section for more information.


### Description
The inputs for this KO are medication and weightloss and must be formatted as follows, with medication and weightloss representing keys that should not be changed:

execute(
    {"medication":"",
    "weightloss":0})

weightloss is a binary yes/no response, with yes = 1, and no = 0. medication can be one of the following. These strings are also keys and should not be changed:

- "no medication or oral medication"
- "secretagogues"
- "fixed daily insulin"
- "premixed insulin"
- "intensive flexible insulin program (basal/bolus)"

If medication doesn't match one of these options, the function will return "No matching medication option."

### Running
The script can be run by calling execute({"medication":"","weightloss":0}). We have also included a test() function that we suggest running before running your data through.


### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import gmmp
3. gmmp.execute({"medication":"","weightloss":0}).

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4vm4hg3v**

1. To add to shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf/ark:/99999/fk4vm4hg3v
2. To check shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf
3. To execute:
  - Add the following headers:
    - Content-Type:application/json
    - Accept:application/json
  - Enter input into "body" (i.e. {"medication":"secretagogues","weightloss":0})
  - Run the POST command. http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/knowledgeObject/ark:/99999/fk4vm4hg3v/result

### Related Objects/Future Development
This KO was created with other diabetes KO in hopes to create a collection of KO helpful for the diabetes community.

### Literature
The documentation can be found at: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf
