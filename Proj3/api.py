from flask import Flask, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)

model = tf.keras.models.load_model('models/Alt_L5.keras')

def preprocess_input(im):
   """
   Prepares the user-inputted image into a format the model can process.
   """
   # convert to a numpy array
   prepd_img = np.array(im)
   # Rescale the image
   prepd_img = d/255
   return prepd_img
    

@app.route('/help', methods=['GET'])
def get_help():
    help = "\n /help                    Provides a summary of routes and corresponding curl call."
    info = "\n /models/alt_L5/info      Provides information about the model."
    process = "\n /models/alt_L5/process   Allows for a user-input to test the model with their own image. \n"
    space = "\n"
    return help + info + process + space

@app.route('/models/alt_L5/info', methods=['GET'])
def model_info():
   return {
      "version": "v1",
      "name": "Alt_L5",
      "description": "Classify images containing damaged or undamaged houses",
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


# start the development server
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')