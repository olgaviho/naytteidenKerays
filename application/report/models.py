from application import db
from application.models import Base

from sqlalchemy.sql import text

class Report(Base):

    __tablename__ = "report"

    title = db.Column(db.String(144), nullable=True)
    description = db.Column(db.String(144), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    naturesite_id = db.Column(db.Integer, db.ForeignKey('nature_site.id'), nullable=True)

    comments = db.relationship("Comment", backref='report', lazy = True)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def isMyAuthor(self, autid):
        if autid == self.account_id:
            return True
        else:
            return False     

    @staticmethod
    def allreports():
        stmt = text("SELECT Report.title, Account.username, Report.description, Nature_site.name, COUNT(comment.id) FROM Report"
                    " LEFT JOIN Account ON Report.account_id = Account.id"
                    " LEFT JOIN Nature_site ON Report.naturesite_id = Nature_site.id"
                    " LEFT JOIN Comment ON Comment.report_id = report.id"
                    " GROUP BY Report.id, Account.username, Nature_site.name"
                    ) 
    
        res=db.engine.execute(stmt)
    
        response = []
        for row in res:
            response.append({"title": row[0], "author": row[1], "description": row[2], "naturesite": row[3], "number": row[4]})    
        return response 

   
