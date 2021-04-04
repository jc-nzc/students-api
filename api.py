from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

Students = {}

if __name__== "__main__":
  app.run(debug=True)
