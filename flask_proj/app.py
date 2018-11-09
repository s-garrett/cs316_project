from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
