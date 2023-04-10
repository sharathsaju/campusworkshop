"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqtcou9tun42u4rgdg-a.oregon-postgres.render.com",
        database="todo_clxr",
        user="root",
        password="J27mpGEKwuP4OMH7xxy9SjH37eGaGQPi")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
