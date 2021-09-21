import os
import dotenv
import sqlalchemy as alch

dotenv.load_dotenv()

passw = os.getenv("pass_sql")
dbName = "mydb1"

def connect_db():
    """
    create a connection to database returning the engine object of the connection.
    Name of database should be in config.py
    :return: engine object
    """
    connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine
