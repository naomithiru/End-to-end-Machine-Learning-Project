import json
from predict.prediction import predict
from predict.messages import explain_expectations, api_is_alive
from preprocessing.cleaning_data import preprocess
from flask import Flask, request, jsonify, make_response
from preprocessing.json_schema_file import json_schema
import pickle
import os
model = pickle.load(open('./model/model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/', methods=['GET'])
def alive():
    return api_is_alive


@app.route('/predict', methods=['GET', 'POST'])
def predictive():  # The parsed JSON data (application/json, see is_json()).
    if request.method == 'POST':
        json_input = request.get_json(force=True)
        if len(json_input["data"].keys()) > 3:
            json_input = request.get_json(force=True)
            error, message, json_input_cleaned = preprocess(json_input)
            if error:
                response = {"error": f"{message}"}
            else:
                response = {"prediction": f"{predict(model,json_input_cleaned)}",
                            "extra info": message}
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify({"message": "Sorry, you should send minimum 4 mandatory features. You can GET more info by GET method to /predict link"}), 406)
    else:
        json_schema_user = json.dumps(json_schema)
        return json_schema_user


def timer():    
    while true:
        # settimer(function(),86400*7)    
        


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    port = int(os.environ.get('PORT', 5000))
    # You will also define the host to "0.0.0.0" because localhost will only be reachable from inside de server.
    app.run(host="0.0.0.0", threaded=True, port=port)
