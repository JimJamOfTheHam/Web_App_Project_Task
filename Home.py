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
    x = request.form['message']
    y = request.form['number']
    if y == '1':
        g.beforethequestion = f"Aussie kids are"
        g.afterthequestion = f"kids. "
        if x == 'weetbix':
            g.answerfeedback = f'Correct, Try This One.'
        else:
            g.answerfeedback = f'Incorrect Try Again.'

    elif y=='2':
        print('Yes')

    print ('THIS WORKS', y)

    return render_template('Fill_In_The_Blanks.html')

app.run(debug=True, port=2007)