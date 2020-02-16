from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///user_details.db')
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM users")
        return {'users': [i for i in query.cursor.fetchall()]}

class Profession(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM profession;")
        result = {'profession_details': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class UserById(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from users where ID =%d "  %int(id))
        result = {'user': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(Users, '/users')
api.add_resource(Profession, '/profession')
api.add_resource(UserById, '/users/<id>')


if __name__ == '__main__':
     app.run(debug=True)