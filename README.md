# TSA-ML

TSA-ML is a data pipeline that integrates survey data from diverse sources. A piece of work that demostrate my interest in the region. More information about this work is on the [official website](http://#).

---

![alt text](resources/pipeline_diagram.png)

TSA-ML is a data pipeline which:

* **Transforms and ingest** microeconomic data from surveys drawn from diverse sources, mainly in the East-Asia region. It provides granular data at the level of the individual which allows powerful analytics and predictions.

* **Links** different sources using Resource Description Framework (RDF) and SPARQL W3C standards. Data is stored in a graph database, and interconnects data via Schema.org volcabulary.

* **Automates** the data preprocessing stage using Natural Language Processing (NLP), machine learning, and AI.

## Public datasets

Below is a list of the datasets currently used in the system.

| Region | Source | Owner | Description | Link
|:------|:-------------------|:----------------|:----------------------------------|:--------------|
| Taiwan |  Taiwan Social Change Survey (TSCS) | Center for Survey Research, Academia Sinica | A longitutindal dataset containing survey data on different social topics such as employment, family, and social networks. The TSCS contains data from the 1980's from individuals and families across Taiwan. | [Link](https://www2.ios.sinica.edu.tw/sc/en/home2.php)
| Taiwan |  World Values Survey (WVS) | Research Center for Humanities and Social Sciences, Academia Sinica, Taipei | Social surveys conducted in 2019, 2012, 2006, and 1998 | [Link](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp) 
| Hong Kong |  World Values Survey (WVS) | Department of Government and International Studies, Hong Kong Baptist University | Social surveys conducted in 2018, 2014, and 2005 | [Link](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp)
| Macao | World Values Survey (WVS) | Faculty of Social Sciences, Avenida da Universidade | Social surveys conducted in 2019 | [Link](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp)
| China |  World Values Survey (WVS) | Public Opinion Research Center of School of International and Public Affairs at Shanghai Jiao Tong University | Social surveys conducted in 2018, 2013, 2007, 2001, 1995, and 1990 | [Link](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp)

## Quick Start

### Requirements and Installation

Need to install the following in your environment:

* Python 3.9.6
* R version 4.2.3
* Docker 4.19.0
* AllegroGraph 7

### What is in this repository?

This repository contains the following:

* Ingestion folder containing the ingestion files for graph database (`./ingestion/`).
* The landing web page.
* The python scrip that loads ingestion file (`ingest_json.py`).
* The jupyter notes contains tutorials and use cases (`.ipynb` files).

### Setup graph database

Install and activate virtual environment for TSA-ML graph database.

```
$ python3 -m venv tsaml
$ source tsaml/bin/activate
```

Install python libraries for AllegroGraph database. 

```
$ pip3 install agraph-python
```

Start up AllegroGraph database using Docker.

```
$ docker start agraph
```

To stop AllgegroGraph database instance using Docker.

```
$ docker stop agraph
```

## Data Ingestion

### Uploading the data in the graph database

Graph database can ingest TSA-ML data in various ways. Data can be manually moved or copy into the directory that contains the AllegroGraph installation on the local or remote machine. If you have a copy of the directory containing the data files of a specific data repository, then it can be simply copy and pasted from command land. Go into Docker then under `Containers` > `agraph` > `Files`. Under the `agraph` folder in the file explorer, drill down to `data` > `rootcatalog` > [database repository name]. This folder contains all of th TSA-ML files and subfolders. All contents of this 

Data can also be ingested via python script using command prompt. Note, in the `inguest_json.py`, a string variable called `pwd_ingest` can be set to the directory containing the json files, in this case, it is `./ingestion`.

```
$ python3 ./inguest_json.py
```

Data processing can take some time, as there are 2,395,151 statements. If the script is running on a local machine, it may stall or interrupt. In this instance, re-run the script using the above command.

### Testing data

This curl command access the endpoint which will return all triples in the graph database. 

```
$ curl -v -X POST -u [user name]:[password] --data "query=SELECT ?s ?p ?o { ?s ?p ?o . }" http://[host]:[port number]/repositories/[name of the repository]/sparql
```
## Tutorials and Use Cases

### SPARQL 

The [SPARQL Queries](./SPARQL%20Queries%20-%20Use%20Cases.ipynb) tutorial demostrates different SPARQL queries addressing different research questions using the TSA-ML data platform. 

### Research Question on Occupation 

The [tutorial and use case](./Research%20Questions%20-%20Use%20Cases.ipynb) demostrates how TSA-ML can be used to address research questions relating to occupation. This tutorial demonstrates the use of different SPARQL queriesm, machine learning, and AI using python. 

## Contact

Please email your questions or comments to (d01520417@gmail.com).

## Contributing

Thanks for your interest in contributing! There are many ways to get involved;
start by sending us an email to email address listed above or access more information on 
our official [website] (https://#)