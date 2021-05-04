import pytest
from app import create_app
from app import db
from app.Models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mars = Planet(name="Mars",
                    description="Red planet")
    venus = Planet(name="Venus",
                    description="Large planet")

    db.session.add_all([mars, venus])
    db.session.commit()

@pytest.fixture
def planet_data(app):
    # Arrange
    return {
        "name": "Sun",
        "description": "Very hot"
    }