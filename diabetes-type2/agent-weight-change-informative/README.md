# Agent Weight Change Informative
Created: January 27th, 2017

UMMG Clinical Value and Innovations

Clinical Alignment & Performance Excellence

University of Michigan

### Objective
This knowledge object (KO) takes in an agent, and outputs the corresponding weight change information.

This KO is derived from Table 7: Comparisons of Agents for Glycemic Control in Patients with Type 2 Diabetes. See Literature section for more information.


### Description
The input is agent (type string) a must be formatted as follows, with agent representing a key that should not be changed:

execute({"agent":""})

If no agent is provided or the agent input doesn't match an existing agent, the function will output "cannot calculate".

### Running
The script can be run by calling execute({"agent":""}). We have also included a test() function that we suggest running before running your data through.


### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import awci
3. awci.execute({"agent":""})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4d50wh15**

1. To add to shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf/ark:/99999/fk4d50wh15
2. To check shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf
3. To execute:
  - Add the following headers:
    - Content-Type:application/json
    - Accept:application/json
  - Enter input into "body" (i.e. {"agent":"Glucophage XR"})
  - Run the POST command. http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/knowledgeObject/ark:/99999/fk4d50wh15/result

### Related Objects/Future Development
This KO was created with other diabetes KO in hopes to create a collection of KO helpful for the diabetes community.

### Literature
The documentation can be found at: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf
