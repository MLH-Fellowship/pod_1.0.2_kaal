from flask import Flask
from flask import jsonify
from flask import request
from firebase_upload import upload, get_user
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"status": "The API is healthy and working properly"})


@app.route('/register/', methods=['POST'])
def register_user():
    input_json = request.get_json(force=True)
    print("USER ID", input_json['user_id'])
    print("ROLES", input_json['roles'])
    userHash = upload(input_json['user_id'], input_json['roles'])
    return jsonify({"statusCode": 200, "userHash": userHash})


@app.route('/<string:userHash>', methods=['GET'])
def get_user_details(userHash):
    print(userHash)
    resp = get_user(userHash)
    return jsonify({'user': resp})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
