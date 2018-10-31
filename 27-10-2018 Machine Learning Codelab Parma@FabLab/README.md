![Python](https://img.shields.io/badge/python-2.7,%203.5+-green.svg)
![OS](https://img.shields.io/badge/OS-CentOS%207-orange.svg)
![OS](https://img.shields.io/badge/OS-Ubuntu%2018.04-orange.svg)
[![Platform](https://img.shields.io/badge/Platform-GoogleCloudPlatform-blue.svg)](https://cloud.google.com/free/)
# Data Science & AI | Codelab in Parma
## Descrizione evento
Dopo gli incontri di introduzione ai temi di Data Science, Machine Learning e Artificial Intelligence tenuti presso FabLab e Caffeina, DS&AI Parma vi propone un incontro in cui iniziare a fare insieme i primi passi nel Machine Learning ed AI.

L’incontro sarà strutturato in due parti principali:

* Machine Learning codelab nel quale si introdurranno i principali concetti di ML si vedrà un esempio di applicazione di computer vision
* Machine Learning in the cloud nel quale verranno illustrati i vantaggi nell’utilizzo di piattaforme di cloud computing a supporto di Data Science e Machine Learning 

In entrambi gli interventi i partecipanti potranno portare il proprio laptop per provare in prima persona gli strumenti mostrati.

## Requisiti per seguire le attività pratiche

Durante la presentazione verranno utilizzati i seguenti strumenti:

* python
* jupyter
* pip
* java
* sklearn
* mxnet
* h2o
* tensorflow
* keras
* plotly
* pandas
* numpy
* matplotlib

È inoltre possibile seguire la presentazione in maniera interattiva sul proprio PC o anche su una istanza di Google Cloud Platform (per questo è necessario creare un account GRATUITO GCP https://cloud.google.com/free/).

Tutto il codice necessario è disponibile al download dal repository Git pubblico https://github.com/lucafon/DS-AI-Parma.

Per clonare in locale il repository, aprire un terminale ed eseguire:

```
git clone https://github.com/lucafon/DS-AI-Parma.git
```

Per avviare jupyter eseguire:

```
jupyter notebook
```

## Installing instructions

### System packages
#### Centos 7

```
sudo yum install git
sudo yum upgrade python-setuptools
sudo yum install python-pip python-wheel
sudo yum install java-1.8.0-openjdk-devel
```

#### Ubuntu 18.04+

```
sudo apt update
sudo apt install git
sudo apt install python-setuptools python-wheel python-pip
sudo add-apt-repository ppa:webupd8team/java
sudo apt install oracle-java8-set-default
sudo apt install jupyter
```

### Python libraries

```
pip install numpy pandas matplotlib sklearn plotly mxnet h2o tensorflow keras jupyter
```

## Programma
### Opening & Intro (16:00 - 16:30)

Introduzione al DS&AI group di Parma, registrazione, setup.

### Getting started with AI - Computer Vision 101 (16:30 - 17:30)
#### Agenda
* Machine Learning & Computer Vision
* Digit recognition - MNIST data set
* Artificial Neural Networks
* Fully connected NN
* Deep NN
* Convolutional NN

### Pausa (17:30 - 17:45)

### Scaling Machine Learning with Cloud Computing (17:45 - 18:45)
#### Agenda
* Svantaggi del on premise / Vantaggi Cloud Computing
* Principali piattaforme di Cloud Computing
* H2O on Cloud

### Networking, Q&A, B&A (18:45 - 19:00)
