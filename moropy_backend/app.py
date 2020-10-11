from firebase_services import get_user, store_activity, update, upload
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"status": "The API is healthy and working properly"})


@app.route('/register/', methods=['POST'])
def register_user():
    input_json = request.get_json(force=True)
    print("USER ID", input_json['userId'])
    print("ROLES", input_json['roles'])
    userHash = upload(input_json['userId'], input_json['roles'], input_json['userName'])
    return jsonify({"statusCode": 200, "userHash": userHash})


@app.route('/validate/', methods=['POST'])
def get_user_details():
    input_json = request.get_json(force=True)

    print(input_json['userHash'])
    resp = get_user(input_json['userHash'])
    if resp == 'User not found':
        return jsonify({'msg': "User does not exist"}), 401
    else:
        return jsonify({'user': resp}), 200


@app.route('/storeactivity/', methods=['GET', 'POST'])
def activity():
    if request.method == 'GET':
        print('GET')
        return jsonify({"msg": "This is a POST route"})
    else:
        input_json = request.get_json(force=True)
        print('POST')
        ret = store_activity(input_json['userHash'], input_json['activities'])
        if ret == 'working':
            return jsonify({"msg": "Activity stored successfully"})
        else:
            return jsonify({"msg": "Error"})


@app.route('/status/', methods=['GET', 'POST'])
def update_status():
    if request.method == 'GET':
        print('GET')
        return jsonify({"msg": "This is a POST route"})
    else:
        input_json = request.get_json(force=True)
        ret = update(input_json['userHash'], input_json['status'])
        if ret == 'successful':
            return jsonify({"msg": "Status updated successfully"})
        else:
            return jsonify({"msg": "Error"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1500, debug=True)
