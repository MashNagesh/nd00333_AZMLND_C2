<H2> UDACITY || Machine Learning Engineer with Microsoft Azure Nanodegree Program || PROJECT 2 - OPERATIONALIZING THE ML MODELS </H2>

<H3> OVERVIEW </H3>

The obejctive is to use Azure to configure a cloud-based machine learning production model, deploy it, and consume it and also to create, publish, and consume a pipeline.

<H5> Data Set Used </H5> 
Bank Marketing Dataset :This dataset contains data from a marketing campaign of a bank.The classification goal is to predict if the client will subscribe a term deposit (y).

(Source: https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv)

<p>We have used the following to arrive at the best model

1. AutoML method from Studio

2. AUTOML config using Python SDK</p>

<H3> ARCHITECTURE </H3>

The following steps have been used to achieve the desired result:

1. Authentication
2. Automated ML Experiment
3. Deploy the best model
4. Enable logging
5. Swagger Documentation
6. Consume model endpoints
7. Create and publish a pipeline

![image](https://user-images.githubusercontent.com/26400438/124588424-6829a900-de76-11eb-91f9-0a4499304510.png)

The details of each of these steps are explained along with  Snapshots  in the next section.

<H3> SCOPE FOR IMPROVEMENT </H3>

The focus of the current project is about understaing the steps involved in operationalising the models.Some of the other areas that can be considered 

1.Accuracy has been considered as an evaluation metric which is not the right metric for imbalanced datasets.This could have been optimised to arrive at optimal models.

2.Benchmark section to be explored 

<H3> MAIN STEPS  </H3>

<H5>1.  Authentication : </H5>

Creation of Service Principal and allowing Service Principal to access workspace

![image](https://user-images.githubusercontent.com/26400438/124589468-a96e8880-de77-11eb-98eb-06f679853f7d.png)

<H5>2.  Automated ML Experiemnt : </H5>

2a. Registered Dataset with Bank Marketing Dataset - Using the bank marketing DataSet for the AutoML experiment

![Regd_DS](https://user-images.githubusercontent.com/26400438/124589738-f3576e80-de77-11eb-8ff9-7cbe39ed1b52.PNG)

2b. Experiment Completed - The below screen shot shows the status of the experiment as complete after nearly running for 60 minutes.
Cluster Choice : A standard_DS12_V2 was chosen with minimum node as  1
Additional Configuration : Default Exit criterion is set to 60 minutes and concurrency is set to  5


![Experiment_completion](https://user-images.githubusercontent.com/26400438/124589853-12ee9700-de78-11eb-970e-642ff2658142.PNG)


2c.  Best Model - the choice of Best model is based on  the evaluation criteria specified while defining the AutoMl model.**Accuracy** is chosen as the evaluation metric and the Voting Ensemble model has been chosen as the best model in this case.

![Voting_Ensemble_Best_Model](https://user-images.githubusercontent.com/26400438/124589902-213cb300-de78-11eb-9636-b430a6c16b26.PNG)


The performance of the chosen model on other metrics can be seen using the "View Explanations" options.Below snapshot shows that the chosen best model has performed fairly well against other evaluation metrics as well.
![image](https://user-images.githubusercontent.com/26400438/124603061-29e8b580-de87-11eb-9d9e-e7d7c3d369b1.png)


<H5>3.  Deploy the Best Model : </H5>

Deploying the Voting Ensemble model using ACI


![image](https://user-images.githubusercontent.com/26400438/124590399-b6d84280-de78-11eb-84bd-a66c752e448a.png)


Status of Deployed Model :Below screenshot shows that the deployed model is healthty.The main intention of the deployment is to be able to use.Azure also helps us with a consume section which will help the users with ways to consume the delpoyed service.

![image](https://user-images.githubusercontent.com/26400438/124590511-d8392e80-de78-11eb-9b01-b05ec3245c3e.png)


<H5>4. Enable Logging : </H5>

Application Insights is an application performance management service for web applications that enables us  to do all the monitoring of performance in Azure.
As a default option the Application Insights is not enabled.The same is enabled using the below command:
service.update(enable_app_insights=True).
Upon enabling the same we are able to see that the API URL is available 

![image](https://user-images.githubusercontent.com/26400438/124590690-0f0f4480-de79-11eb-9fe9-1874a4c4f3c3.png)

Output from Logs.py: Logs  contain the information on which part of the code is executed and what problems have been arisen.

![image](https://user-images.githubusercontent.com/26400438/124590769-25b59b80-de79-11eb-9e08-c7421c5cc342.png)


<H5>5. Swagger Documentation : </H5>


Swagger is an Interface Description Language for describing RESTful APIs expressed using JSON. (Wiki) .Swagger includes automated documentation, code generation, and test-case generation.Swagger enabled using the Swagger.sh started code at port - 9000 and the API interface is shown

![Swagger](https://user-images.githubusercontent.com/26400438/124591715-3dd9ea80-de7a-11eb-834e-f19478091486.PNG)


<H5>5. Consume Model Endpoints : </H5>

The endpoint.py script is interacting with the API to produce the JSON output.
The consume section provides the REST API URL  and the key to access the deployed model

![image](https://user-images.githubusercontent.com/26400438/124604706-d37c7680-de88-11eb-85cb-4e208461eb95.png)

Data is passed in the below fashion using a Python script(endpoint.py)

   
         {
            'age': 39,
            'job': "management",
            'marital': "married",
            'education': "university.degree",
            'default': "no",
            'housing': "yes",
            'loan': "no",
            'contact': "telephone",
            'month': "nov",
            'day_of_week': "wed",
            'duration': 204,
            'campaign': 1,
            'pdays': 3,
            'previous': 0,
            'poutcome': "success",
            'emp.var.rate': -0.1,
            'cons.price.idx': 93.2,
            'cons.conf.idx': -42,
            'euribor3m': 4.633,
            'nr.employed': 5195.8
        },
        
        {
            "age": 27,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 400,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          },


![image](https://user-images.githubusercontent.com/26400438/124591858-6cf05c00-de7a-11eb-9d93-95ce065ced39.png)


<H5>6. Create and Consume Pipelines : </H5>

6.a Pipeline Creation

Some of the Pre-requisite steps is as follows :

A. Use the config.Json (Contains Workspace, Resource Group and Subscription details) to  initialize workspace.

B. Create a compute cluster or Use the existing cluster which was created for the AutoML model from Studio

C.Bank marketing Data Set which was registered in the earlier step is being used

![Bank_Mktng_DS](https://user-images.githubusercontent.com/26400438/124592687-572f6680-de7b-11eb-8f8f-820d69d26eeb.PNG)


From Python SDK:
Pipeline is created with the following AUTOML settings

(    "experiment_timeout_minutes": 60,
    "max_concurrent_iterations": 5,
    "primary_metric" : 'accuracy',
    "n_cross_validations": 5


Detailed StepRuns during the creation of the Pipeline


![image](https://user-images.githubusercontent.com/26400438/124594492-7929e880-de7d-11eb-88ed-33464f6ceb29.png)


![StepRun](https://user-images.githubusercontent.com/26400438/124592851-8d6ce600-de7b-11eb-9404-cfca0a61a64d.PNG)

![image](https://user-images.githubusercontent.com/26400438/124592389-0881cc80-de7b-11eb-9158-9f7552512246.png)

![image](https://user-images.githubusercontent.com/26400438/124592279-e8eaa400-de7a-11eb-9d4f-c33198987876.png)


6.b Published Pipeline Overview

REST endpoint - Scheduled for run.Intermittent Stage  of the Piepline end point before the status becomes Active

![image](https://user-images.githubusercontent.com/26400438/124592896-9bbb0200-de7b-11eb-98be-2029b61465e6.png)

The Pipeline End point is published and active

![Pub_Pipeline](https://user-images.githubusercontent.com/26400438/124592797-7b8b4300-de7b-11eb-92e0-07f0aa8fd4fb.PNG)


![image](https://user-images.githubusercontent.com/26400438/124601548-9793e200-de85-11eb-92e0-f72b08a8516c.png)

Pipeline Endpoint -  Publishing the pipeline enables a REST endpoint to rerun the pipeline from any HTTP library on any platform.

![image](https://user-images.githubusercontent.com/26400438/124592745-6adacd00-de7b-11eb-9577-d1f7479a6a23.png)


<H3> SCREEN CAST </H3>

A Screen Recording of the project is available on the link below
Link - https://youtu.be/4VLcUA7lMcY











