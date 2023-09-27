from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questionsfill')
def questionsfill():
    g.beforethequestion = f""
    g.afterthequestion = f""
    return render_template('Fill_In_The_Blanks.html')

@app.post('/postanswerfill')
def get_postanswer():
    x = request.form['message']
    if x == 'game 1':
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
        g.beforethequestion = f"Question 4: I’m"
        g.afterthequestion = f'It!.'

    elif x =='loving':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Question 5:"
        g.afterthequestion = f'Gives You Wings'

    elif x == 'RedBull':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Well Done You Have Finished The Slogans"
        g.afterthequestion = f'Now Write game 2.'

    else:
        g.answerfeedback = f"Inncorect Try Again"
        g.beforethequestion = f""
        g.afterthequestion = f""
    
    return render_template('Fill_In_The_Blanks.html')

@app.route('/questiontrue')
def questiontrue():
    g.beforethequestion = f''
    g.afterthequestion = f''
    return render_template('trueorfalse')

@app.post('/postanswertrue')
def get_postanswer():
    x = request.form['message']
    if x == 'game 1':
        g.beforethequestion = f'True or False'
        g.afterthequestiom = f'False or True'

app.run(debug=True, port=2007)