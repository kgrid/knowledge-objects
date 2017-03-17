# Diabetes Mellitus Type II Knowledge Objects
Based off the following practice guidelines: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf

Within each knowledge object repository, we have included the python code, an input RDF, an output RDF, a README, and the clinical documentation where the knowledge was extracted from. The README contains important metadata, along with information on how to execute the object locally and how to execute the object using REST API.

We have created a collection of these knowledge objects that can be found in the following file: dm.json. This collection contains a list of commands for these knowledge objects, including a PUT(ADD/UPDATE) command and a POST command for each one. The collection can be directly imported to a REST API client; we use postman.


The completed knowledge objects are as follows (also on ObjectTeller):

   1. Type II Diabetes Diagnosis
      - Input: diagnosticTest, glucoseLevel (i.e. {"diagnosticTest":"hemoglobin A1c","glucoseLevel":6})
      - Output: diabetic diagnosis (i.e. "pre-diabetes")
      - ArkID: ark:/99999/fk4gm8g63d
 
   2. Meal Planning For Glycemic Management based on Medication
      - Input: medication, weightloss (i.e. {"medication":"secretagogues","weightloss":0})
      - Output: meal planning recommendation (i.e. "carbohydrate at each meal")
      - ArkID: ark:/99999/fk4vm4hg3v

   3. Steps in Glycemic Control with oral agents: 1 Agent 
      - Input: a1c, individualTarget (i.e. {"a1c":8.2,"individualTarget":0})
      - Output: glycemic control recomendation (i.e. "add a second agent or insulin customized to patient. re-measure A1c in 6-12 weeks after initiation or dose change of medication")
      - ArkID: ark:/99999/fk4fn1fb10

   4. Steps in Glycemic Control with 2 oral agents in Patients with Type 2 Diabetes Based on A1c
      - Input: a1c, individualTarget (i.e. {"a1c":7.5,"individualTarget":8.0})
      - Output: glycemic control recommendation (i.e. "below individual target, no additional agents")
      - ArkID: ark:/99999/fk41g0zd0q

   5. Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus: Step 1 
      - Input: systolic, diastolic, albuminLevel (i.e. {"systolic":300,"diastolic":0,"albuminLevel":400})
      - Output: pharmacological treatment recommendation (i.e. "Albumin levels indicate macroalbuminuria.")
      - ArkID: ark:/99999/fk49c76k8x

   6. Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus: Step 2 
      - Input: systolic, diastolic (i.e. {"systolic":10,"diastolic":0})
      - Output: pharmacological treatment recommendation (i.e. "Not applicable, patient doesn't have high blood pressure.")
      - ArkID: ark:/99999/fk4w66qt8k

   7. Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus: Step 3
      - Input: systolic, diastolic (i.e. {"systolic":150,"diastolic":90})
      - Output: pharmacoogical treatment recommendation (i.e. "If above agents are contraindicated or dose is optimized and patient BP remains >= 140/90-, Add a Dihydropyridine Calcium Channel Blocker - initiate therapy, Amlodipine (Norvasc) 2.5-2mg daily. Titrate by doubling dose in 2-4 weeks if BP goal is NOT met (max dose: 10mg)"
      - ArkID: ark:/99999/fk4rf6114q

   8. Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus: Step 4 
      - Input: systolic, diastolic (i.e. {"systolic":10,"diastolic":0})
      - Ouput: pharmacologic treatment recommendation (i.e. "Not applicable, patient doesn't have high blood pressure.")
      - ArkID: ark:/99999/fk4mp5968n

   9. Classifying Candidate Patients that would Benefit from Tight Control: Result
      - Input: comorbidities, advanced complications, treatment safety, life expectancy, hypoglycemia hisory, hypoglyocemia unawareness, vascular disease, autonomic neuropathy, hypoglycemia comorbidities, poor support (i.e {"comorbidities":"1","advComplications":"1","treatmentSafety":"1","lifeExpectancy":"1","hypoglycemiaHistory":"1","hypoglycemiaUnawareness":"1","vascularDisease":"1","autonomicNeuropathy":"1","hypoglycemiaComorbidities":"1","poorSupport":"1"})
      - Output: candidiate for tight control (i.e.  "no")
      - ArkID: ark:/99999/fk4hq46j3g

   10. Agent Weight Change Informative 
       - Input: agent (i.e. {"agent":"Glucophage XR"})
       - Output: weight change information (i.e. "likelihood of weight loss")
       - ArkID: ark:/99999/fk4d50wh15

   11. Agent Renal Dose Adjustment 
       - Input: agent (i.e. {"agent":"miglitol"})
       - Output:recommended renal dose adjustment (i.e. "Contraindicated for CrCl <25 ml/min")
       - ArkID: ark:/99999/fk48d05q0d


### Survey/Checklist instruments
We have also created 3 helpful survey and checklist instruments that can be utilized to get data.

   1. Classifying Candidate Patients that would Benefit from Tight Control: survey [html survey instrument](./classifying-candidate-for-tight-control/resource/classifying-candidate-for-tight-control-of-blood-glucose.html)
      - Responses are sent to Classifying Candidate Patients that would Benefit from Tight Control: Result (ark:/99999/fk4hq46j3g)

   2. Self Management Topics: Annual Visit [html checklist instrument](./self-management-topics/annual/self-management-topics-annual.html)
      - Checklist of topics

   3. Self Management Topics: Regular Visit [html checklist instrusment](./self-management-topics/regular/self-management-topics-regular.html)
      - Checklist of topics
