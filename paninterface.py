from flask import Flask, jsonify, abort, request
from random import randrange
app=Flask(__name__)

#we shall be using a volatile PAN DB as list containing dictionary items as PAN
pans_db=[
    {
        'pan':'ATYPR3434L',
        'name':'ABC kumar',
        'dob':'09-09-2020',
        'mobile':'898989',
        'email':'abc@gmail.com'
    },
    {
        'pan':'LIMCA9999K',
        'name':'XYZ Smith',
        'dob':'01-01-1990',
        'mobile':'8989898989',
        'email':'abc@yahoo.com'
    }

]


#welcome page
@app.route('/')   
def index():
    return "welcome to PAN Interface API"

#Model URI to get info about ALL  PANs
@app.route('/pans',methods=['GET'])
def get_all_pan():
    return jsonify({'pans':pans_db})

#Model URI to get info about a particular PAN
@app.route('/pans/<string:searched_pan>',methods=['GET'])
def get_pan(searched_pan):
    pan = [pan for pan in pans_db if pan['pan'] == searched_pan]
    if len(pan) == 0:
        abort(404)
    return jsonify({'pan': pan[0]})

#Model URI to create a PAN instance
@app.route('/pans',methods=['POST'])
def create_pan():
    if not request.json or not 'name' in request.json:
        abort(400)
    
    new_pan={
        'pan':randrange(10000,99999999,2),
        'name':request.json['name'],
        'dob':request.json['dob'],
        'mobile':request.json['mobile'],
        'email':request.json['email'],
    }
    pans_db.append(new_pan)
    return jsonify({'new_pan':new_pan}), 201

#Model URI to update a PAN instance
@app.route("/pans/<string:update_pan>", methods=['PUT'])
def update_pan(update_pan):
    pan = [pan for pan in pans_db if pan['pan'] == update_pan]

    pan[0]['name']=request.json.get('name', pan[0]['name'])
    pan[0]['dob']=request.json.get('dob', pan[0]['dob'])
    pan[0]['mobile']=request.json.get('mobile', pan[0]['mobile'])
    pan[0]['email']=request.json.get('email', pan[0]['email'])

    return jsonify({'updated_pan':pan[0]})

#Model URI to delete a PAN instance
@app.route('/pans/<string:delete_pan>', methods=['DELETE'])
def delete_task(delete_pan):
    pan = [pan for pan in pans_db if pan['pan'] == delete_pan]
    if len(pan) == 0:
        abort(404)
    pans_db.remove(pan[0])
    return jsonify({'result': True})


if __name__=='__main__': #it runs the application
    app.run(debug=True)