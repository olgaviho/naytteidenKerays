from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    naturesites = db.relationship("NatureSite", backref='account', lazy=True)
    reports = db.relationship("Report", backref='account', lazy=True)
    comment = db.relationship("Comment", backref='account', lazy = True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True    
  

    @staticmethod
    def how_many_reports_users_have_created():
        stmt = text("SELECT Account.name, COUNT(Report.id) FROM Account"
                    " LEFT JOIN Report ON Report.account_id = Account.id"
                    " GROUP BY Account.id") 
    
        res=db.engine.execute(stmt)
    
        response = []
        for row in res:
            response.append({"name": row[0], "amount": row[1]})    
        return response                  
