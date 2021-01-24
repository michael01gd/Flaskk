from flask import Flask
from flask import  request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/users/<user_id>', methods=["GET","POST","PUT","DELETE"])
def parameter(user_id):
    if request.method== "GET":
        return "GET method"
    elif request.method== "POST":
        data=request.form
        return data
        return "POST method"
    elif request.method== "PUT":

        return "PUT method"
    elif request.method== "DELETE":
        return "DELETE method"
    return user_id


app.run()