from http.client import responses

from scipy.linalg.interpolative import estimate_spectral_norm

import util
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = float(request.form['bhk'])
        bath = float(request.form['bath'])
    except (KeyError, ValueError):
        return jsonify({"error": "Please provide valid inputs for total_sqft, location, bhk, and bath"}), 400

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({"estimated_price": estimated_price})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





if __name__ == '__main__':
   print("Starting Python Flask server for House Price Prediction")
   app.run()