from flask import Flask
from flask import jsonify
from DBHelper import DataBase

app = Flask(__name__)
db = DataBase()

@app.route('/genres', methods=['GET'])
def get_genres():
    db.connect()
    genres = map(dict, db.get_genres())
    db.disconnect()

    return jsonify(genres)

@app.route('/locations', methods=['GET'])
def get_locations():
    db.connect()
    locations = map(dict, db.get_locations())
    db.disconnect()
    return jsonify(locations)

@app.route('/areas/<int:loc_id>', methods=['GET'])
def get_areas(loc_id):
    db.connect()
    areas = map(dict, db.get_areas(loc_id))
    db.disconnect()
    return jsonify(areas)

@app.route('/areastations/<int:area_id>', methods=['GET'])
def get_stations_by_area(area_id):
    db.connect()
    stations = map(dict, db.get_stations(area_id=area_id))
    db.disconnect()
    return jsonify(stations)

@app.route('/genrestations/<int:genre_id>', methods=['GET'])
def get_stations_by_genre(genre_id):
    db.connect()
    stations = map(dict, db.get_stations(genre_id=genre_id))
    db.disconnect()
    return jsonify(stations)

if __name__=="__main__":
    app.run(port=5000, debug=True)
