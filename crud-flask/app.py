from flask import Flask, Response, Request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import pymysql
pymysql.install_as_MySQLdb()
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@172.17.0.2:3306/mysqlteste'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
