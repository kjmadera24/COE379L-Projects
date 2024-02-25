# Software Design Project 1 Report

## Overview
In this project, the goal was to perform an exploratory analysis of a specific dataset and prepare it for predictive analysis using an intelligent system. The primary objective was to achieve the highest accuracy percentage for predictive analysis and fit it to a Linear Regression model. The purpose of this project was to apply skills in data preparation for ease of use and responsible system manipulation to generate accurate predictive results.

## Exploratory Analysis
For this project, a dataset containing information about 398 cars was provided. Key characteristics included mileage, acceleration, and origin.

Basic data cleaning tasks were performed, including handling null values, duplicates, and unnecessary columns. One-hot encoding was applied, particularly to the origin column, for efficiency.

## Uni/Multivariate Analysis Plotting
After data preparation, three plots were generated: two Univariate boxplots of the horsepower and acceleration columns, and a multivariate heatmap of multiple columns including mpg, displacement, horsepower, weight, and acceleration.

## Fit Regression
To investigate factors affecting fuel efficiency, a Linear Regression model was trained and tested. The train_test_split function from Sklearn was used for data splitting. 
The model achieved accuracy scores of 91% and 85% on training and testing data, respectively.

## Conclusion
While the model demonstrates promising accuracy, it's essential to acknowledge potential sources of error, including technological limitations and individual driving habits. 
Personal knowledge of current fuel efficiency trends should complement model predictions. Despite inherent uncertainties, the model provides valuable insights into factors influencing car fuel efficiency.
