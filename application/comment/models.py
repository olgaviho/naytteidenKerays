from application import db
from application.models import Base

from sqlalchemy.sql import text

class Comment(Base):

    __tablename__ = "comment"

    text = db.Column(db.String(144), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=True)

    def __init__(self, text):
        self.text = text
    
    def isMyAuthor(self, autid):
        if autid == self.account_id:
            return True
        else:
            return false
