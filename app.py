# Import framework
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import json
import psutil
import time
from decimal import Decimal
import pickle
import pandas as pd

# load the model
model = pickle.load(open('rf_model.pkl', 'rb'))

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class predict_model(Resource):
    def post(self):
        json_data = request.get_json()

        dfclone = pd.DataFrame(json_data, index=[0])

        predict_result = model.predict(dfclone)[0]
        
        body = {
            "predict_result": predict_result
        }
        
        response = {
            "statusCode": 200,
            "body": json.dumps(str(body)),
            "headers": {
                "Access-Control-Allow-Origin": "*"
            }
        }
        
        return response

# Create routes
api.add_resource(predict_model, '/predict')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)