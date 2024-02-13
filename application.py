from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    
    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"
    
    
    
@app.route('/')
def index():
    return 'hello world!'

@app.route('/books')
def get_books():
    books = book.query.all()
    
    output = []
    for book in books:
        book_data = {'book_name': book.name, 'author':book.author , 'publisher': book.publisger}
        output.append(book_data)
    return {'books': output}

@app.route('/books/<id>')
def get_book(id):
    book = book.query.get_or_404(id)
    return {"book_name":book.book_name , "author":book.author ,"publisher":book.publisher}

@app.route('/books' , methods=['post'])
def add_book():
    book=book(book_name=request.json['book_name'],author=request.json['author'],publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}