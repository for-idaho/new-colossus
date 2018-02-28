from flask import Flask, request
app = Flask(__name__)

@app.route("/sites/new", methods=['POST'])
def new_site():
    return "todo"