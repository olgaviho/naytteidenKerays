from application import db
from application.models import Base

from sqlalchemy.sql import text

class Report(Base):

    __tablename__ = "report"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    naturesite_id = db.Column(db.Integer, db.ForeignKey('nature_site.id'), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description