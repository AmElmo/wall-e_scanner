# Wall-E Scanner
### Garbage Object Detection and Classification
Using python machine learning to perform image frame object detection from a video feed to detect and classify different recycling categories of trash.

## Motivation
One of the most important ways to combat climate change is with recycling
-	World generates 2.01 billion tonnes of municipal solid waste annually.
-	At least 33 percent of that—not managed in an environmentally safe manner. 
- 	Worldwide, waste generated per person per day averages 0.74 kilogram but ranges widely, from 0.11 to 4.54 kilograms.

## Possible use Case
Possible use cases of a machine learning model like this would be a recycling centre conveyor belt, or potentially a Wall-E Style trash collecting robot that could sort it into recycling bins.

![image](https://user-images.githubusercontent.com/100606725/189529054-71fdbbc0-e986-4d43-ab58-1c44182ead88.png)

# Project Setup
1.	Object Detection with Tensorflow API
2.	Custom classification training on Trash Datasets
3.	Java Script and React web cam user interface

# Data Source 
-Trash Annotations in Context (TACO) 
http://tacodataset.org/

![image](https://user-images.githubusercontent.com/100606725/189529061-8a575245-b4c8-43ea-85b4-bf8ddbae65c7.png)

@article{taco2020,
    title={TACO: Trash Annotations in Context for Litter Detection},
    author={Pedro F Proença and Pedro Simões},
    journal={arXiv preprint arXiv:2003.06975},
    year={2020}
}

- Kaggle Drinking Waste Classification
https://www.kaggle.com/datasets/arkadiyhacks/drinking-waste-classification

![image](https://user-images.githubusercontent.com/100606725/189529069-51f74e1d-18f0-41cf-bc36-6a15f88428a5.png)

# Data Preprocessing 
Uploaded TACO and Drinking Set data with pre-made annotations to Roboflow, which was then used to create TF Records and CSV.  Able to rename to 7 recycling categories 
1.	Plastic 
2.	Paper 
3.	Metal 
4.	Glass
5.	Organic
6.	Other 
7.	Non-recyclable 

# Object Detection with Tensorflow API
We used transfer learning from the Tensorflow API version 2.8.2 to get the basis of object detection. 

# Custom classification training on Trash Datasets
Follow the steps in notebook:  Wall_E_Scanner_Model_2.ipynb

We trained MobileNet v2 model for the best accuracy and speed. 

We tried Yolo v4 as a base, with good modeling results, however was not able to successfully engineer the model into the java script react video feed frame.

# Java Script and React web cam user interface
Follow the steps in notebook:  Wall_E_Scanner_Model_2.ipynb

The code was hosted on google cloud platform.  We hooked a smartphone camera to be the webcam to use as a video feed. 


# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for wall-e_scanner in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/wall-e_scanner`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "wall-e_scanner"
git remote add origin git@github.com:{group}/wall-e_scanner.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
wall-e_scanner-run
```

# Install

Go to `https://github.com/{group}/wall-e_scanner` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/wall-e_scanner.git
cd wall-e_scanner
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
wall-e_scanner-run
```
