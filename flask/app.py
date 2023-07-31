

from flask import Flask ,render_template,redirect,request,url_for,jsonify


app=Flask(__name__)

@app.route('/')
def home():
    return "Home page testing"


@app.route('/index',methods=['GET']) 
def index():
    return "<h1>welcome to index page <h1>"

@app.route('/success/<score>')
def success(score) :
    return "your are pass and your score is : "+ score

@app.route('/fail/<score>')
def fail(score) :
    return "your are fail and your score is : "+ score


@app.route('/form',methods=["GET","POST"])
def form():
    if request.method== "GET":
        return render_template('form.html')
    else :
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        ave_mark=(maths+science+history)/3
        #return render_template('form.html',score=ave_mark)
        res=" "
        if ave_mark>35:
            res="success"
        else :
            res="fail"
        return redirect(url_for(res,score=ave_mark))
    
@app.route('/api',methods=["GET","POST"])
def api():
    data=request.get_json()
    print(data)
    maths=float(data['maths'])
    science=float(data['science'])
    history=float(data['history'])
    return jsonify('sum :',maths+science+history)
    



if __name__ == "__main__" :
    app.run()

    