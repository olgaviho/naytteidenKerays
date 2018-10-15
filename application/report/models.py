from application import db
from application.models import Base

from sqlalchemy.sql import text

class Report(Base):

    __tablename__ = "report"

    title = db.Column(db.String(144), nullable=True)
    description = db.Column(db.String(144), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    naturesite_id = db.Column(db.Integer, db.ForeignKey('nature_site.id'), nullable=False)

    comments = db.relationship("Comment", backref='report', lazy = True)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @staticmethod
    def allreports():
        stmt = text("SELECT Report.title, Account.name, Report.description, Nature_site.name, COUNT(Comment.id) FROM Report"
                    " LEFT JOIN Account ON Report.account_id = Account.id"
                    " LEFT JOIN Nature_site ON Report.naturesite_id = Nature_site.id") 
    
        res=db.engine.execute(stmt)
    
        response = []
        for row in res:
            response.append({"title": row[0], "author": row[1], "description": row[2], "naturesite": row[3]})    
        return response     
