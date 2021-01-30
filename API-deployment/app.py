import json
from predict.prediction import predict
from predict.messages import api_is_alive
from preprocessing.cleaning_data import preprocess
from flask import Flask, request, jsonify, make_response
from preprocessing.json_schema_file import json_schema
import pickle
import os
from db.p1_1_new import p0
from db.p1_3 import p1
from db.p3 import p3
from db.p4 import p4
from flask_cors import CORS
global model
model = pickle.load(open('./model/model.pkl', 'rb'))
app = Flask(__name__)
CORS(app)


def pipeline():
    p0()
    print("----------p0 is completed----------")
    p1()
    print("----------p1 is completed----------")
    p3()
    print("----------p3 is completed----------")
    model = p4()
    print("----------p4 is completed----------")


@app.route('/', methods=['GET'])
def alive():
    return api_is_alive


@app.route('/p0', methods=['GET', 'POST'])
def pipe0():
    if request.method == 'POST':
        json_input = request.get_json(force=True)
        message = "error in p0"
        if json_input["pass"] == 925:
            if json_input["parameter"]:
                p = int(json_input["parameter"])
            else:
                p = "full"
            p0(p)
            print("----------p0 is completed----------")
            message = "p0 is finished"
        else:
            message = "p0 did not start , password is wrong"
        return message
    else:
        return {"pass": "pasword <int>"}


@app.route('/p1', methods=['GET', 'POST'])
def pipe1():
    if request.method == 'POST':
        json_input = request.get_json(force=True)
        message = "error in p1"
        if json_input["pass"] == 925:
            p = int(json_input["parameter"])
            p1(p)
            # print("from "+str(p*1000)+" to " + str((p+1)*1000) +
            #       " records from news table is processed")
            message = "from "+str(p*1000)+" to " + str((p+1)*1000) +\
                " records from news table is processed"
        else:
            message = "p1 did not start , password is wrong"
        return message
    else:
        return {"pass": "pasword <int>", "parameter": "0<int> for first 1000 new ads, 1 for 2. 1000 ads and so..."}


@app.route('/p3', methods=['GET', 'POST'])
def pipe3():
    if request.method == 'POST':
        json_input = request.get_json(force=True)
        message = "error in p3"
        if json_input["pass"] == 925:
            p3()
            print("----------p3 is completed----------")
            message = "p3 is finished"
        else:
            message = "p3 did not start , password is wrong"
        return message
    else:
        return {"pass": "pasword <int>"}


@app.route('/p4', methods=['GET', 'POST'])
def pipe4():
    if request.method == 'POST':
        json_input = request.get_json(force=True)
        message = "error in p4"
        if json_input["pass"] == 925:
            global model
            model = p4()
            print("----------p4 is completed----------")
            message = "p4 is finished"
        else:
            message = "p4 did not start , password is wrong"
        return message
    else:
        return {"pass": "pasword <int>"}


@app.route('/pipeline', methods=['GET', 'POST'])
def pipe():
    if request.method == 'POST':
        json_input = request.get_json(force=True)
        message = "error in pipeline = p1, p3, p4"
        if json_input["pass"] == 925:
            pipeline()
            message = "pipeline is finished"
        else:
            message = "pipeline did not start , password is wrong"
        return message
    else:
        return {"pass": "pasword <int>"}


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


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    port = int(os.environ.get('PORT', 5000))
    # You will also define the host to "0.0.0.0" because localhost will only be reachable from inside de server.
    app.run(host="0.0.0.0", threaded=True, debug=True, port=port)
