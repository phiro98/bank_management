from flask import jsonify

def makeResponse(data, err, status_code):
    response = jsonify({"msg": data, "error": err})
    response.status_code = status_code
    return response
