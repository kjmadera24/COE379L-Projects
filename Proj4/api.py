from flask import Flask, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)

def get_config():
    default_config = {"debug": True}
    try:
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Couldn't load the config file; details: {e}")
    # if we couldn't load the config file, return the default config
    return default_config

#L5 = tf.keras.models.load_model('models/Lenet5.keras')
#AltL5 = tf.keras.models.load_model('models/AltLenet5.keras')
#mNetv2 = tf.keras.models.load_model('models/MobileNet.keras')
#alexNet = tf.keras.models.load_model('models/AlexNet.keras')

def preprocess_input(img):
   """
   Prepares the user-inputted image into a format the model can process.
   """
   processed_image = tf.cast(processed_image, tf.float32)
   processed_image = tf.image.resize(processed_image, image_size, method='nearest')
   processed_image = processed_image / 255
    

@app.route('/help', methods=['GET'])
def get_help():
    help = "\n /help                    Provides a summary of routes and corresponding curl call."
    info1 = "\n /models/lenet5          Provides information about the lenet-5 model."
    info2 = "\n /models/alt_lenet5      Provides information about the alternate lenet-5 model."
    info3 = "\n /models/mobilenetv2     Provides information about the mobile net v2 model."
    info4 = "\n /models/alexnetlike     Provides information about the alexnet-like model."
    
    #process = "\n /models/alt_L5/process   Allows for a user-input to test the model with their own image. \n"
    space = "\n"
    return help + info1 + info2 + info3 + info4 + space

@app.route('/models/lenet5', methods=['GET'])
def L5_info():
   return {
      "version": "v1",
      "name": "Lenet-5",
      "description": "Lenet-5 trained model to classify images of dogs to their respective breeds. \n Had an accuracy score of 22% after 10 epochs!!",
      "number_of_parameters": 5632124
   }

@app.route('/models/alt_lenet5', methods=['GET'])
def altL5_info():
   return {
      "version": "v1",
      "name": "Alt_L5",
      "description": "Alternate Lenet-5 trained model to classify images of dogs to their respective breeds. \n Had an accuracy score of 81% after 10 epochs!!",
      "number_of_parameters": 9740088  
   }
    
@app.route('/models/mobilenetv2', methods=['GET'])
def mNet_info():
   return {
      "version": "v1",
      "name": "MobileNetV2",
      "description": "MobileNetV2 trained model to classify images of dogs to their respective breeds. \n Had an accuracy score of 99% after 10 epochs!!",
      "number_of_parameters": 2411704 
   }

@app.route('/models/alexnetlike', methods=['GET'])
def alexNet_info():
   return {
      "version": "v1",
      "name": "AlexNet-like",
      "description": "AlexNet-like trained model to classify images of dogs to their respective breeds. \n Had an accuracy score of 0.8% after 10 epochs!!",
      "number_of_parameters": 2411704 
   }


# start the development server
if __name__ == '__main__':
    config = get_config()
    if config.get('debug', True):
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run(host='0.0.0.0')
