def test_get_all_planets_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Mars",
        "description": "Red planet"
    },{
        "id": 2,
        "name": "Venus",
        "description": "Large planet"
    }]

def test_get_single_planet_with_records(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "Red planet"
    }

def test_get_single_planet_without_records(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 404
    # assert response_body == {
    #         "success": False,
    #         "message": f"Planet id_1 was not found"
    #     }

def test_create_one_planet(client, planet_data):
    # Act
    response = client.post("/planets", json=planet_data)
    response_body = response.get_json()
    # Assert
    assert response.status_code == 201

