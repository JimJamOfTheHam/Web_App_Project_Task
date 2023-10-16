from flask import *
import dataset 

app = Flask(__name__)
db = dataset.connect('sqlite:///chatroom.db')
app.secret_key = 'cactus'

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

    elif x == 'crackle' and y == '3':
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
        g.beforethequestion = f"The capital of Russia is"
        g.afterthequestion = f''
        g.question = f'Question'
        g.questionnumber = f'16'

    elif x == 'Moscow' and y == '16':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"The capital of Australia is"
        g.afterthequestion = f''
        g.question = f'Question'
        g.questionnumber = f'17'


    elif x == 'Canberra' and y == '17':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"Mount Everest is in"
        g.afterthequestion = f''
        g.question = f'Question'
        g.questionnumber = f'18'

    elif x == 'Nepal' and y == '19':
        g.answerfeedback = f'Correct'
        g.beforethequestion = f"River Nile is located in"
        g.afterthequestion = f''
        g.question = f'Question'
        g.questionnumber = f'20'

    elif x == 'Egypt' and y == '20':
        g.answerfeedback = f'You Are Welcomed To Try It Again Or Play A Diffrent Game'
        g.beforethequestion = f"Well Done You Have "
        g.afterthequestion = f'All Of The Fill In The Blank'
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

@app.route('/questionfortrue')
def questionsfortrue():
    g.beforethequestion = f"this is were you will write"
    g.afterthequestion = f"To Start The Game Write Start"
    g.question = f'this will tell you want quesiton you are on'
    g.restart = f''
    return render_template('true.html')

@app.post('/answerfortrue')
def get_answerfortrue():
    x = request.form['message']
    y = request.form['question']
    x = x.lower()

    if x == ('start'):
        g.question = f"Question"
        g.questionnumber = f"1"
        g.beforethequestion = f"Do crocodiles cry when they eat food?"

    #elif x == ("true") and y == (""):
        #g.question == f"Question"
        #g.questionnumber == f""
        #g.beforethequestion == f""

    elif x == ("true") and y == ("1"):
        g.question = f"Question"
        g.questionnumber = f"2"
        g.beforethequestion = f"Bats are Blind"
        g.answerfeedback = f"Correct. Fun "

    elif x == ("false") and y == ("2"):
       g.question = "Question"
       g.questionnumber = "3"
       g.beforethequestion = f"An ostrich has an eye larger than its brain"

    elif x == ("true") and y == ("3"):
        g.question = f"Question"
        g.questionnumber = f"4"
        g.beforethequestion = f"There are dolphins in the Amazon River in South America"

    else:
        g.beforethequestion = f"You Have Writen A Answer Wrong, Looks Like You Have To Start Again."

    return render_template('true.html')



#chat 
@app.route("/homepage")
def homepage():
    if 'username' not in session:
        return redirect ('/login')
    return render_template('homepage.html' , posts=db['posts'] )

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/set_picture')
def set_picture():
    return render_template('set_picture.html')

@app.route('/set_picture_post', methods= ['post'])
def set_picture_post():
    file = request.files['file']
    filename_to_save = 'static/uploads/' + file.filename
    file.save (filename_to_save)
    session ['profile_picture_url'] = filename_to_save
    return redirect ('/homepage')

@app.route('/logout')
def logout():
    del session ['username']
    return redirect ('/homepage')

@app.route('/login_post', methods=['post'])
def login_post():
   session['username'] = (request.form['username'])
   return redirect('/homepage')


@app.route('/createpost', methods=['post'])
def createpost():
    post_dictionary = {
        'message' : request.form ['message'],
        'username' :session['username'],
        'picture' : session['profile_picture_url']
    }
    db['posts'].insert(post_dictionary) 

    return redirect('/homepage') 






app.run(debug=True, port=2007)