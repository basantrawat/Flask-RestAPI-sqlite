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
    
    def post(self):       
        user_id = request.form["id"]
        name = request.form["name"]
        address = request.form["address"]
        dob = request.form["dob"]
        
        conn = db_connect.connect()
    
        query = f"""INSERT INTO users (ID, NAME, ADDRESS, DOB) VALUES ({user_id}, '{name}', '{address}', '{dob}')"""
        conn.execute(query)

        return ("Inserted Data of {}".format(name))

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

    def delete(self,id):
        conn = db_connect.connect()
        conn.execute("DELETE from users where ID =%d "  %int(id))
        return ("Deleted the User with ID : {}".format(id))
    

api.add_resource(Users, '/users')
api.add_resource(Profession, '/profession')
api.add_resource(UserById, '/users/<id>')


if __name__ == '__main__':
     app.run(debug=True)