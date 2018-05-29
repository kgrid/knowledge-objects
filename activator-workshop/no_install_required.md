# No Install Required Version of the Knowledge Grid Activator


## Getting Started

These instructions will get you interacting with a version of the Knowledge Grid Activator which is hosted remotely at http://kgrid.med.umich.edu/stack2/health . 

### Prerequisites

* [Java](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) - Must be updated to version 8


### Interacting with the Activator
**Step 1** Navigate to your browser and check the status of the remotely hosted activator.

```
http://kgrid.med.umich.edu/stack2/health
```

![Remote Activator](/activator-workshop/screenshots/remote_activator.png?raw=true)


If working properly, the "Number of objects on the shelf" should be 41. This is the number of Knowledge Objects available for use.


## Interacting With a Knowledge Object

A list of Clinical Pharmacogenetics Implementation Consortium (CPIC®) guidelines can be found in knowledge object form in the [Knowledge Grid Library](http://kgrid.med.umich.edu/library2/#/). This tutorial will be using two objects authored for determining Codeine reccomendations based on the CYP2D6 gene, which can be found [here](https://umich.box.com/v/CPICKnowledgeObjects).


For MacOS users, the following cURL commands can be run directly from the command line. If you are working in a Windows or Linux environment, naviagate to https://onlinecurl.com/ in your browser and copy the below commands directly (no need to include your email address to use this website). 


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


*API response in browser showing the recommended dosing*
![Online Result](/activator-workshop/screenshots/online_response.png?raw=true)



## Authors

* **Allen Flynn**
* **Jack Allan**


