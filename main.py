from flask import Flask, request, url_for
from flask.helpers import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


#To specify the default route and input values.
@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Ebert'})
#To specifiy the route and input value type.
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return 'Welcome! {} to the Home page'.format(name)


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'Hi {name} from {location}'


@app.route('/theform', methods=['GET', 'POST'])
def theform():

    if request.method == 'GET':
        return '''
                    <form method="POST" action="/theform">
                        <input type="text" name="name">
                        <input type="text" name="location">
                        <input type="submit" value="Submit">
                    </form>
                '''
    else:
        name = request.form['name']
        location = request.form['location']
        #print(name, location)
        #return '<p>Hi {} from {}</p>'.format(name, location)
        return redirect(url_for('home', name=name, location=location))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
