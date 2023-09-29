from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#Fill In The Blanks
@app.route('/questionsfill')
def questionsfill():
    g.beforethequestion = f"And This Is Were You Write Your Answer --->"
    g.afterthequestion = f"<---- so write game in here to start"
    g.question = f'This Box Will Tell You Want Question You Are On'
    return render_template('Fill_In_The_Blanks.html')

@app.post('/postanswerfill')
def get_postanswerfill():
    x = request.form['message']
    y = request.form['question']
    x = x.lower()


    if x == 'game':
        g.beforethequestion = f'Aussie kids are'
        g.afterthequestion = f'kids.'
        g.question = f'Question'
        g.questionnumber = f'1'

    elif x == 'weetbix' and y == '1':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Just'
        g.afterthequestion = f'It.'
        g.question = f'Question'
        g.questionnumber = f'2'

    elif x == 'do' and y == '2':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Question 3: Snap'
        g.afterthequestion = f'Pop!.'
        g.question = f'Question'
        g.questionnumber = f'3'

    elif x == 'crackel':
        g.answerfeedback = f'Correct'
        g.afterthequestion = f"licken' good !."
        g.question = f'Question'
        g.questionnumber = f'4'

    elif x == 'finger':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Question 4: I’m"
        g.afterthequestion = f'It!.'
        g.question = f'Question'
        g.questionnumber = f'5'

    elif x =='loving':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Question 5:"
        g.afterthequestion = f'Gives You Wings'
        g.question = f'Question'
        g.questionnumber = f'6'

    elif x == 'redbull':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Well Done You Have Finished The Slogans"
        g.afterthequestion = f'Now Write game 2.'
        g.question = f'Question'
        g.questionnumber = f'7'

    elif x =='game 2':
        g.beforethequestion = f'It is what it'
        g.question = f'Question'
        g.questionnumber = f'1'

    elif x == 'is':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Whatever floats your'
        g.question = f'Question'
        g.questionnumber = f'2'

    elif x == 'boat':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Better late then'
        g.question = f'Question'
        g.questionnumber = f'3'
    
    elif x == 'never':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Easier '
        g.afterthequestion = f'then done'
        g.question = f'Question'
        g.questionnumber = f'4'

    elif x == 'said':
        g.answerfeedback = f'Correct'
        g.afterthequestion = f'to my ears'
        g.question = f'Question'
        g.questionnumber = f'5'

    elif x == 'music':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"That’s what"
        g.afterthequestion = f'said'
        g.question = f'Question'
        g.questionnumber = f'6'

    elif x == 'she':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Don’t bit the'
        g.afterthequestion = f'that feeds you'
        g.question = f'Question'
        g.questionnumber = f'7'

    elif x == 'hand':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Well Done You Have Finished The Sayings/Phrases"
        g.afterthequestion = f'Now Write game 3.'
        g.question = f'Question'
        g.questionnumber = f''


    else:
        g.answerfeedback = f"Wrong"
        g.beforethequestion = f"Because You Have Gotten A Question Wrong"
        g.afterthequestion = f"You Have To Restart The On You Were On"
        g.question = f'You Got A Question Wrong'
        g.questionnumber = f'Oh No'
    
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
    x = x.lower()
    if x == 'game 1':
        g.beforethequestion = f'True or False'
        g.afterthequestion = f'False or True'

    else:
        g.beforethequestion = f''
    return render_template('trueorfalse.html')

#chat 


app.run(debug=True, port=2007)