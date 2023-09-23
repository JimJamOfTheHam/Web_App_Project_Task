from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():
    g.beforethequestion = f"Question 1. Aussie kids are"
    g.afterthequestion = f"kids. "
    return render_template('Fill_In_The_Blanks.html')

@app.post('/postanswer')
def get_postanwer():
    x = request.form['message']
    y = request.form['number']
    if y == '0':
        g.beforethequestion = f'Question 1. Aussie kids are'
        g.afterthequestion = f'kids.'
        
    elif y == '1':
        g.beforethequestion = f'Question 2: Just'
        g.afterthequestion = f'It.'
        if x == "Do":
            g.beforethequestion = f'Question 3: Snap'
            g.afterthequestion = f'Pop.'

    else:
        g.answerfeedback = f"You Haven't Filled In The Question Or You Haven't Filled In The Question Numer."
        g.beforethequestion = f"Question 1. Aussie kids are"
        g.afterthequestion = f"kids. "
    
    return render_template('Fill_In_The_Blanks.html')

app.run(debug=True, port=2007)