from application import db
from application.models import Base



class Author(Base):
    __tablename__ = "author"

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
