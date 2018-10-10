from application import db
from application.models import Base

from sqlalchemy.sql import text

class Comment(Base):

    __tablename__ = "comment"

    text = db.Column(db.String(144), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)

    def __init__(self, text):
        self.text = text
