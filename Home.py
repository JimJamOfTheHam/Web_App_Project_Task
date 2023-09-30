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


    if x == 'start':
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

    elif x == 'crackel' and y == '3':
        g.answerfeedback = f'Correct'
        g.afterthequestion = f"licken' good !."
        g.question = f'Question'
        g.questionnumber = f'4'

    elif x == 'finger' and y == '4':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Question 4: I’m"
        g.afterthequestion = f'It!.'
        g.question = f'Question'
        g.questionnumber = f'5'

    elif x =='loving' and y == '5':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Question 5:"
        g.afterthequestion = f'Gives You Wings'
        g.question = f'Question'
        g.questionnumber = f'6'

    elif x == 'redbull' and y == '6':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Well Done You Have Finished The Slogans"
        g.afterthequestion = f'Now Write Start Game 2.'
        g.question = f'Question'
        g.questionnumber = f'7'

    elif x =='start game 2' and y == '7':
        g.beforethequestion = f'It is what it'
        g.question = f'Question'
        g.questionnumber = f'8'

    elif x == 'is' and y == '8':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Whatever floats your'
        g.question = f'Question'
        g.questionnumber = f'9'

    elif x == 'boat' and y == '9':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Better late then'
        g.question = f'Question'
        g.questionnumber = f'10'
    
    elif x == 'never'and y == '10':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Easier '
        g.afterthequestion = f'then done'
        g.question = f'Question'
        g.questionnumber = f'11'

    elif x == 'said' and y == '11':
        g.answerfeedback = f'Correct'
        g.afterthequestion = f'to my ears'
        g.question = f'Question'
        g.questionnumber = f'12'

    elif x == 'music' and y == '12':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"That’s what"
        g.afterthequestion = f'said'
        g.question = f'Question'
        g.questionnumber = f'13'

    elif x == 'she' and y == '13':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f'Don’t bit the'
        g.afterthequestion = f'that feeds you'
        g.question = f'Question'
        g.questionnumber = f'14'

    elif x == 'hand' and y == '14':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Well Done You Have Finished The Sayings/Phrases"
        g.afterthequestion = f'Now Write Start Game 3.'
        g.question = f'Question'
        g.questionnumber = f'15'
    
    elif x == 'start game 3' and y == '15':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f""
        g.afterthequestion = f''
        g.question = f'Question'
        g.questionnumber = f'16'

    elif x == '' and y == '16':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f""
        g.afterthequestion = f''
        g.question = f'Question'
        g.questionnumber = f'17'

    else:
        g.answerfeedback = f"Click The Submit To Continue"
        g.beforethequestion = f"Because You Have Gotten A Question Wrong"
        g.afterthequestion = f"You Have To Restart The On You Were On"
        g.question = f'You Got A Question Wrong'
        g.questionnumber = f'Oh No'
        g.restart = f'start'
    
    return render_template('Fill_In_The_Blanks.html')

#True or False
@app.route('/questiontrue')
def questiontrue():
    g.beforethequestion = f"Write True When Ready"
    g.question = f'This Box Will Tell You Want Question You Are On'
    return render_template('trueorfalse.html')

@app.post('/postanswertrue')
def get_postanswertrue():
    x = request.form['post']
    y = request.form['question']
    x = x.lower()
    if x == 'true':
        g.beforethequestion == f'Does a crocodile cry when it eats food.'

    elif x == 'true':
        g.beforethequestion == f'Yes It Works'

    else:
        g.beforethequestion = f''
    return render_template('trueorfalse.html')

#chat 


app.run(debug=True, port=2007)