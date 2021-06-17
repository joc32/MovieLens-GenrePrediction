from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

if __name__ == '__main__':

    #The flask wrapper just serves as an infinite loop which allows us to get into the container and perform commands without the container stopping.

    app.run(debug=False, host='0.0.0.0', port='4000')