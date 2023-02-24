from flask import Flask, render_template, session,redirect,request
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key="Secret to the golds! "
@app.route("/")
def index():
    if 'gold' and 'activities' not in session:
        session['gold']=0 
        session['activities']=""
    return render_template("index.html",messages=session['activities'])

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/process_money", methods=['POST'])
def process():
    current_time=datetime.now().strftime('%Y/%m/%d %I:%M %p')

    if request.form['building'] == 'farm':
        n=random.randint(10,20)
        session['gold'] += n 
        
    if request.form['building'] == 'cave':
        n=random.randint(5,10)
        session['gold'] += n 
        
    if request.form['building'] == 'house':
        n=random.randint(2,5)
        session['gold'] += n 
        
    if request.form['building'] == 'casino':
        n=random.randint(-50,50)
        session['gold']+= n

    if n<0:
        session['activities'] += (f"<p class='text-danger'>Oh nooo! You lost {-n} golds from the {request.form['building']}! ({current_time})</p>")
    if n>0:
            session['activities'] += (f"<p class='text-success'>Yaayyy! You won {n} golds from the {request.form['building']}! ({current_time})</p>")

    return redirect ('/')
        



if  __name__ == "__main__":
    app.run(debug=True)