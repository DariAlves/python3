from flask import Flask, Response, Request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import pymysql
pymysql.install_as_MySQLdb()
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/mysqlteste'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))


# Mostrar todos usuários
@app.route('/usuarios', methods=['GET'])
def todos_usuarios():
    usuarios = Usuario.query.all()
    print(usuarios)

    return Response()

app.run()