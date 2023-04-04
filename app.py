
from flask import Flask, Response, request,jsonify
import pymongo
from pymongo import MongoClient
import json
from bson import ObjectId
app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.company
    mongo.server_info() #trigger exception if can't connect to DB...

except:
    print("ERROR - can't connect to db")




#  POST Method :=>
@app.route("/users", methods = ["POST"])
def create_user():
    try:
        user = {
            "name":request.form["name"],
            "lastName":request.form["lastName"]
            }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)

        return Response(
            response=json.dumps(
            {"message":"user created",
             "id":f"{dbResponse.inserted_id}"
             }),
            
        status=200,
        mimetype="application/json"
        )
    except Exception as ex:
        print('******')
        print(ex)
        print('******')





#  GET Method :=>
@app.route('/users', methods=['GET'])
def get_users():
    users = db.users.find()
    output = []
    for user in users:
        output.append({'name': user['name'], 'lastName': user['lastName']})
    return jsonify({'result': output})






#  PUT Method :=>
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = db.users.find_one({'_id': ObjectId(user_id)})
    print(user)
    if user:
        new_name = request.json.get('name')
        new_lastName = request.json.get('lastName')
        db.users.update_one(
            {'_id': user_id},
            {'$set': {'name': new_name, 'lastName': new_lastName}}
        )
        return jsonify({'message': 'User updated successfully.'})
    else:
        return jsonify({'error': 'User not found.'}), 404





#  DELETE Method :=>
@app.route('/delete/<id>', methods=['DELETE'])
def delete_document(id):
    # find the document with the specified id and delete it
    result = db.users.delete_one({'_id': ObjectId(id)})
    
    # check if the document was deleted successfully
    if result.deleted_count == 1:
        return jsonify({'message': 'Document deleted successfully'})
    else:
        return jsonify({'message': 'Document not found'})
    



if __name__ == '__main__':
    app.run(debug=True)



