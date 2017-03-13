# Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus
## Step 1. Elevated BP uncontrolled by prior lifestyle modifications
Created: January 16, 2016

UMMG Clinical Value and Innovations

Clinical Alignment & Performance Excellence

University of Michigan

### Objective
This knowledge object takes in blood pressure readings and albumin level test results and outputs a therapy recommendation for those with high BP uncontrolled by prior lifestyle modifications.

The knowledge is derived from Table 11: Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus. See Literature section for more information.

### Description
The inputs are systolic, diastolic, and albuminLevel, all type float. The inputs must be formatted as follows, with systolic, diastolic and albuminLevel representing keys that should not be changed:

execute({"systolic":0.0,
                      "diastolic":0.0,
                      "albuminLevel":0.0})


The output is the recommended therapy, or an "unable to calculate" message if values are missing, the patient doesn't have high BP, or the diagnosis is macroalbuminuria. Outputs include:
- No systolic or diastolic information provided. Cannot calculate.
- Not applicable, patient doesn't have high blood pressure.
- No albumin level information provided. Cannot calculate.
- Albumin levels indicate macroalbuminuria.
- With microalbiminuria-
(1) ACE Inhibitor- initiate therapy unless contraindication (hypersensitivity reaction, angioedema) or documented persistent cough.
(a) Lisinopril 10mg daily. Titrate by doubling dose every 2-4 weeks until the BP goal is met (max dose: 40mg)
(2) If ACE inhibitor contraindicated: Angiotensin II Receptor BLOCKER (ARB)
(a) Losartan 25-50mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT met (max dose: 100mg)
- Without microalbuminuria-
initiate therapy with either:
(1) Thiazide diuretic - initiate therapy.
(a) Chlorthalidone 25mg/day. Titrate by doubling dose in 2-4 weeks if BP goal NOT met. (max dose: 50mg daily)
(b) Hydrochlorothiazide 12.5mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT met. (max dose: 25mg daily).
(2) ACE inhibitor (Angiotensin-Converting Enzyme) Inhibitor- initiate therapy unless contraindication (hypersensitivity reaction, angioedema) or documented persistent cought.
(a) Lisinopril 10mg daily. Titrate by doubling dose every 2-4 weeks until the BP goal is met (max dose: 40mg).
(3) If ACE inhibitory contraindicated: Angiotensin II Receptor Blocker (ARB).
(a) Losartan 24-50mg daily. Titrate by doubling dose in 2-4 weeks if BP goal NOT med (max dose: 100mg)

### Getting started
  To run program from terminal, go to terminal and cd into the directory where the python file is located. Enter the following:
  1. python2
  2. import step-1
  3. step-1.execute({"systolic":0.0,"diastolic":0.0,"albuminLevel":0.0})

### Running through SHELF REST API...
To run through SHELF REST API, the knowledge object needs to be added to ObjectTeller and to the REST API SHELF before its executable.
The ark ID for this object is: **ark:/99999/fk49c76k8x**

1. To add to shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf/ark:/99999/fk49c76k8x
2. To check shelf: http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/shelf
3. To execute:
  - Add the following headers:
    - Content-Type:application/json
    - Accept:application/json
  - Enter input into "body" (i.e. {"systolic":10,"diastolic":0,"albuminLevel":230})
  - Run the POST command. http://dlhs-fedora-dev-a.umms.med.umich.edu:8080/ExecutionStack/knowledgeObject/ark:/99999/fk49c76k8x/result

### Related Objects/Future Development
This knowledge represents the first step in a series of four steps focused on pharmacologic treatment of hypertension in patients with diabetes mellitus. This KO was created with other diabetes KO in hopes to create a collection of KO helpful for the diabetes mellitus community.

- **Step 1: ark:/99999/fk49c76k8x**
- Step 2: ark:/99999/fk4w66qt8k
- Step 3: ark:/99999/fk4rf6114q
- Step 4: ark:/99999/fk4mp5968n

### Literature
The documentation can be found at: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf
