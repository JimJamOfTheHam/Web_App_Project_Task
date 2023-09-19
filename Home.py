from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/postanswer')
def get_postanwer():
    return render_template('Fill_In_The_Blanks.html')
#@app.route('/')
#def index():
    #x = input('Question 1: ')
    #if x == ('Q'):
        #print ('Question')
    #else:
        #print("why not")
    #return render_template('index.html')

app.run(debug=True, port=2007)