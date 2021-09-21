import sqlalchemy
from sqlalchemy import Sequence
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey,Date
import config.config as cfg


def create_connection_db():
        """
        create conection with database. Name of database should be in config.py
        :return: engine object
        """
        connectionData=f"mysql+pymysql://root:{cfg.passw}@localhost/"
        engine = sqlalchemy.create_engine(connectionData)
        return engine
def delete_db(engine):
        """
        Delete database. Name of database should be in config.py
        :param engine: engine object
           """
        engine.execute(f"drop DATABASE {cfg.dbName}")

def create_db(engine):
    """
        Create database. Name of database should be in config.py
        :param engine: engine object
        :return:
:
    """
    engine.execute(f"CREATE DATABASE {cfg.dbName}") #create db
    engine.execute(f"USE {cfg.dbName}") # select new db

def create_tables_db(engine):
    """
    Create database tables : artist, character_movie, quote, move.
    :param engine: engine object

    """

    metadata_obj = MetaData()
    artist = Table('artist', metadata_obj,
       Column('id', Integer, Sequence('artist_id_seq'), primary_key=True),
       Column('artist_name', String(50), nullable=False)
    )


    character_movie = Table('character_movie', metadata_obj,
        Column('id', Integer, Sequence('character_move_id_seq'), primary_key=True),
        Column('character_movie_name', String(60), nullable=False),
        Column('sex', String(1), nullable=False),
        Column('artist', Integer, ForeignKey("artist.id")))

    quote = Table('quote', metadata_obj,
        Column('id', Integer, Sequence('quote_id_seq'), primary_key=True),
        Column('quote', String(200), nullable=False),
        Column('tokenized', String(200), nullable=False),
        Column('character_movie', Integer, ForeignKey("character_movie.id")))

    movie = Table('movie', metadata_obj,
        Column('id', Integer, Sequence('movie_id_seq'), primary_key=True),
        Column('name', String(50), nullable=False),
        Column('year', Integer, nullable=False),
        Column('character_movie', Integer, ForeignKey("character_movie.id")))

    metadata_obj.create_all(engine)
print("...database created")

def create_db_and_tables():
    """
    create_connection_db, delete_db, create_db, create_tables_db.
    Name of database should be in config.py
    :return:
    """
    engine = create_connection_db()
    delete_db(engine)
    create_db(engine)
    create_tables_db(engine)

