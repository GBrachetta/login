from flask import Flask, render_template, url_for, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
