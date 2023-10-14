from flask import *

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route('/createpost', methods=['post'])
def createpost():
    return "SUCCESS"

app.run(debug=True, port=2005)