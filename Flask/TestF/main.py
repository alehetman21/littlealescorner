from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.app_context().push()
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=512), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False)
    price = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return self.name


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/market')
def market():
    context = {
        'items': Item.query.all()
    }

    return render_template('market.html', context = context)