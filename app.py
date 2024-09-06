from flask import Flask
from flask_restful import Api
from models import db
from routes import initialize_routes

app = Flask(__name__)

# Config for SQLAlchemy DB (using SQLite for simplicity)
app.config["SQLALCHEMY_DATABASE_URI"] = "./data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize API and DB
api = Api(app)
db.init_app(app)

# Initialize Routes
initialize_routes(api)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
