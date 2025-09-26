from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'Flask App'
    myresult = 20 + 20
    mylist = [1, 2, 3, 4, 5]
    return render_template('index.html', myvalue = myvalue, myresult = myresult, mylist = mylist)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/filters')
def filters():
    some_text = "Este es un texto de ejemplo para demostrar los filtros en Jinja2"
    return render_template('filters.html', some_text = some_text)

@app.route('/redirect')
def redirection():
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)