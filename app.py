
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import shabbos_web_class
import googleapi
import testdown



app = Flask(__name__)
 
@app.route("/")
def index():
    #return name
    

    Candletime = shabbos_web_class.return_candletime_string()
    countdown = shabbos_web_class.time_remaining()
    mover = testdown.countdown(100)


    return render_template(
        'test.html',**locals())
 
if __name__ == "__main__":
    app.run()
