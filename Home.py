from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return render_template('Fill_In_The_Blanks.html')

@app.post('/postanswer')
def get_postanwer():
    x = request.form['message']
    print(f' this is {x}')

    if x == 'test':
        g.somevariable = f'test'
    else:
        g.somevariable = f'wrong'
        #g.c = f"this is a test {x}"
    #g.somevariable = (f"this is a test {x}")

    return render_template('Fill_In_The_Blanks.html')
#@app.route('/')
#def index():
    #x = input('Question 1: ')
    #if x == 'Q':
        #print ('Question')
    #else:
        #print("why not")
    #return render_template('index.html')

app.run(debug=True, port=2007)