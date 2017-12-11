# Lung Cancer Validator

The Lung Cancer Validator is a python script which allows a user to supply a formatted excel spreadsheet of patient data which will be read and formatted into RESTful API calls to the KnowledgeGrid database, providing lung cancer risk scores generated from multiple published models. The response of these calls are then written to a new sheet of the provided excel file. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See 'Running the tests' for further information on example API calls, and input/output formatting.

### Prerequisites

The Lung Cancer Validator makes calls to the Knowledge Grid Activator hosted remotely at kgrid.med.umich.edu, so no local files are necessary beyond the executable and input files. A template for the excel input file can be found [here](/template.xlsx).

The **xlrd** and **xlwt** plugins are used in this project for implementing excel reading/writing functionality. If not already installed, follow their respective [links](/README.md/Built_With) to download, then navigate to that directory and run the following: 

```
python setup.py install
``` 

### Running

Direct to repository where file is saved and run the Lung Cancer Validator executable

```
python validator.py
```

Provide name of the input file containing the patient data

```
Input File: data.xlsx
```

File will run and responses will be recorded in the same file under sheetname "Model Output".

## Running the tests

Sample input and output can be found in the /test folder.

### activator_test

This test file runs API calls to each of the eight lung cancer prediction models from their respective test cases based on hard coded variables (i.e. without the need for excel functionality).

```
python activator_test.py
```

### validator_test_2

This test file is to assure the reading/writing functionality of the Validator. Issues with this program may be indicative of an outdated version of the plugin used for this project, which can be troubleshooted [here](http://www.python-excel.org/).

```
python validator_test.py
```


## Built With

* [KnowledgeGrid](http://kgrid.org/) - The database system used
* [xlrd](https://github.com/python-excel/xlrd) - Plugin for data extraction from excel
* [xlwt](https://github.com/python-excel/xlwt) - Plugin for generating excel spreadsheets

## Authors

* **Jack Allan** - *University of Michigan '20* - [Contact](mailto:jackall@umich.edu)
* **Natalie Lampa** - *University of Michigan '20* - [Contact](mailto:nlampa@umich.edu)


## Acknowledgments

* Allen Flynn
* Matt Fiorillo
