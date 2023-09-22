from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():
    g.beforethequestion = f"Aussie kids are"
    g.afterthequestion = f"kids. "
    return render_template('Fill_In_The_Blanks.html')

@app.post('/postanswer')
def get_postanwer():
    g.beforethequestion = f"Aussie kids are"
    g.afterthequestion = f"kids. "
    x = request.form['message']
    
    if x == 'weetbix':
        g.answerfeedback = f'Correct, Try This One.'
    else:
        g.answerfeedback = f'Incorrect Try Again.'

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