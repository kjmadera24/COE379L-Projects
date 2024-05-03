from flask import Flask, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)

#L5 = tf.keras.models.load_model('models/Lenet5.keras')
#AltL5 = tf.keras.models.load_model('models/AltLenet5.keras')
#mNetv2 = tf.keras.models.load_model('models/MobileNet.keras')
#alexNet = tf.keras.models.load_model('models/AlexNet.keras')

#def preprocess_input(img):
#   """
#   Prepares the user-inputted image into a format the model can process.
#   """
#   processed_image = tf.cast(processed_image, tf.float32)
#   processed_image = tf.image.resize(processed_image, image_size, method='nearest')
#   processed_image = processed_image / 255

@app.route('/help', methods=['GET'])
def get_help():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Help</title>
    </head>
    <body>
        <h1>API Help</h1>
        <ul>
            <li><b>/help:</b> Provides a summary of routes and corresponding curl call.</li>
            <li><b>/models/lenet5:</b> Provides information about the lenet-5 model.</li>
            <li><b>/models/alt_lenet5:</b> Provides information about the alternate lenet-5 model.</li>
            <li><b>/models/mobilenetv2:</b> Provides information about the mobile net v2 model.</li>
            <li><b>/models/alexnetlike:</b> Provides information about the alexnet-like model.</li>
        </ul>
    </body>
    </html>
    """
    return html_content

@app.route('/models/lenet5', methods=['GET'])
def L5_info():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lenet-5 Model</title>
    </head>
    <body>
        <h1>Lenet-5 Model</h1>
        <p>Version: v1</p>
        <p>Name: Lenet-5</p>
        <p>Description: Lenet-5 trained model to classify images of dogs to their respective breeds. <br>Had an accuracy score of 22% after 10 epochs!!</p>
        <p>Number of Parameters: 5632124</p>
    </body>
    </html>
    """
    return html_content

@app.route('/models/alt_lenet5', methods=['GET'])
def altL5_info():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Alternate Lenet-5 Model</title>
    </head>
    <body>
        <h1>Alternate Lenet-5 Model</h1>
        <p>Version: v1</p>
        <p>Name: Alt_L5</p>
        <p>Description: Alternate Lenet-5 trained model to classify images of dogs to their respective breeds. <br>Had an accuracy score of 81% after 10 epochs!!</p>
        <p>Number of Parameters: 9740088</p>
    </body>
    </html>
    """
    return html_content
    
@app.route('/models/mobilenetv2', methods=['GET'])
def mNet_info():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MobileNetV2 Model</title>
    </head>
    <body>
        <h1>MobileNetV2 Model</h1>
        <p>Version: v1</p>
        <p>Name: MobileNetV2</p>
        <p>Description: MobileNetV2 trained model to classify images of dogs to their respective breeds. <br>Had an accuracy score of 99% after 10 epochs!!</p>
        <p>Number of Parameters: 2411704</p>
    </body>
    </html>
    """
    return html_content

@app.route('/models/alexnetlike', methods=['GET'])
def alexNet_info():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AlexNet-like Model</title>
    </head>
    <body>
        <h1>AlexNet-like Model</h1>
        <p>Version: v1</p>
        <p>Name: AlexNet-like</p>
        <p>Description: AlexNet-like trained model to classify images of dogs to their respective breeds. <br>Had an accuracy score of 0.8% after 10 epochs!!</p>
        <p>Number of Parameters: 2411704</p>
    </body>
    </html>
    """
    return html_content

# start the development server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
