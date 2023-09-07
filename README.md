# Machine Learning for Stroke Risk

## **Team  - Project 2**

### Ethan Brush
### Ivan Milivojevic
### Maximus Onwukanjo
### Alex Melino
 
#

## **Overview**

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths. Stroke is said to be a blocked artery (ischemic stroke) or leaking or bursting of a blood vessel.

The dataset used (located in the *'Resources'* folder of this repo) for this project is used to predict whether a patient is likely to get stroke based on several input parameters like gender, age, various diseases, and smoking status. The dataset was sourced from Kaggle.com, a popular repository for datasets and information.

The goal of the project was to create and test various Machine Learning models to predict whether a person is at risk of having a stroke and what the important factors would be in identifying that risk. Using the best performing model, the idea was to create an interactive application using Streamlit linked to the model that can be used to predict whether a person is currently at risk of having a stroke based on their input data.

The main program file is *'machine_learning_for_stroke_risk.ipynb'*, and the *'strokeapp.py'* file contains the code for the stroke risk indicator application.
#


## **Data Analysis and Visualization**

The necessary libraries for machine learning were imported: pandas, numpy, seaborn, matplotlib, tensorflow, streamlit as well as all the various sklearn modules for each machine learning method. The .csv file was then read and the data was cleaned up for analysis.

The data was then visualized to present the information with alternative visual tools for a better analysis of what the data actually says. The various visualizations can be found in the *'Images'* folder fo this repo.

After initial analysis and data visualization, it was determined that the dataset is imbalanced (apporximately a 19:1 ratio of no-stroke to positive stroke signals)

![Stroke Proportion](Resources/stroke_proportion.png)

Additionally, some feature engineering was done to create a new column of data based on the number of potential risks. If a patient has a positive signal for a risk (ie. high bmi or glucose levels, hypertension, heart disease, smoking status) they were given a '1'. The 'number of risks' column summs up the total potential risk factors and acts as a solid indicator feature.

![Number fo Risks](Resources/risk_visual.png)

Due to the imbalanced nature of the data, the SMOTEEN oversampling technique was used to improve machine learning capability. Additionally, the data was scaled and split into testing and training sets for use in the models.
#

## **Machine Learning**

* Machine Learning models explored:
  * Logistic Regression Model
  * Random Forest Classifier
  * Support Vector Machine Classifier
  * Decision Tree Classifier
  * KNN Classifier
  * Stacking Classifier 
  * Neural Network

The most important metric to measure the performance of these models is the recall score, that is, the ability for the model to allow the fewest number of missed positive stroke signals to slip through. Based on thsi metric, the Logistic Regression classifier produced the best results.

![Model Performance](Resources/model_performance.png)
#

## **Stroke Risk Indicator App**

After identifying the best performing machine learning model, that model was used to create an application using Streamlit. The application asks the user questions to gather various data that mimics what is present in the initial dataset. The logistic regression model is then applied to the user's input and it provides the used with feedback about if they are at risk of stroke or not.

