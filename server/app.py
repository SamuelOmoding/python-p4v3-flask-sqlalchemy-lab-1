from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    quake = Earthquake.query.filter_by(id=id).first()
    if not quake:
        return jsonify({"message": f"Earthquake {id} not found."}), 404
    return jsonify({"id": quake.id, "location": quake.location, "magnitude": quake.magnitude, "year": quake.year}), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
