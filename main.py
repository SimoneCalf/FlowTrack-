from flask import Flask, render_template, request, session, redirect, url_for
from Queries import queries

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    user_found = queries.validate_user(username, password)
    if user_found == False:
        return 'Invalid credentials'
    else:
        session['User_id'] = user_found
        print(f"value in session['User_id']: {session['User_id']}")
        return redirect(url_for('overwiew'))
    

@app.route('/overwiew', methods=['GET'])
def overwiew():
    return render_template('overwiew.html')

@app.route('/add_mutation', methods=['POST'])
def add_mutation():
    amount = request.form['amount']
    account = request.form['account']
    date = request.form['date']
    comment = request.form['description']
    category = request.form['category']
    
    print(amount, account, date, comment, category)
    return render_template('overwiew.html')



if __name__ == '__main__':
    app.run(debug=True)
