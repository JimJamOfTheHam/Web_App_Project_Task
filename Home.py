from flask import *

app = Flask(__name__)

@app.route('/', methods=['post'])
def index():
    return render_template('index.html')

#@app.route('/')
#def index():
    #x = input('Question 1: ')
    #if x == ('Q'):
        #print ('Question')
    #else:
        #print("why not")
    #return render_template('index.html')

app.run(debug=True, port=2007)