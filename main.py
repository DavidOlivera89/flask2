from flask import Flask, request, jsonify, make_response, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
import jwt
from datetime import datetime, timedelta
from functools import wraps
from psycopg2 import connect
from flask_cors import CORS, cross_origin
import json
import numpy as np
from scipy.linalg import inv


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

if __name__ == '__main__':
  app.run(port=5000)
