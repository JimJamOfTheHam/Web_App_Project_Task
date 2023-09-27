from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():
    g.beforethequestion = f""
    g.afterthequestion = f""
    return render_template('Fill_In_The_Blanks.html')

@app.post('/postanswer')
def get_postanwer():
    x = request.form['message']
    if x == 'game 1' and 'games 1':
        g.beforethequestion = f'Question 1. Aussie kids are'
        g.afterthequestion = f'kids.'

    elif x == 'weetbix':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Question 2: just'
        g.afterthequestion = f'it.'

    elif x == 'do':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Question 3: Snap'
        g.afterthequestion = f'Pop!.'

    elif x == 'crackel':
        g.answerfeedback = f'Correct'
        g.afterthequestion = f"licken' good !."

    elif x == 'finger':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Question 4: Snap'
        g.afterthequestion = f'Pop!.'


    else:
        g.answerfeedback = f"Inncorect else"
        g.beforethequestion = f""
        g.afterthequestion = f""
    
    return render_template('Fill_In_The_Blanks.html')

app.run(debug=True, port=2007)