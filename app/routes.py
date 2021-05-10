from app import db
from app.Models.planet import Planet
from flask import Blueprint, request, jsonify


solar_system_bp = Blueprint("solar_system", __name__, url_prefix="/planets")

@solar_system_bp.route("", methods=["POST"], strict_slashes=False)
def create_new_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"]
    )
    db.session.add(new_planet)
    db.session.commit()
    return {
        "success": True,
        "message": f"Planet {new_planet.name} successfully created"
    }, 201

@solar_system_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_json())
    return jsonify(planets_response)

def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False
    
@solar_system_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_single_planet(planet_id):
    if not is_int(planet_id):
        return {
            "success": False,
            "message": "Planet id must be an integer"
        }, 404

    planet = Planet.query.get(planet_id)
    if not planet:
        return {
            "success": False,
            "message": f"Planet id_{planet_id} was not found"
        }, 404

    if request.method == "GET":
        return planet.to_json()
    elif request.method == "PUT":
        update_data = request.get_json()
        planet.name = update_data["name"]
        planet.description = update_data["description"]
        db.session.commit()
        return {
            "success": True,
            "message": f"Planet id_{planet_id} successfully updated"
        }, 200
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return {
            "success": True,
            "message": f"Planet {planet.name} successfully deleted"
        }, 200