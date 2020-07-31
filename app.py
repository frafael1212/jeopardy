import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from models import db_drop_and_create_all, setup_db, Questions
import json


app = Flask(__name__)
setup_db(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

# Decors
@app.route('/')
def jeopardy():
    return 'Hello Jeopardy!'