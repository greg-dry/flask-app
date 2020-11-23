from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello'

@app.route('/home')
def home_page():
    return str(random.randint(1,10))

if __name__=="__main__":
    app.run()
