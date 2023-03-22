from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from sqlalchemy.engine import URL
from datetime import datetime


engine = create_engine('postgresql://postgres:example@172.26.0.1:5432/postgres')
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer(), primary_key=True)
    slug = Column(String(100), nullable=False, unique=True)
    title = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    content = Column(Text)
    author_id = Column(Integer(), ForeignKey('authors.id'))

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(255), nullable=False)
    joined = Column(DateTime(), default=datetime.now)

    articles = relationship('Article', backref='author')



Session = sessionmaker(bind=engine)
session = Session()


ezz = Author(
    firstname="Ezzeddin",
    lastname="Abdullah",
    email="ezz_email@gmail.com"
)

ahmed = Author(
    firstname="Ahmed",
    lastname="Mohammed",
    email="ahmed_email@gmail.com"
)

article1 = Article(
    slug="clean-python",
    title="How to Write Clean Python",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    author=ezz
    )

article2 = Article(
    slug="postgresql-system-catalogs-metadata",
    title="How to Get Metadata from PostgreSQL System Catalogs",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    created_on = datetime(2022, 8, 29),
    author=ezz
    )

article3 = Article(
    slug="sqlalchemy-postgres",
    title="Interacting with Databases using SQLAlchemy with PostgreSQL",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    author=ahmed
    )

session.add(article1)
session.add(article2)
session.add(article3)

session.flush()

session.add_all([ezz, ahmed])

session.commit()


articles = session.query(Article).all()
for article in articles:
    print(article.title) 