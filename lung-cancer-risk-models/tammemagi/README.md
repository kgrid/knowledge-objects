# Tammemagi, Selection Criteria for Lung-Cancer Screening (Tammemagi, et.al.,2013)
Created: November 16, 2016
Authors: Wei Shi, Rocky Fischer, Tanner Caverly
Last Updated: April 26th, 2017 by Kristen McGarry


### Objective
This knowledge object (KO) estimates the 6-year lung cancer risk for a given person.

### Description
The input is as  follows: {"age":0,"edLevel":0,"bmi":0,"copd":0,"hxLungCancer":0,"famHxCanc":0,"race":0,"cigsPerDay":0,"smokDurat":0,"yrsQuit":0})

### Running
The script can be run by calling execute({"age":0,"sex":0,"smokDurat":0,"copd":0,"priorDiag":0,"earlyOnset":0,"lateOnset":0}). We have also included a test() function that we suggest running before running your data through.


### Getting started
To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
1. python
2. import tammemagi
3. tammemagi.execute({"age":70,"edLevel":1,"bmi":0,"copd":0,"hxLungCancer":1,"famHxCanc":1,"race":1,"cigsPerDay":0,"smokDurat":0,"yrsQuit":0})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4jh3tk9s**

1. To add to shelf: {{baseUrl}}/shelf/ark:/99999/fk4jh3tk9s
2. To check shelf: {{baseUrl}}/shelf
3. To execute:
   - Add the following headers:
     - Content-Type:application/json
     - Accept:application/json
   - Enter input into "body" (i.e. {"age":70,"edLevel":1,"bmi":0,"copd":0,"hxLungCancer":1,"famHxCanc":1,"race":1,"cigsPerDay":0,"smokDurat":0,"yrsQuit":0})
   - Run the POST command. {{baseUrl}}/knowledgeObject/ark:/99999/fk4x92gk0r/result

### Literature
The documentation can be found at: http://www.nejm.org/doi/full/10.1056/NEJMoa1211776#t=article
