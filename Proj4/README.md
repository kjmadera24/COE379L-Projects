# Project 4: Dog Breed Classification Project

## Overview

This project focuses on classifying images of different dog breeds using various convolutional neural network (CNN) architectures. The dataset I used consists of 20,580 images, split into ~60/40 training/testing data respectively. The goal is to accurately identify the breed of a dog from its image. You can get the dataset here https://www.tensorflow.org/datasets/catalog/stanford_dogs.

For this project I chose to also compare the CNN models used in lecture to those of a project I found online. This https://github.com/aribiswas/stanford-dogs-classifier?tab=readme-ov-file
github, which I will refer to as the AriClassifier from here on, trained different models on  the same dataset. I also used the AriClassifier to help with my datapreprocessing, their format created the basis for the data that the models used. 

### Model Architectures

- LeNet-5: A classic CNN architecture.
- Alternate LeNet-5: A modified version of LeNet-5 based on the Alternate L5 Reference.

#### These architectures are from the AriClassifier 

- MobileNetV2: A lightweight CNN architecture optimized for mobile devices from the AriClassfifier Reference.
- AlexNet-like: A CNN architecture inspired by AlexNet, designed specifically for this project, from the AriClassfifier Reference.

## Project Structure

The repository consists of the following files and folders:

- **models**: Folder containing the pre-trained neural network model files for image classification.
  - `Lenet5.keras`: saved model after running 10 epochs with a Lenet-5 model.
  - `AltLenet5.keras`: saved model after running 10 epochs with an Alternate Lenet-5 model.
  - `MobileNet.keras`: saved model after running 10 epochs with a MobileNetV2 model.
  - `AlexNet.keras`: saved model after running 10 epochs with a AlexNet-like model.
- `api.py`: Flask API script for providing information about the trained models.
- `Dockerfile`: Configuration file for building the Docker container.
- `KM_Proj4.ipynb`: Jupyter Notebook containing code for data preprocessing and model training.
- `README.md`: This file, providing an overview of the project and instructions for usage.
- `docker-compose.yml`: Docker Compose configuration file for managing multi-container Docker applications.
- `KM_Report4.pdf`: A report summarizing the project, including details about the dataset, model architectures, training process, and evaluation results.

## Usage

### Docker Usage

1. Install Docker on your system if not already installed.
2. Clone this repository: `git clone https://github.com/kjmadera24/COE379L_Projects.git`.
3. Navigate to the project directory: `cd Proj4`.
4. Pull the Docker image: `docker pull kamimadera24/ml-api`.
5. Run the Docker container:
   - If running with a single container: `docker run -it --rm -p 5000:5000 kamimadera24/ml-api`. *You must open another window to call curl commands!!*
   - If using Docker Compose: `docker-compose up -d`. *Docker compose allows the user to call curl in the same window!!*
6. Access the API routes to perform predictions.

### API Routes

To use any of the routes you must 

- `/help`: Provides a summary of available routes and corresponding curl calls.
- `/models/lenet5/`: Provides information for the saved LeNet-5 model.
- `/models/alt_lenet5/`: Provides information for the saved Alternate LeNet-5 model.
- `/models/mobilenetv2/`: Provides information for the saved MobileNetV2 model.
- `/models/alexnetlike/`: Provides information for the saved AlexNet-like model.

### Stopping the Container

To stop the Docker container, use one of the following commands:
- `ctrl-C`, `docker ps`, `docker stop <container ID>` (for single container)
- `docker-compose down` (for Docker Compose)

## Resources
- Dataset: https://www.tensorflow.org/datasets/catalog/stanford_dogs
- AriClassifier: https://github.com/aribiswas/stanford-dogs-classifier?tab=readme-ov-file
- Debugging Reference: https://www.tensorflow.org/datasets/overview
- Alternate L5 Reference:  https://arxiv.org/pdf/1807.01688.pdf
- MobileNetV2 Reference: https://arxiv.org/abs/1801.04381
- AlexNet Reference: https://arxiv.org/abs/1803.01164
