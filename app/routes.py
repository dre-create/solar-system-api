from flask import Blueprint


solar_system_bp = Blueprint("solar_system", __name__)

@solar_system_bp.route('/planets', methods = ["GET"])

def get_planets():
    my_response = "planets"
    return my_response
    
@solar_system_bp.route('/planet', methods = ["GET"])

def get_planet():
    my_response = "planet"
    return my_response

@solar_system_bp.route('/new_planet', methods = ["POST"])

def get_new_planet():
    my_response = "new planet"
    return my_response