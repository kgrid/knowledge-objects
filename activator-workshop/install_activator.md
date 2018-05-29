# Installation Instructions for the Knowledge Grid Activator



## Getting Started

These instructions will get you a copy of the Knowledge Grid Activator up and running on your local machine for interaction with a pre-authored knowledge object. 

### Prerequisites

* [Java](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) - Must be updated to version 8
* [Postman](https://www.getpostman.com/) - An API development environment.
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
http://localhost:8082/health
```
**Tip** /health shows the status of the Activator running locally on your machine. If you properly organized the /shelf files the _"Number of objects on the shelf"_ should be **4** (the two knowledge objects that come pre-installed on the Activator, and the two CPIC objects you downloaded for this activity). 

![MacOS Health](/activator-workshop/screenshots/macos_health.png?raw=true)


### Interacting With a Knowledge Object

A list of Clinical Pharmacogenetics Implementation Consortium (CPIC®) guidelines can be found in knowledge object form in the [Knowledge Grid Library](http://kgrid.med.umich.edu/library2/#/). This tutorial will be using two objects authored for determining Codeine reccomendations based on the CYP2D6 gene, which can be found [here](https://umich.box.com/v/CPICKnowledgeObjects) .


**Step 5** Start Postman and import the Postman Files from [Box](https://umich.box.com/v/KnowledgeGridStarterKit).
![Postman Import](/activator-workshop/screenshots/postman_import.png?raw=true)

Within this folder you can find a series of PUT and GET commands which will allow you to interact with the CYP2D6 knowledge objects.



- [ ] do something with object 1
- [ ] do something with object 2
- [ ] didnt we have four things?
- [ ] I think so...




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


## Authors

* **Allen Flynn**
* **Jack Allan**






