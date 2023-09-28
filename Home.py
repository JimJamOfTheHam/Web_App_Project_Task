from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#Fill In The Blanks
@app.route('/questionsfill')
def questionsfill():
    g.beforethequestion = f""
    g.afterthequestion = f""
    return render_template('Fill_In_The_Blanks.html')

@app.post('/postanswerfill')
def get_postanswerfill():
    x = request.form['message']
    x = x.lower()
    
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

    elif x == 'redbull':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Well Done You Have Finished The Slogans"
        g.afterthequestion = f'Now Write game 2.'

    elif x =='game 2':
        g.beforethequestion = f'It is what it'

    elif x == 'is':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Whatever floats your'

    elif x == 'boat':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Better late then'
    
    elif x == 'never':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Easier '
        g.afterthequestion = f'then done'

    elif x == 'said':
        g.answerfeedback = f'Correct'
        g.afterthequestion = f'to my ears'

    elif x == 'music':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"That’s what"
        g.afterthequestion = f'said'

    elif x == 'she':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Don’t bit the'
        g.afterthequestion = f'that feeds you'

    elif x == 'hand':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Well Done You Have Finished The Sayings/Phrases"
        g.afterthequestion = f'Now Write game 3.'


    else:
        g.answerfeedback = f"Inncorect Try Again"
        g.beforethequestion = f""
        g.afterthequestion = f""
    
    return render_template('Fill_In_The_Blanks.html')
#True or False
@app.route('/questiontrue')
def questiontrue():
    g.beforethequestion = f'TEST 1234'
    g.afterthequestion = f'1234 TEST'
    return render_template('trueorfalse.html')

@app.post('/postanswertrue')
def get_postanswertrue():
    x = request.form['message']
    if x == 'game 1':
        g.beforethequestion = f'True or False'
        g.afterthequestion = f'False or True'

    else:
        g.beforethequestion = f''
    return render_template('trueorfalse.html')

app.run(debug=True, port=2007)