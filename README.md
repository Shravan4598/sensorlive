# sensorlive
# Air Pressure System (APS) Sensor Fault Detection

![Logo](https://www.intel.com/content/dam/develop/public/us/en/images/thumbnails/tool-thumbnail-beta-oneapi-logo.jpg)

## Problem Statement
The Air Pressure System (APS) is one of the important component of a heavy-duty vehicle that uses compressed air to force a piston to help for pressure to the brake pads. This is more sustainable and easy availability

This is a Binary Classification problem, in which the positive class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.


## Dataset Description
- The training set contains 36188 examples in total in which 35188 belong to the negative class and 1000 positive.

- The attribute names of the data have been anonymized for proprietary reasons. It consists of both single numerical counters and histograms consisting of bins with different conditions.

- In total there are 171 attributes and one target variable.
- Link for Dataset: https://drive.google.com/file/d/1jHWPdnzAKZIVFI5_UxaG-A6yV6E5mVGf/view?usp=sharing

## Challenges with Dataset

- Most of the columns in the dataset contains null values, some of them more contain 70%. 

- The Dataset is highly imbalanced.

## Model Evalution Metrics
The Cost function for this problem is 
```
  Total_Cost = (Cost_1 x No_Instances) + (Cost_2 x No_Instances)
```

- Cost_1 = 10 and Cost_2 = 500.
- Cost_1 → cost that an unnecessary check needs to be done by an mechanic at a workshop.                     
- Cost_2 → cost of missing a faulty truck which may cause a breakdown.





## Tech Stack 

- **Intel One API**
- **Confluent Kafka**
- **Python**
- **MongoDB**

## Proposed WorkFlow

- The Data generted by the APS Sensors in fixed time intervals is send to Kafka (Confluent Kafka), which is a live data streaming platforms to store the large amount of data recieved from the sensor.

- For flexibility, the data present in the Kafka topic is written into a MongoDB Database whenever the model needs to be trained.

- Finally, a .csv file is created by extracting the data from the MongoDB.

- Performing different experiments with Imputers (KNN Imputer, Simple Imputer),Scalers(Min-Max Scaler, Robust Scaler) and check which gives the best result when model training.

- The Dataset is balanced using oversampling techniques like SMOTE and TOMEK to remove nosie created in the process of oversampling.

- Traing the Data using different model like RandomForest,Logistics Regression, K-Nearest Neighbour using the One-DAL library of Intel's ONE API. 

- Choose the trained model with best acuuracy and less cost function.
### workflow
![Workflow](flowchart/10%20img.png)
### Model Training workflow
![TrainingWorkflow](flowchart/11%20img.png)
## Future Work
- As of now, the data is not directly recorded from the APS sensors. This project can be taken further by obtaining the data directly from the sensor and keep monitoring the performance of the trained model.
