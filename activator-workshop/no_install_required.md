# No Install Required Version of the Knowledge Grid Activator


## Getting Started

These instructions will get you interacting with a version of the Knowledge Grid Activator which is hosted remotely at http://kgrid.med.umich.edu/stack2/health . 

### Prerequisites

* [Java](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) - Must be updated to version 8


### Interacting with the Activator
**Step 1** Navigate to your browser and connet to the remote Activator.

```
http://kgrid.med.umich.edu/stack2/health
```

![Remote Activator](/activator-workshop/screenshots/remote_activator.png?raw=true)

**Step 2** Open the command line (Terminal on MacOS and Command Prompt on Windows).

![Search Terminal](/activator-workshop/screenshots/search_terminal.png?raw=true)
![Search Command Prompt](/activator-workshop/screenshots/search_command_prompt.png?raw=true)



## Interacting With a Knowledge Object

A list of Clinical Pharmacogenetics Implementation Consortium (CPIC®) guidelines can be found in knowledge object form in the [Knowledge Grid Library](http://kgrid.med.umich.edu/library2/#/). This tutorial will be using two objects authored for determining Codeine reccomendations based on the CYP2D6 gene, which can be found [here](https://umich.box.com/v/CPICKnowledgeObjects).


For MacOS users, the following cURL commands can be run directly from the command line. If you are working in a Windows or Linux environment, naviagate to https://onlinecurl.com/ in your browser and copy the below commands directly (no need to include your email address). 



Use a cURL Command to get CPIC Object #1, (what it does....)
```
curl -X GET \
  http://kgrid.med.umich.edu/stack2/knowledgeObject/ark:/99999/fk49z9gr7p \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 1e486f30-ba1b-4b05-a94f-f0a70cc578bc'
```


Use a cURL Command to get CPIC Object #2, (what it does....)
```
curl -X GET \
  http://kgrid.med.umich.edu/stack2/knowledgeObject/ark:/99999/fk4mc97w6m \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 85b5ac3f-b886-4b58-ace9-397fe7741c0f'
```



Use a cURL Command to engage CPIC Object #1, (what it does....)
```
curl -X POST \
  http://kgrid.med.umich.edu/stack2/knowledgeObject/ark:/99999/fk49z9gr7p/result \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: b944f1d5-d34a-4182-8bbf-9a3a8f25a25d' \
  -d '{"diplotype":"","allele1":"*3","allele2":"*3"}'
```



Use a cURL Command to engage CPIC Object #2, (what it does....)
```
curl -X POST \
  http://kgrid.med.umich.edu/stack2/knowledgeObject/ark:/99999/fk4mc97w6m/result \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: ef25c4be-8dc6-4365-88de-8705015b77d9' \
  -d '{"phenotype": "Normal metabolizer", "choice":"1"}'
```

*API response in Terminal showing the recommended dosing*
![Reccomendation](/activator-workshop/screenshots/curl4.png?raw=true)


*API response in browser showing the recommended dosing*
![Online Result](/activator-workshop/screenshots/online_response.png?raw=true)


## **_Optional..._** Create a Knowledge Object using the CPIC Wizard

### Prerequisites
* [pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)
```
sudo apt-get install python3-pip
```
* [XLRD](https://pypi.python.org/pypi/xlrd)
```
pip3 install xlrd
```
* [Postman](https://www.getpostman.com/)


## **Optional** Create a Knowledge Object using the CPIC Wizard

Explain what these tests test and why

```
Give an example
```



## Built With

* [KnowledgeGrid](http://kgrid.org/index.html) - The web framework used?
* [Fedora](https://duraspace.org/fedora/) - The .... used

## Authors

* **Allen Flynn**
* **Jack Allan**


## Acknowledgments

* ?

