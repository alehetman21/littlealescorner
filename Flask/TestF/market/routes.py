from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

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


@app.route('/signup')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)