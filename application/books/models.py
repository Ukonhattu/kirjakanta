from application import db
from application.models import Base
from application.genre.models import Genre
from application.series.models import Series

genreToBook = db.Table('genreToBook',
            db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
            db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
            )
authorToBook = db.Table('authorToBook',
            db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
            db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
            )

class Book(Base):
    """Kirjan tehtävien hallinta"""
    __tablename__ = "book"

    name = db.Column(db.String(144), nullable=False)
    read = db.Column(db.Boolean, nullable=False, default=False)

    genres = db.relationship('Genre', secondary=genreToBook, backref='book')
    authors = db.relationship('Author', secondary=authorToBook, backref='book')

    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.read = False

    def getGenres(self):
        response = []
        for genre in self.genres:
            response.append(genre.name)
        if not response:
            return "Unkown"
        return response

    def getAuthors(self):
        response = []
        for author in self.authors:
            response.append(author.name)
        if not response:
            return "Unkown"
        return response

    def getSeries(self):
        if self.series_id == 0 or self.series_id is None:
            return "None"
        s = Series.query.filter_by(id=self.series_id).first()
        return s.name
