from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.email}')"


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']
        message = request.form['msg']

        new_contact = Contact(firstname=firstname,
                lastname=lastname, email=email, message=message)
        
        try:
            db.session.add(new_contact)
            db.session.commit()
            return redirect('/contact')
        except:
            return "<h1>Adding in adding the contact</h1>"
    else:
        return render_template('contact.html')