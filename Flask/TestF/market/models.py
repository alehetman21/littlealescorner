from market import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    budget = db.Column(db.Float(), nullable=False, default=1000.0)
    items_owned = db.relationship('Item', backref='owned_by', lazy=True)


    @property
    def budget_printer(self):
            if (self.budget).is_integer():
                p_budget = ""
                n_budget = ""
                i = 1

                for number in reversed(str(round(self.budget))):
                    if i == 4:
                        p_budget += '.'
                        i = 1
                    p_budget += number
                    i += 1
                
                for number in reversed(p_budget):
                    n_budget += number
                return n_budget

            else:
                p_budget = ""
                n_budget = ""
                i = 1
                decimals = str(self.budget)[-2:]
                for number in reversed(str(round(self.budget))):
                    if i == 4:
                        p_budget += '.'
                        i = 1
                    p_budget += number
                    i += 1
                
                for number in reversed(p_budget):
                    n_budget += number
                n_budget += f",{decimals}"
                return n_budget


    @property
    def plain_pass(self):
        return self.password
    
    
    @plain_pass.setter
    def plain_pass(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


    def check_password(self, password_input):
        return bcrypt.check_password_hash(self.password, password_input)
    
    def __repr__(self):
        return self.username

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=512), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return self.name