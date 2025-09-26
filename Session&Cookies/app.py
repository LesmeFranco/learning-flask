from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates') 
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_data')
def set_data():
    session['name'] = 'Franco'
    session['age'] = '18'
    return render_template('index.html', message='Session data set!')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'age' in session.keys():
        name = session['name']
        age = session['age']
        return render_template('index.html', message=f'Name: {name}, Age: {age}')
    else:
        return render_template('index.html', message='No session data found.')

@app.route('/clear_data')
def clear_data():
    session.clear()
    return render_template('index.html', message='Session data cleared!')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set!'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message=f'Cookie Value: {cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message='Cookie removed!'))
    response.set_cookie('cookie_name', 'cookie_value', expires=0)
    return response

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            flash('Login successful!', 'success')
            return render_template('index.html', message='Login successful!')
        else:
            flash('Invalid credentials!', 'danger')
            return render_template('index.html', message='Invalid credentials!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)