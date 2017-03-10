# Classifying Candidates for Tight Control of Blood Glucose: Survey & Results
Created: January 23, 2016

UMMG Clinical Value and Innovations

Clinical Alignment & Performance Excellence

University of Michigan

### Objective
These knowledge objects (KO) represent an HTML survey with JSON-formatted output, and a results script that interprets the survey response, and outputs the result at the bottom of the survey page. This KO is derived from Table 5: Targeting and Monitoring Glycemic Control in Patients with Diabetes Mellitus. See Literature section for more information.

To utilize these KO, simply open the file in any browser.

### Description
The resource (survey) is an HTML version of the questionnaire. When the survey is completed, the HTML output is converted to JSON, and POST to the second knowledge object, the result (scoring) (the knowledge objects are hard coded to operate this way).

The result knowledge object takes in the JSON-formatted responses, and outputs whether the patient would or would not be a good candidate.

If wanting to run the result function separately, the input needs to be formatted like this:
surveyResults({"comorbidities":"0","advanced-complications":"0","treatment-safety":"0","life-expectancy":"0","hypoglycemia-history":"0","hypoglycemia-unawareness":"0","vascular-disease":"0","autonomic-neuropathy":"0","hypoglycemia-comorbidities":"0","poor-support":"0"})

### Object Teller information
Classifying Candidates for Tight Control of Blood Glucose: Survey - **ark:/99999/fk4d22641k**

Classifying Candidates for Tight Control of Blood Glucose: Result - **ark:/99999/fk4hq46j3g**


### Related Objects/Future Development
These KO were created with other diabetes KO in hopes to create a collection of KO helpful for the diabetes community.

### Literature
The documentation can be found at: https://www.med.umich.edu/1info/FHP/practiceguides/diabetes/dm.pdf
