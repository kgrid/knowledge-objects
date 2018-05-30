# Installation Instructions for the Knowledge Grid Activator



## Getting Started

These instructions will get you a copy of the Knowledge Grid Activator up and running on your local machine for interaction with a pre-authored knowledge object. 

### Prerequisites

* [Java](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) - Must be updated to version 8
* [Postman](https://www.getpostman.com/) - An API development environment
* **Optional** [JSON Formatter for Chrome](https://chrome.google.com/webstore/detail/json-formatter/cfaihfocdnniaholfnjcemnfhcjchohb) - Better viewing for JSON files in web browser.


### Installing



**Step 1** Download starter files from https://umich.box.com/v/KnowledgeGridStarterKit .

**Step 2**  Arrange files in appropriate two-folder structure.

One folder for storing Knowledge Objects:
```
/users/name/activator/shelf
```

and a second folder for the adapter:

```
/users/name/activator/adapters
```
![Folder Setup](/activator-workshop/screenshots/folder_setup.png?raw=true)


**Step 3** Open the command line (Terminal on MacOS and Command Prompt on Windows), navigate to the Activator directory, and run the start up command.
```
java -jar activator-0.5.8-SNAPSHOT.war
```

![Terminal](/activator-workshop/screenshots/terminal.png?raw=true)
![Command Prompt](/activator-workshop/screenshots/command_prompt.PNG?raw=true)


**Step 4** Navigate to your browser and confirm that the Activator is live by running the following command:

```
[http://localhost:8080/health]
```
**Tip** /health shows the status of the Activator running locally on your machine. If you properly organized the /shelf files the _"Number of objects on the shelf"_ should be **4** (the two knowledge objects that come pre-installed on the Activator, and the two CPIC objects you downloaded for this activity). 

![MacOS Health](/activator-workshop/screenshots/macos_health.png?raw=true)


### Interacting With a Knowledge Object

A list of Clinical Pharmacogenetics Implementation Consortium (CPIC®) guidelines can be found in knowledge object form in the [Knowledge Grid Library](http://kgrid.med.umich.edu/library2/#/). This tutorial will be using two objects authored for determining Codeine reccomendations based on the CYP2D6 gene, which can be found [here](https://umich.box.com/v/CPICKnowledgeObjects) .


**Step 5** Start Postman and import the 'Postman Files' folder from [Box](https://umich.box.com/v/KnowledgeGridStarterKit).
![Postman Import](/activator-workshop/screenshots/postman_import.png?raw=true)

Within this folder you can find a series of PUT and GET commands which will allow you to interact with the CYP2D6 knowledge objects. The commands in this folder are listed below.



- [ ] **Check Local Activator:** confirms that your Activator is running properly and your knowledge objects are loaded onto the shelf.
- [ ] **Get Shelf From Local Activator:** returns the full list of objects stored on your local Shelf.
- [ ] **Get Single CPIC Object From Local Activator:** returns the knowledge object for going from genotype to phenotype for the CYP2D6 gene.
- [ ] **Get Single CPIC Object From Local Activator:** returns the knowledge object for mapping dosing recommendations based on phenotype for the CYP2D6 gene.
- [ ] **Post Single CPIC Object From Local Activator:** returns metabolizing status based on example gene information.
- [ ] **Post Single CPIC Object From Local Activator:** returns a Codeine dosing reccomendation based on example data. 




## **_Optional..._** Create a Knowledge Object using the CPIC Wizard

### Prerequisites
* Python, version 2.7 or above
* [pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)
```
sudo apt-get install python3-pip
```
* [XLRD](https://pypi.python.org/pypi/xlrd)
```
pip3 install xlrd
```


### Installing



**Step 1** Download “CPIC_GPWizard.py” and the “CYP2D6B_Diplotype_Phenotype_Table.xlsx” data set from https://umich.box.com/v/KnowledgeGridStarterKit .

**Step 2** Open this file with a text editor and update line 49 where the KOFILE variable is set. Change this variable to match the file path to your own shelf from Step 2.

![Link 49](/activator-workshop/screenshots/line49.png?raw=true)

**Step 3** Navigate to your command line and run the CPIC Wizard with the following command:
```
python CPIC_GPWizard.py CYP2D6B_Diplotype_Phenotype_Table.xlsx
```

After successfully running this command, navigate to your shelf folder to confirm that the new Knowledge Object was created. 
 


![new object](/activator-workshop/screenshots/newobject.png?raw=true)

 



### Using The New Knowledge Object


Below is a list of commands that can be used to interact with this newly authored CPIC Knowledge Object. They can either be copied directly into the command line (MacOS) or the Postman Folder can be downloaded from the **CPIC Wizard** folder in [Box](https://umich.box.com/v/KnowledgeGridStarterKit).
```
curl -X GET \
  http://localhost:8080/knowledgeObject/ark:/CYP2D6B/object \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 0e43abb4-7e4e-41bc-ae45-d43631ddcd35'
```


```
curl -X POST \
  http://localhost:8080/knowledgeObject/ark:/CYP2D6B/object/result \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: ca598759-f92a-48fd-8f01-3bcbcdaac8f1' \
  -d '{"diplotype":"","allele1":"*3","allele2":"*3"}'
```




## Authors

**Allen Flynn** and **Jack Allan** of the Knowledge Grid Team in the Department of Learning Health Sciences, Michigan Medicine


<img src="/activator-workshop/screenshots/kgrid.png?raw=true" width="100">
<img src="/activator-workshop/screenshots/medschool.png?raw=true" width="200">







