import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_filename = "jeopardy.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Question
a persistent drink entity, extends the base SQLAlchemy Model
'''
class Questions(db.Model):
    # Attributes
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    question = Column(String(), unique=True)
    answer = Column(Integer().with_variant(Integer, "sqlite"), nullable=False)
    value =  Column(Integer().with_variant(Integer, "sqlite"), nullable=False)

    #Methods
    def insert(self):
        db.session.add(self)
        db.session.commit()
