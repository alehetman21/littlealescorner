from market import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    budget = db.Column(db.Float(), nullable=False, default=1000.0)
    items_owned = db.relationship('Item', backref='owned_by', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=512), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return self.name