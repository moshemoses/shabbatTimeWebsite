from flask import request
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
	rover =  request.remote_addr
	return rover
 
if __name__ == "__main__":
    app.run()
