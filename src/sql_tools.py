import config.config as conf
import src.checks as ch
import src.utils as ut
import pandas as pd


engine = conf.connect_db()


def getallquotessa(br=False):
    """
    Return all quotes on DB with their Sentimental analsysis
    :param br:  br: br =Treu return a df , False , return a Json
    :return: json with all quotes and its Sentimental analsysis

    """
    query = f"""
    SELECT tokenized, quote FROM quote"""
    datos_df = pd.read_sql_query(query, engine)
    datossn_df = ut.sentiment_df(datos_df)
    if br:
        return datossn_df
    else:
        return datossn_df.to_json(orient="records")


def getallquotes(br = False):
    """
    Return  all quotes from our database
    :param br: br =Treu return a df , False , return a Json
    :return:
    """
    query = f"""
    SELECT quote FROM quote"""
    datos = pd.read_sql_query(query, engine)

    if br:
        return datos
    else:
     return datos.to_json(orient="records")


    
def quotesbyartist(artist):
    """
    Return quotes by an artist . User must set the artist name
    :param artist: artist name
    :return: json with the quotes of this artist
    """
    query = f"""
        select quote.quote, artist.artist_name from quote, character_movie, artist where 
        character_movie.id = quote.id and artist.id = character_movie.artist and
        artist_name = '{artist}'
        """
    datos = pd.read_sql_query(query,engine)

    return datos.to_json(orient="records")


def quotesbysex(sex):
    """
    Return all quotes from a specific sex. User must set the sex (M,F)
    :param sex: (M or F)
    :return: json with the quotes by Sex

    """
    query = f"""
        select quote.quote, artist.artist_name, character_movie.sex from quote, character_movie, artist where 
        character_movie.id = quote.id and artist.id = character_movie.artist and
        character_movie.sex = '{sex}'
        """
    datos = pd.read_sql_query(query,engine)

    return datos.to_json(orient="records")



def quotesbysexsa(sex):
    """
    return all quotes by sex with their Sentimental analsysis (M, F, B = Both)
    :param sex: (M, F, B = Both)
    :return: quotes by sex with thier Sentimental analysis
    """
    if sex == "B":
        query = f"""
            select quote.quote, quote.tokenized, artist.artist_name, character_movie.sex from quote, character_movie, artist where 
            character_movie.id = quote.id and artist.id = character_movie.artist 
            """
    else:
        query = f"""
            select quote.quote, quote.tokenized, artist.artist_name, character_movie.sex from quote, character_movie, artist where 
            character_movie.id = quote.id and artist.id = character_movie.artist and
            character_movie.sex = '{sex}'
            """
    datos_df = pd.read_sql_query(query,engine)
    datossn_df = ut.sentiment_df(datos_df)
    result = datos_df[["artist_name","quote","sex"]]
    result["sentiment"] = datossn_df["sentiment"]
    print(result["sentiment"])
    return result.to_json(orient="records")


def insertmovie(name, year, character_movie):
    name = ut.format(name)
    id_movie = ch.check_movie(name, year, character_movie)
    if id_movie >= 0:
        return id_movie, f"Movie {name} already exist"
    else:
        cursor = engine.execute(f"""
        INSERT INTO movie (name, year, character_movie)
        VALUES ('{name}', '{year}', {character_movie});
        """)

        return cursor.lastrowid, "Movie inserted into DB"


def insertartist(artist):
       """
       insert an artist by artist name:
       :return: {"artist": artist, "id": id, "msg": msg}

       """
       artist = ut.format(artist)
       id_artist = ch.check_artist(artist)
       if id_artist>=0:
           return id_artist, f"Artist {artist} already exist"
       else:
        cursor = (engine.execute(f"""
          INSERT INTO artist (artist_name)
          VALUES ('{artist}');
          """))
        return cursor.lastrowid, "Artist inserted into DB"


def deleteartist(artist):
    """
    Delete an artist by artist name
    :param artist: artist to delete
    :return:  {"artist": artist, "id": id, "msg": msg}


    """
    artist = ut.format(artist)
    id_artist = ch.check_artist(artist)
    if id_artist <0:
        return id_artist, f"Artist {artist} doesn't  exist in the DB"
    else:
        cursor = (engine.execute(f"""
        DELETE FROM artist WHERE artist_name = '{artist}';
        """))
        return cursor.lastrowid, "Artist deleted from DB"


def updateartist(artist, artist_new):
    """
     Update an artist by artist name
    :param artist: old artist name
    :param artist_new: new artist name
    :return: "artist": artist, "artist_new": artist_new, "msg": msg}

    """
    artist = ut.format(artist)
    id_artist = ch.check_artist(artist)
    if id_artist <0:
        return id_artist, f"Artist {artist} doesn't  exist in the DB"
    else:
        cursor = (engine.execute(f"""
        UPDATE artist
            SET artist_name = '{artist_new}'
            WHERE artist_name = '{artist}';
        """))
        return cursor.lastrowid, "Artist updated in DB"

def insertcharacter(character_movie, sex, artist):
    character_movie = ut.format(character_movie)
    id_character = ch.check_character(character_movie, sex, artist)
    if id_character >= 0:
        return id_character, f"Character {character_movie} already exist"
    else:
        cursor = (engine.execute(f"""
          INSERT INTO character_movie (character_movie_name, sex, artist)
          VALUES ('{character_movie}','{sex}',  {artist} );
          """))
        return cursor.lastrowid, "Character inserted into DB"

def insertquote(quote, character_movie):
    quote = ut.format(quote)
    id_quote= ch.check_quote(quote, character_movie)
    if id_quote >= 0:
        return id_quote, f"Quote {quote} already exist"
    else:
        tokenized = ut.tokenizer(quote)
        cursor = (engine.execute(f"""
          INSERT INTO quote (quote, tokenized, character_movie)
          VALUES ('{quote}', '{tokenized}',  {character_movie} );
          """))
        return cursor.lastrowid,  "Quote inserted into DB"