from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from . import app
import sys
sys.path.append('../')
from database.tag import insert_tag, get_tags, delete_tag, exists
from auth import verify

@app.route("/tag", methods=["POST"])
def insert_db_tag():
    access_token = request.headers.get("access_token")
    given_json = request.json
    tag_name = given_json['tag_name']
    user_id = verify(access_token)
    exist_flag = exists(user_id, tag_name)
    if exist_flag == 1:
        return jsonify({}), 400
    insert_tag(user_id, tag_name)
    return jsonify({}), 204

@app.route("/tags", methods=["GET"])
def get_db_tags():
    access_token = request.headers.get("access_token")
    user_id = verify(access_token)
    tags = get_tags(user_id)
    return jsonify({ 'tags': tags }), 200

@app.route("/tag/delete", methods=["POST"])
def delete_db_tag():
    access_token = request.headers.get("access_token")
    given_json = request.json
    tag_name = given_json['tag_name']
    user_id = verify(access_token)
    exist_flag = exists(user_id, tag_name)
    if exist_flag == 0:
        return jsonify({}), 404
    delete_tag(user_id, tag_name)
    return jsonify({}), 204

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
