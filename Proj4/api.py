from flask import Flask, request
import yaml
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

L5 = tf.keras.models.load_model('models/Lenet5.keras')
AltL5 = tf.keras.models.load_model('models/Alt_L5.keras')

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
    info = "\n /models/alt_L5/info      Provides information about the alternate lenet-5 model."
    process = "\n /models/alt_L5/process   Allows for a user-input to test the model with their own image. \n"
    space = "\n"
    return help + info + process + space

@app.route('/models/alt_L5/info', methods=['GET'])
def model_info():
   return {
      "version": "v1",
      "name": "Alt_L5",
      "description": "Classify images of dogs into their respective breeds using the saved Lenet-5 model!!",
      "number_of_parameters": 2601666
   }

@app.route('/models/alt_L5/process', methods=['POST'])
def classify_image():
   im = request.json.get('image')
   if not im:
      return {"error": "The `image` field is required"}, 404
   try:
      data = preprocess_input(im)
   except Exception as e:
      return {"error": f"Could not process the `image` field; details: {e}"}, 404
   return { "result": model.predict(data).tolist()}

@app.route('/models/L5/info', methods=['GET'])
def model_info():
   return {
      "version": "v1",
      "name": "L5",
      "description": "Classify images of dogs into their respective breeds using the saved Alternate Lenet-5 Model!!",
      "number_of_parameters": 2601666
   }

@app.route('/models/L5/process', methods=['POST'])
def classify_image():
   im = request.json.get('image')
   if not im:
      return {"error": "The `image` field is required"}, 404
   try:
      data = preprocess_input(im)
   except Exception as e:
      return {"error": f"Could not process the `image` field; details: {e}"}, 404
   return { "result": model.predict(data).tolist()}


# start the development server
if __name__ == '__main__':
    config = get_config()
    if config.get('debug', True):
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run(host='0.0.0.0')