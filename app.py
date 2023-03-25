from flask import Flask, render_template, request, redirect, url_for
import pymysql
import pickle
app = Flask(__name__,template_folder='./')
app.secret_key = 'super secret key'

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Database connection details
HOST = 'localhost'
USER = 'root'
PASSWORD = 'Srivatsan@03'
DB_NAME = 'flask_login'

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DB_NAME)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username=%s AND password=%s', (username, password))
    user = cursor.fetchone()
    if user:
        return redirect(url_for('success'))
    else:
        error = 'Invalid username or password'
        return render_template('index.html', error=error)

# Success page
@app.route('/success')
def success():
    return render_template('success.html')

# Prediction page
@app.route('/predict', methods=['POST'])
def prediction():
    SepalLengthCm = float(request.form['SepalLengthCm'])
    SepalWidthCm = float(request.form['SepalWidthCm'])
    PetalLengthCm = float(request.form['PetalLengthCm'])
    PetalWidthCm = float(request.form['PetalWidthCm'])

    values = [SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]

    result = model.predict([values])

    if (result==0):
        result = 'Iris-setosa'
    if (result==1):
        result = 'Iris-versicolor'
    if (result==2):
        result = 'Iris-virginica'

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)
