from flask import Flask


    
app = Flask('abc')
@app.route('/')
def hello_world():
    return 'Hello, World!'