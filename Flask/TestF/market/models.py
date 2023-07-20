from market import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=512), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False)
    price = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return self.name