# Installation Instructions for the Knowledge Grid Activator



## Getting Started

These instructions will get you a copy of the Knowledge Grid Activator up and running on your local machine for interaction with a pre-authored knowledge object. 

### Prerequisites

* [Java](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) - Must be updated to version 8
* [Postman](https://www.getpostman.com/)
* **Optional** [JSON Formatter for Chrome](https://chrome.google.com/webstore/detail/json-formatter/cfaihfocdnniaholfnjcemnfhcjchohb) - Better viewing for JSON files in web browser.


### Installing



**Step 1** Download starter files from https://umich.box.com/v/KnowledgeGridStarterKit .

**Step 2** Arrange files in appropriate two-folder structure.

One folder for storing Knowledge Objects:
```
/users/name/activator/shelf
```

and a second folder for the adapter:

```
/users/name/activator/adapters
```

**Step 3** Navigate to the command line (Terminal on MacOS and Command Prompt on Windows) and run the Activator start up command.
![Terminal](/screenshots/terminal.png?raw=true)
<!-- ![Command Prompt](https://raw.github.com/ryanmaxwell/iArrived/master/Screenshots/Settings.png) -->

```
java –jar activator-0.5.8.SNAPSHOT.war
```

**Step 4** Navigate to your browser and confirm that the Activator is live by running the following command:

```
http://localhost:8082/shelf
```


### Interacting With a Knowledge Object

A list of Clinical Pharmacogenetics Implementation Consortium (CPIC®) guidelines can be found in knowledge object form in the [Knowledge Grid Library](http://kgrid.med.umich.edu/library2/#/). This tutorial will be using an object authored for determining Codeine reccomendations based on the CYP2D6 gene, which can be found here: [x]()


**Step 5** Start Postman and import the Postman Files from [Box](https://umich.box.com/v/KnowledgeGridStarterKit).
![Postman_import](/screenshots/postman_import.png?raw=true)

Within this folder you can find a series of PUT and GET commands which will allow you to interact with the CYP2D6 knowledge objects.



- [ ] 




## **_Optional_** Create a Knowledge Object using the CPIC Wizard

Explain what these tests test and why

###Prerequisites
* Python, version 2.7 or above
* [pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)
```
sudo apt-get install python3-pip
```
* [XLRD](https://pypi.python.org/pypi/xlrd)
```
pip3 install xlrd
```



```
Give an example
```



## Built With

* [KnowledgeGrid](http://kgrid.org/index.html) - The web framework used


## Authors

* **Allen Flynn**
* **Jack Allan**


## Acknowledgments



