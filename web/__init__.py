from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)       
migrate = Migrate(app, db) 

from web.books.views import books
app.register_blueprint(books)

from web.authors.views import authors
app.register_blueprint(authors)

from web.searches.views import searches
app.register_blueprint(searches) 