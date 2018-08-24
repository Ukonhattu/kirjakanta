from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    books = db.relationship("Book", backref='account', lazy=True)

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

    def roles(self):
        if self.admin is True:
            return ["ADMIN"]
        else:
            return ["USER"]

    @staticmethod
    def find_users_with_most_read_books():

        stmt = text("SELECT Account.id, Account.name, COUNT(Book.id) as bookcount FROM Account"
                    " LEFT JOIN Book ON Book.account_id = Account.id"
                    " WHERE (Book.read = '1')"
                    " GROUP BY Account.id"
                    " ORDER BY bookcount DESC"
                    " LIMIT 10")
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id":row[0], "name":row[1], "book_count":row[2]})
        return response
