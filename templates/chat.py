from flask import *

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route('/create_post', methods=['post'])
def create_post():
    return "SUCCESS"

app.run(debug=True)