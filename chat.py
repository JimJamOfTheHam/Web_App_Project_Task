from flask import *
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///chatroom.db')
app.secret_key = 'asdfghjkl'

@app.route("/")
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
    return redirect ('/')

@app.route('/logout')
def logout():
    del session ['username']
    return redirect ('/')

@app.route('/login_post', methods=['post'])
def login_post():
   session['username'] = (request.form['username'])
   return redirect('/')


@app.route('/createpost', methods=['post'])
def createpost():
    post_dictionary = {
        'message' : request.form ['message'],
        'username' :session['username'],
        'picture' : session['profile_picture_url']
    }
    db['posts'].insert(post_dictionary) 

    return redirect('/') 

app.run(debug=True, port=2005)