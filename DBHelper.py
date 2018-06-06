# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exists
from dbconfig import conn_data


class DataBase:

    def __init__(self):
        engine = conn_data['ENGINE']
        user = conn_data['USER']
        passwd = conn_data['PASSWORD']
        host = conn_data['HOST']
        database = conn_data['NAME']
        port = conn_data['PORT']

        self.engine = create_engine("{0}://{1}:{2}@{3}/{4}?host={3}?port={5}"
                                    .format(engine, user, passwd, host, database, port),
                                    isolation_level="READ UNCOMMITTED")

    def connect(self):
        self.conn = self.engine.connect()

    def disconnect(self):
        self.conn.close()

    def get_genres(self):
        return self.conn.execute("SELECT * FROM public.\"radioApp_genre\";").fetchall()

    def get_locations(self):
        return self.conn.execute("SELECT * FROM public.\"radioApp_location\";").fetchall()

    def get_areas(self, location_id=None):
        condition = "" if not location_id else " where loc_id={}".format(location_id)
        query = "SELECT * FROM public.\"radioApp_area\"{};".format(condition)
        return self.conn.execute(query).fetchall()

    def get_stations(self, area_id=None, genre_id=None):
        condition = "" if not area_id else "area_id={}".format(area_id)
        condition = condition if not genre_id else "genre_id={}".format(genre_id)
        condition = " where {}".format(condition) if condition else ""
        query = "SELECT * FROM public.\"radioApp_station\"{};".format(condition)
        return self.conn.execute(query).fetchall()
