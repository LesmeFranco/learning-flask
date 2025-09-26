from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Bienvenido a Flask!')
    response.status_code = 202 
    response.headers['content-type'] = 'text/plain'
    return response

@app.route('/handle_url_params')
def handle_params():
    if 'name' in request.args.keys() and 'age' in request.args.keys():
        name = request.args.get('name')
        age = request.args.get('age')
        return f"Hello, {name}. You are {age} years old."
    else:
        return "Please provide both 'name' and 'age' parameters in the URL." , 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
