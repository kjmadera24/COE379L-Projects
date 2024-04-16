# Project 3: Hurricane Damage Classification

## Overview

In this project, I aimed to classify satellite images captured after Hurricane Harvey in Texas as either depicting damaged or undamaged areas. The goal is to develop intelligent systems using neural networks to accurately identify damaged properties, thereby facilitating efficient disaster response and damage control efforts. I used this dataset https://github.com/joestubbs/coe379L-sp24/tree/master/datasets/unit03/Project3 .

### Model Architectures

- A dense (i.e., fully connected) ANN
- The Lenet-5 CNN architecture
- Alternate-Lenet-5 CNN based off of https://arxiv.org/pdf/1807.01688.pdf

## Project Structure

The repository consists of the following files and folders:

- **models**: Folder containing the pre-trained neural network model file (`Alt_L5.keras`) for image classification.
- `api.py`: Flask API script for serving predictions using the trained model.
- `Dockerfile`: Configuration file for building the Docker container.
- `KM_Proj3.ipynb`: Jupyter Notebook containing code for data preprocessing, model training, and evaluation.
- `README.md`: This file, providing an overview of the project and instructions for usage.
- `docker-compose.yml`: Docker Compose configuration file for managing multi-container Docker applications.
- `KM_Report3.pdf`: A report summarizing my project and models represented in this project!!.

## Usage

### Docker Usage

1. Install Docker on your system if not already installed.
2. Clone this repository to get all the files necessary ```git clone https://github.com/kjmadera24/COE379L-Projects.git``` 
3. Make sure you are in the 'Proj3' directory and pull the docker image ```docker pull kamimadera24/ml-altl5-api:1.0```
4. To run the docker image you can use one of the 2 menthods:
   - ```docker run -it --rm -p 5000:5000 kamimadera24/ml-altl5-api:1.0``` This requires you to open another window to run curl commands.
   - ```docker-compose up -d``` This allows you to run curl commands in the same window.

- **API Routes**:
- `/help`: Provides a summary of available routes and corresponding curl calls.
- `/models/alt_L5/info`: Returns information about the model, including its version, name, description, and number of parameters.
- `/models/alt_L5/process`: Accepts a user-inputted image and classifies it as damaged or undamaged.
- 
