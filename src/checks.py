import config.config as conf

engine = conf.connect_db()

def check_artist(artist):
    """
    check if the artist exist on DB
    :param artist: artist name
    :return: id artist if check is OK, -1 is check is not OK
    """
    cursor = engine.execute(f"SELECT id FROM artist WHERE artist_name = '{artist}'")
    try:
        id_artist = list(cursor)[0][0]
    except Exception as err:
        return -1
    return id_artist

def check_character(character_movie, sex, artist_id):
    """
     Check if the character_movie exist on DB
    :param character_movie: character of the movie
    :param sex: sex of the character (F,M)
    :return: id character_movie if check is OK, -1 is check is not OK
    """
    cursor = engine.execute(f"SELECT id FROM character_movie WHERE character_movie_name = '{character_movie}' AND artist = {artist_id} AND sex = '{sex}'")
    try:
        id_character = list(cursor)[0][0]
    except Exception as err:
        return -1
    return id_character

def check_quote(quote, id_character):
    """
    Check if the character_movie exist on DB
    :param quote: string quote to check
    :param id_character: charcter id
    :return: id quote if check is OK, -1 is check is not OK
    """
    print(id_character)
    cursor = engine.execute(
        f"SELECT id FROM quote WHERE character_movie = {id_character} AND quote = '{quote}'")
    try:
        id_quote = list(cursor)[0][0]
    except Exception as err:
        return -1
    return id_quote


def check_movie(movie, year, id_character):
    """
    Check if the movie exist on DB
    :param movie: movie name
    :param year: year of th emovie
    :param id_character: character id
    :return: id quote if check is OK, -1 is check is not OK
    """
    cursor = engine.execute(
        f"SELECT id FROM movie WHERE name = '{movie}' AND year = {year} AND character_movie ={id_character}")
    try:
        id_movie = list(cursor)[0][0]
    except Exception as err:
        return -1
    return id_movie
