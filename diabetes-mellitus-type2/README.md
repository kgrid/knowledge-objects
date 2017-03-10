# Diabetes Mellitus Type II Knowledge Objects
Based off the following practice guidelines: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf

Within each knowledge object repository, we have included the python code, an input RDF, an output RDF, a README, and the clinical documentation where the knowledge was extracted from. The README contains important metadata, along with information on how to execute the object locally and how to execute the object using REST API.

We have created a collection of these knowledge objects that can be found in the following file: dm.json. This collection contains a list of commands for these knowledge objects, including a PUT(ADD/UPDATE) command and a POST command for each one. The collection can be directly imported to a REST API client; we use postman.


The completed knowledge objects are as follows (also on ObjectTeller):

   1. Type II Diabetes Diagnosis (ark:/99999/fk4gm8g63d)
 
   2. Meal Planning For Glycemic Management based on Medication (ark:/99999/fk4vm4hg3v)

   3. Steps in Glycemic Control with oral agents: 1 Agent (ark:/99999/fk4fn1fb10)

   4. Steps in Glycemic Control with oral agents: Addition of 2nd Agent (ark:/99999/fk41g0zd0q)

   5. Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus: Step 1 (ark:/99999/fk49c76k8x)

   6. Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus: Step 2 (ark:/99999/fk4w66qt8k)

   7. Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus: Step 3 (ark:/99999/fk4rf6114q)

   8. Steps in Pharmacologic Treatment of Hypertension in Patients with Diabetes Mellitus: Step 4 (ark:/99999/fk4mp5968n)

   9. Classifying Candidate Patients that would Benefit from Tight Control: Result (ark:/99999/fk4hq46j3g)

   10. Agent Weight Change Informative (ark:/99999/fk4d50wh15)

   11. Agent Renal Dose Adjustment (ark:/99999/fk48d05q0d)


### Survey/Checklist instruments
We have also created 3 helpful survey and checklist instruments that can be utilized to get data.

   1. Classifying Candidate Patients that would Benefit from Tight Control: survey [html survey instrument](./classifying-candidate-for-tight-control/resource/classifying-candidate-for-tight-control-of-blood-glucose.html)
      - Responses are sent to Classifying Candidate Patients that would Benefit from Tight Control: Result (ark:/99999/fk4hq46j3g)

   2. Self Management Topics: Annual Visit [html checklist instrument](./self-management-topics/annual/self-management-topics-annual.html)
      - Checklist of topics

   3. Self Management Topics: Regular Visit [html checklist instrusment](./self-management-topics/regular/self-management-topics-regular.html)
      - Checklist of topics
