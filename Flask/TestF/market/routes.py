from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm

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
                    plain_pass=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(f"There was an error: {error}", category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', form=form)