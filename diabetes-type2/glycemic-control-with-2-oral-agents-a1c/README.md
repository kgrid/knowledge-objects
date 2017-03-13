# Steps in Glycemic Control with 2 Oral Agents in Patients with Type 2 Diabetes, Based on A1c
Created: January 9th, 2017

UMMG Clinical Value and Innovations

Clinical Alignment & Performance Excellence

University of Michigan

### Objective
This knowledge object takes in an A1c percentage and individualized target (if applicable) and outputs the corresponding glycemic control recommendation.

This KO is derived from Table 6: Steps in Glycemic Control with Oral Agents in Patients with Type 2 Diabetes, Step 3. See Literature section for more information.


### Description
The inputs for this KO are a1c (type float) and individual_target (type float) and must be formatted as follows, with a1c representing a key that should not be changed:

execute({"a1c":0.0, "individual_target":0.0})

If no a1c is provided, the function will output "no a1c provided. unable to calculate". If individual_target is left at 0, the script will assume that there is on defined individualized target, and will calculate based on the averaged values.

### Running
The script can be run by calling execute({"a1c":0.0,"individual_target":0.0}). We have also included a test() function that we suggest running before running your data through.


### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import gc
3. gc.execute({"a1c":0.0,"individual_target":0.0})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk41g0zd0q**

1. To add to shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf/ark:/99999/fk41g0zd0q
2. To check shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf
3. To execute:
  - Add the following headers:
    - Content-Type:application/json
    - Accept:application/json
  - Enter input into "body" (i.e. {"a1c":7.0,"individualTarget":0.0})
  - Run the POST command. http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/knowledgeObject/ark:/99999/fk41g0zd0q/result


### Related Objects/Future Development
This KO was created with other diabetes KO in hopes to create a collection of KO helpful for the diabetes community.

### Literature
The documentation can be found at: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf
