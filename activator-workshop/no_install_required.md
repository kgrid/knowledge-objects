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

* ark:/99999/fk49z9gr7p is the Knowledge Object for determining phenotype based on the genotype of the CYP2D6 gene
* ark:/99999/fk4mc97w6m/result is the Knowledge Object for retrieving Codeine dosing recommendations based on CYP2D6 phenotype.

![SwaggerUI](/activator-workshop/screenshots/swaggerhome.png?raw=true)

**Step 2** Engage either of the Knowledge Objects by clicking on their green box >> "Try it out" >> Execute


_Tip_ Chrome and other browsers may try to block this web client as a security precaution, click "Allow Scripts to Run" (as shown in the video below).


![Demo](/activator-workshop/screenshots/get.mp4?raw=true)


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



