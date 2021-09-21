from textblob import TextBlob
import re
import spacy


def tokenizer(txt):
    """
    Do the tokenized of a text
    :param txt: text to tokenized
    :return: text tokenized
    """
    nlp = spacy.load("en_core_web_sm")
    tokens = nlp(txt)
    filtradas = []
    for word in tokens:
        if not word.is_stop:
            lemma = word.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma):
                filtradas.append(lemma)

    return " ".join(filtradas)

def sentiment(string):
    """
    Analysis Sentiment analysis
    :param string: text to evaluate
    :return: value of the Sentiment analysis [-1,1]
    """
    blob = TextBlob(string)
    sent = blob.sentiment
    pol = blob.sentiment[0]
    return pol

def format(string):
    """
    replacing " and '
    :param string: text to format
    :return: text formated
    """
    string = string.replace("'", "´")
    string = string.replace('"', '')
    pat = "\[.+\]"
    string = re.sub(pat, "", string)
    return string
def sentiment_df(df_quotes):
    """
    adding a new column (sentiment) to the datarame parameter with the column quote sentimental anaylized
    :param df_quotes: data frame with a string column named quote
    :return: dataframe with 2 columns, quote, and sentiment which is the sentimental analysis of quote column
    """
    df_quotes["sentiment"] = df_quotes.tokenized.apply(sentiment)
    return df_quotes[["quote","sentiment"]]

def getsentimentalanalysis(string):
    """
     Return Any string wrote in english will be evaulate y return the sentimental analsys of that string. Value between [-1,1]
    :param string: string with the quote to evaluate
    :return: Sentimental analsysis value [-1,1]

    """
    string = format(string)
    tokenized = tokenizer(string)
    return sentiment(tokenized)

def replace_df(df):
    df.quote = df.quote.str.replace("'", "´")
    df.quote = df.quote.str.replace('"', '')

    df.artist = df.artist.str.replace("'", "´")
    df.character = df.character.str.replace("'", "´")
    df.movie = df.movie.str.replace("'", "´")
    return df


def create_json_movie(artist, character_move, quote, movie, year, sex):
    myobj_json = {
        "artist": artist,
        "character": character_move,
        "quote": quote,
        "movie": movie,
        "year": year,
        "sex": sex

    }
    return myobj_json