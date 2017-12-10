# Lung Cancer Validator

The Lung Cancer Validator is a python script which allows a user to supply a formatted excel spreadsheet of patient data which will be read and formatted into RESTful API calls to the KnowledgeGrid database, providing lung cancer risk scores generated from multiple published models. The response of these calls are then written to a new sheet of the provided excel file. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See 'Running the tests' for further information on example API calls, and input/output formatting.

### Prerequisites

The Lung Cancer Validator makes calls to the Knowledge Grid Activator hosted remotely at kgrid.med.umich.edu, so no local files are necessary beyond the executable and input files. A template for the excel input file can be found [here](/template.xlsx)

### Running

direct to repository where file is saved and run the Lung Cancer Validator executable

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

### validator_test

which models?

```
lets have this one give a sample output
```

### validator_test_2

which models? what data?

```
and this one write to an excel sheet
```


## Built With

* [KnowledgeGrid](http://kgrid.org/) - The database system used


## Authors

* **Jack Allan** - *University of Michigan '20* - [Contact](mailto:jackall@umich.edu)
* **Natalie Lampa** - *University of Michigan '20* - [Contact](mailto:nlampa@umich.edu)


## Acknowledgments

* Allen Flynn
* Matt Fiorillo
