import os
from app import app
from flask import request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from model.mongodb import mongo
from configuration.config import lot_size
from bson.json_util import dumps, loads

lot_size = int(lot_size)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/park', methods=['POST'])
@limiter.limit("10 per minute")
def park_a_car():
    parking_collection = mongo.db.users
    body = request.get_json()
    data = parking_collection.find({})
    data = list(data)
    if len(data) == 0:
        parkinglot = 1
    else:
        obj = parking_collection.find_one(body)
        if obj is not None and len(data) < lot_size:
            return "{'message': 'Bad Request parameters'}", 400
        elif obj is None and len(data) > lot_size:
            return "{'message': 'Parking Full'}", 400
        else:
            obj = parking_collection.find_one({'carnumber': 'empty'})
            if obj is not None and obj['carnumber'] == 'empty':
                parkinglot = obj['parkinglot']
                parking_collection.update(obj, { "$set": {'parkinglot': obj['parkinglot']}})
                return {'parking_id': parkinglot}, 200
            else:
                if len(data) < lot_size:
                    parkinglot = len(data)+1
                else:
                    return "{'message': 'Parking Full'}", 400 
    body['parkinglot'] = parkinglot
    parking_collection.insert_one(body)
    return {'parking_id': parkinglot}, 200


@app.route('/unpark', methods=['POST'])
@limiter.limit("10 per minute")
def unpark_the_car():
    args = request.get_json()
    print(args)
    parking_collection = mongo.db.users
    data = parking_collection.find_one(args)
    if data is None:
        return "given car number doesn't have any slot allocated", 400
    new_data= { "$set": {'carnumber': 'empty'}}
    parking_collection.update(data, new_data)
    return '', 200

@app.route('/info', methods = ['POST'])
@limiter.limit("10 per minute")
def get_car_slot_info():
    args = request.get_json()
    parking_collection = mongo.db.users
    output = parking_collection.find_one(args)
    return dumps(output), 200
