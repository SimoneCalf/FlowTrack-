from flask import Flask, render_template, request
from Queries import queries

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    user_found = queries.validate_user(username, password)
    #print(username, password)
    print(user_found)
    return render_template('overwiew.html')

if __name__ == '__main__':
    app.run(debug=True)
