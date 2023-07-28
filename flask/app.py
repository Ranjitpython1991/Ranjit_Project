

from flask import Flask ,render_template,redirect


app=Flask(__name__)

@app.route('/')
def home():
    return "Home page testing"


@app.route('/index',methods=['GET']) 
def index():
    return "<h1>welcome to index page <h1>"



if __name__ == "__main__" :
    app.run()

    