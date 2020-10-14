import requests as request_lib
from firebase_services import (
    get_user,
    getChannel,
    makeChannel,
    store_activity,
    update,
    updateWebhooks,
    upload,
)
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"status": "The API is healthy and working properly"})


@app.route('/register/', methods=['POST'])
def register_user():
    input_json = request.get_json(force=True)
    userHash = upload(input_json['userId'], input_json['roles'], input_json['userName'])
    return jsonify({"statusCode": 200, "userHash": userHash})


@app.route('/validate/', methods=['POST'])
def get_user_details():
    input_json = request.get_json(force=True)
    resp = get_user(input_json['userHash'])
    if resp == 'User not found':
        return jsonify({'msg': "User does not exist"}), 401
    else:
        return jsonify({'user': resp}), 200


@app.route('/storeactivity/', methods=['GET', 'POST'])
def activity():
    if request.method == 'GET':
        return jsonify({"msg": "This is a POST route"})
    else:
        input_json = request.get_json(force=True)
        ret = store_activity(input_json['userHash'], input_json['activities'])
        if ret == 'working':
            return jsonify({"msg": "Activity stored successfully"}), 200
        else:
            return jsonify({"msg": "Error"}), 400


@app.route('/status/', methods=['GET', 'POST'])
def update_status():
    if request.method == 'GET':
        return jsonify({"msg": "This is a POST route"})
    else:
        input_json = request.get_json(force=True)
        # Update status in database
        user_hash = input_json['userHash']
        user_status = input_json['status']
        ret = update(user_hash, user_status)
        if ret == 'successful':
            notify_on_discord(user_hash, user_status)
            return jsonify({"msg": "Status updated successfully"}), 200
        else:
            return jsonify({"msg": "Error"}), 400


@app.route('/storechannel', methods=['POST'])
def update_web():
    input_json = request.get_json(force=True)
    ret = updateWebhooks(input_json['userHash'], input_json['webhookUrls'])
    if ret is True:
        return jsonify({"msg": "webhooks stored successfully"}), 200
    else:
        return jsonify({"msg": "Error"}), 400


@app.route('/channel/<string:channel_id>', methods=['GET', 'POST'])
def get_channel_details(channel_id):
    if request.method == 'GET':
        ret = getChannel(channel_id)
        if ret != '':
            return jsonify({"channel": ret}), 200
        else:
            return jsonify({"msg": "Error"}), 400
    else:
        input_json = request.get_json(force=True)
        ret = makeChannel(channel_id, input_json['webhook_url'])
        if ret is True:
            return jsonify({"msg": "Channel created successfully"}), 200
        else:
            return jsonify({"msg": "Error"}), 400


def notify_on_discord(user_hash, status):
    user = get_user(user_hash)
    user_channel_urls = user['webhookUrls']
    username = user['userName']
    if status == 'Away':
        message = (
            f'\U0001F534 `{username}` has checked out! '
            'Friendly reminder for everyone to stretch.'
        )
    else:
        message = f'\U0001F7E2 `{username}` has just checked-in, good day `{username}`!'

    for url in user_channel_urls:
        request_lib.post(url, json={'content': message, 'tts': False})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1500, debug=True)
