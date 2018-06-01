# No Install Required Version of the Knowledge Grid Activator


## Getting Started

These instructions will get you interacting with a version of the Knowledge Grid Activator which is hosted remotely at http://kgrid.med.umich.edu/stack2/health . 

### Prerequisites

* No Install Necessary


### Interacting with the Activator
**Step 1** Navigate to your browser and check the status of the remotely hosted activator.


http://kgrid.med.umich.edu/stack2/health


![Remote Activator](/activator-workshop/screenshots/healthraw.png?raw=true)


If working properly, the "Number of objects on the shelf" should be 41. This is the number of Knowledge Objects available for use.


## Web Based API Interaction Through SwaggerUI

SwaggerUI is a web-based API tool which we will be using today to interact with the remotely hosted version of the Knowledge Grid Activator without having to download any external software or use the command line. 

**Step 1** Navigate to https://kgrid-demos.github.io/swaggerui/ in your web browser where we have a list of Knowledge Objects ready to be used. 

* Knowledge Object with id = ark:/99999/fk49z9gr7p is the object for determining phenotype based on the genotype of the CYP2D6 gene.
* Knowledge Object with id = ark:/99999/fk4mc97w6m is the object for retrieving Codeine dosing recommendations based on CYP2D6 phenotype.

![SwaggerUI](/activator-workshop/screenshots/swaggerhome.png?raw=true)

**Step 2** Watch video demonstration below, and follow these steps as shown. 
* Click on one of the green "Post" boxes
* Click "Try it out"
* The request body already contains the necessary message, so you need only click "Execute"
  - _Tip_ Chrome and other browsers may try to block this web client as a security precaution, click on the alert and then click "Allow Scripts to Run" (as shown in the video below).
* Scroll down to the reponse and view the result given by the Knowledge Object


![Demo](/activator-workshop/screenshots/get.gif?raw=true)

**_For Step 2, here is what you're doing..._**
When you execute the genotype to phenotype Knowledge Object (ark:/99999/fk49z9gr7p) you are sending a request with a patient's genetic data and getting their phenotype as a response.

Then, when executing the Codeine recommendation object (ark:/99999/fk4mc97w6m) you are sending a request containing the patient's phenotype and getting a recommendation for that patient about using Codeine.

By doing these things, you are exploring a new way of applying computable algorithms to patient data using APIs. 



## Interacting With a Knowledge Object Using the MacOS Terminal

A list of Clinical Pharmacogenetics Implementation Consortium (CPIC®) guidelines can be found in knowledge object form in the [Knowledge Grid Library](http://kgrid.med.umich.edu/library2/#/). This tutorial will be using two objects authored for determining Codeine reccomendations based on the CYP2D6 gene, which can be found [here](https://umich.box.com/v/CPICKnowledgeObjects).


For MacOS users, the following cURL commands can be run directly from the command line. If you are working in a Windows or Linux environment, naviagate to https://kgrid-demos.github.io/swaggerui/ in your browser and skip to the next section of these instructions, [Web Based API Interaction Through SwaggerUI](https://github.com/kgrid/knowledge-objects/blob/master/activator-workshop/no_install_required.md#web-based-api-interaction-through-swaggerui).


**Step 2** Open the command line (MacOS Users).

![Search Terminal](/activator-workshop/screenshots/search_terminal.png?raw=true)


**Pre-Written Commands**

Use a cURL Command to get CPIC Object #1, this is the object that maps genotype to phenotype for the CYP2D6 gene.
```
curl -X GET \
  http://kgrid.med.umich.edu/stack2/knowledgeObject/ark:/99999/fk49z9gr7p \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 1e486f30-ba1b-4b05-a94f-f0a70cc578bc'
```


Use a cURL Command to get CPIC Object #2, this is the object that returns Codeine dosing recommendations based on the CYP2D6 gene information.
```
curl -X GET \
  http://kgrid.med.umich.edu/stack2/knowledgeObject/ark:/99999/fk4mc97w6m \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 85b5ac3f-b886-4b58-ace9-397fe7741c0f'
```



Use a cURL Command to engage CPIC Object #1.
```
curl -X POST \
  http://kgrid.med.umich.edu/stack2/knowledgeObject/ark:/99999/fk49z9gr7p/result \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: b944f1d5-d34a-4182-8bbf-9a3a8f25a25d' \
  -d '{"diplotype":"","allele1":"*3","allele2":"*3"}'
```



Use a cURL Command to engage CPIC Object #2.
```
curl -X POST \
  http://kgrid.med.umich.edu/stack2/knowledgeObject/ark:/99999/fk4mc97w6m/result \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: ef25c4be-8dc6-4365-88de-8705015b77d9' \
  -d '{"phenotype": "Normal metabolizer", "choice":"1"}'
```


**Example**

*API response in Terminal showing the recommended dosing*
![Reccomendation](/activator-workshop/screenshots/curl4.png?raw=true)





## Authors

**Allen Flynn** and **Jack Allan** of the Knowledge Grid Team in the Department of Learning Health Sciences, Michigan Medicine


<img src="/activator-workshop/screenshots/kgrid.png?raw=true" width="100">
<img src="/activator-workshop/screenshots/medschool.png?raw=true" width="200">



