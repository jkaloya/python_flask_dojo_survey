from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  return render_template("index.html")

def countLetters(word):
    count = 0
    for c in word:
        count += 1
    return count

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    if request.form['name'] == '' and request.form['comment'] == '':
        flash('Name cannot be empty', 'nameError')
        flash('Comment cannot be empty', 'commentError')
        return redirect('/')
    if request.form['name'] == '':
        flash('Name cannot be empty', 'nameError')
        return redirect('/')
    if request.form['comment'] == '':
        flash('Comment cannot be empty', 'commentError')
        return redirect('/')
    session['comment'] = request.form['comment']
    comment = countLetters(session['comment'])
    print comment
    if comment > 120:
        flash('Comment must be less then 120 characters', 'commentError')
        return redirect('/')
    session['comment'] = request.form['comment']
    return redirect ('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('user.html')

app.run(debug=True) # run our server
