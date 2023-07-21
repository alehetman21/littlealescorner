from market import app, db
from flask import render_template, redirect, url_for
from market.models import Item, User
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


@app.route('/signup', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    if form.errors != {}:
        for error in form.errors.values():
            print(f"There was an error: {error}")
    return render_template('register.html', form=form)