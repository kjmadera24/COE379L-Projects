# Software Design Project 2 Report

## Overview
The goal of this project is to conduct an exploratory analysis of a specific dataset and 
prepare it for predictive analysis using intelligent system techniques. The aim is to develop
a learning model with supervised learning techniques to predict the recurrence
of breast cancer in patients.

## Data Preprocessing
For this project, a dataset containing information about 286 breast cancer patients was 
provided. Key characteristics included age, degree of malignancy, and tumor size.

Basic data cleaning tasks were performed, including handling null values, and removing 
unnecessary columns, one-hot encoding, and replacement of invalid values.

## Uni/Multivariate Analysis
Before proceeding with one-hot encoding, univariate analysis was performed on select columns.
A histogram of patient ages was generated to understand age distribution, another for the breast 
quadrant column to identify tumor location trends.

I also included a multivariate heatmap plot to show the correlation between every column 
amongst eachother.

## Building & Assessing Models
Three supervised learning techniques, namely K-Nearest Neighbor, Random Forest, and Decision
Tree classifiers, were employed for model development. The dataset was split into 70/30 
train-test sets, with the encoded "class" column serving as the dependent variable. While 
evaluating the models, emphasis was placed on minimizing false negatives, considering their 
greater impact in medical predictions.

### K-Nearest Neighbor
Grid search revealed the best parameter to be 1. However, the model exhibited mediocre performance
on the test data, indicating potential overfitting due to significant disparities between training
and testing accuracies.

### Random Forest
Surprisingly, the Random Forest model demonstrated excellent recall for true values on the test 
data, achieving 100%. Although the overall accuracy was relatively low, the absence of false 
negatives highlights its effectiveness in identifying recurrence.

### Decision Trees
Despite initial expectations, the Decision Trees classifier showed suboptimal performance, 
similar to K-Nearest Neighbor. Overfitting was evident, leading to an undesirable increase in 
false negatives.

## Conclusion
Given the importance of accurate predictions in medical scenarios, particularly in 
identifying cancer recurrence, model selection is crucial. Considering the focus on minimizing 
false negatives, the Random Forest classifier emerges as the preferred choice due to its ability
to achieve high recall for true values.
