from application import db
from application.models import Base

from sqlalchemy.sql import text

class NatureSite(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    reports = db.relationship("Report", backref='nature_site', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description


    def editing(self):
        return True       


   
