from db.db import db

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(255), nullable=False)
    userEmail = db.Column(db.String(255), nullable=False)
    saleTotal = db.Column(db.Numeric(10, 2), nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    def __init__(self, userName, userEmail, saleTotal, date):
        self.userName = userName
        self.userEmail = userEmail
        self.saleTotal = saleTotal
        self.date = date

