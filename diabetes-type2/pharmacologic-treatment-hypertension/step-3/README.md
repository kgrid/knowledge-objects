# Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus
## Step 3. If above agents are contraindicated or dose is optimized and patients BP remains >= 140/90

Created: January 16, 2016

UMMG Clinical Value and Innovations

Clinical Alignment & Performance Excellence

University of Michigan

### Objective
This knowledge object takes in blood pressure readings and outputs a therapy recommendation for those with high BP, with an optimized dose of the agent from Step 2.

The knowledge is derived from Table 11: Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus. See Literature section for more information.

### Description
The inputs are systolic and diastolic, type float. The inputs must be formatted as follows, with systolic and diastolic representing keys that should not be changed:

therapyRecommendation3({"systolic":0.0,
                      "diastolic":0.0})


The output is the recommended therapy, or an "unable to calculate" message if values are missing, the patient doesn't have high BP.
 Outputs include:
- No systolic or diastolic information provided. Cannot calculate.
- Not applicable, patient doesn't have high blood pressure.
- If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90-
  Add a Dihydropyridine Calcium Channel Blocker - initiate therapy
  Amlodipine (Norvasc) 2.5-2mg daily. Titrate by doubling dose in 2-4 weeks if BP goal is NOT met (max dose: 10mg)


### Getting started
  To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
  1. python2
  2. import step-3
  3. step-1.therapyRecommendation3({"systolic":0.0,"diastolic":0.0})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk4rf6114q**

1. To add to shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf/ark:/99999/fk4rf6114q
2. To check shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf
3. To execute:
  - Add the following headers:
    - Content-Type:application/json
    - Accept:application/json
  - Enter input into "body"
  - Run the POST command. http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/knowledgeObject/ark:/99999/fk4rf6114q/result

### Related Objects/Future Development
This knowledge represents the third step in a series of four steps focused on pharmacologic treatment of hypertension in patients with diabetes mellitus. This KO was created with other diabetes KO in hopes to create a collection of KO helpful for the diabetes mellitus community.

- Step 1: ark:/99999/fk49c76k8x
- Step 2: ark:/99999/fk4w66qt8k
- **Step 3: ark:/99999/fk4rf6114q**
- Step 4: ark:/99999/fk4mp5968n

### Literature
The documentation can be found at: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf
