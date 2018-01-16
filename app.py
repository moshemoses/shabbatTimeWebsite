from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import shabbos2_web



app = Flask(__name__)
 
@app.route("/")
def index():
    #return name
     
    Candletime = shabbos2_web.time_stmt()
    countdown = shabbos2_web.timetil()


    return render_template(
        'test.html',**locals())
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=99)
