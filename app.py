from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///user_details.db')
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def __init__(self):
        self.conn = db_connect.connect()
        
    def get(self):
        query = self.conn.execute("SELECT * FROM users")
        return {'users': [i for i in query.cursor.fetchall()]}
    
    def post(self):       
        name = request.form["name"]
        address = request.form["address"]
        dob = request.form["dob"]
        
        values = (name, address, dob)
        query = """INSERT INTO users (NAME, ADDRESS, DOB) VALUES (?,?,?)"""
        self.conn.execute(query, values)
        return ("Inserted Data of {}".format(name))

class Profession(Resource):
    def __init__(self):
        self.conn = db_connect.connect()
    
    def get(self):
        query = self.conn.execute("SELECT * FROM profession;")
        result = {'profession_details': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class UserById(Resource):
    def __init__(self):
        self.conn = db_connect.connect()
    
    def get(self, id):
        query = self.conn.execute("select * from users where ID =? ", (int(id)))
        result = {f'user id {id}': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    def delete(self,id):
        self.conn.execute("DELETE from users where ID =?",(int(id)))
        return ("Deleted the User with ID : {}".format(id))
    

api.add_resource(Users, '/users')
api.add_resource(Profession, '/profession')
api.add_resource(UserById, '/users/<id>')


if __name__ == '__main__':
     app.run(debug=True)