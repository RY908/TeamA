from flask import Flask, request, jsonify
from . import app
import sys
sys.path.append('../')
from database.chatroom import add_chatroom, check_chatroom
from auth import verify

@app.route("/chatrooms/<chatroom_id>", methods=["GET"])
def get_chatroom_users(chatroom_id):
    access_token = request.headers.get("access_token")
    user_id = verify(access_token)
    users = check_chatroom(chatroom_id)
    if users != 4:
        return jsonify({}), 205
    return jsonify({}), 200

@app.route("/chatrooms", methods=["POST"])
def join_chatroom():
    access_token = request.headers.get("access_token")
    given_json = request.json
    tag_name = given_json['tag_name']
    user_id = verify(access_token)
    chatroom_id = add_chatroom(user_id, tag_name)
    return jsonify({ 'chatroom_id': chatroom_id }), 200

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
