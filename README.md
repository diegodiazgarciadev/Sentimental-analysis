# Sentimental-analysis

## Introduction

We are going to do a sentimental analysis of all catching quotes in the movie history.

We will do the analysis of each quote checking if there are more positve quotes than negatives or the other way round.

We are going to check if Males quotes are more or less positives against Female quotes.

In this development we are going to create an API which will allow us to :
  * Insert data in DB
  * Get data from DB
      * From code
      * From the browser (Table)
  * Sentimental analysis about some data
      * From code
      * From browser (Table)
      * From browser (Chart)
      
  ## project structure
    We have several directories:
      SRC:
        * checks.py: We create a check funtion for every entity we are creating. We will only check if the entity exist so far, 
        but we have create individually in case we will do more checks in the future
        * db_creation.py : I have create a .py for the creation of the database and for the creation of all the tables in the 
        database. It is not an sql script, I have used SQLAlchemy for that. We use the config.py to get the name of the database, 
        in that way we could change the config file if we would like to create a new DB. I have create even a function to drop the DB
        * sql_tools.py : Here we are doing all sql we are going to neeed in our APIs
        * test.py : This is just some random test I have be doing during the developmen process
        * utils.py : some utils function, as format text or sentimentAnalysis
      CONFIG:
        * config.py: configuration file where we are doing the db connection
      DATA: 
        * movie_quotes.csv : File with the data we will be using
      TEMPLATES: 
        * templates.html we will use to display the plots 
        
    ## ENDPOINTS
    
    /quotes
    /quotesbyartist/<artist>
    /sa/quotes
    /sa/quotesbysex
    /br/quotes', methods=("GET")
    /br/quotessa', methods=("GET")
    /insertartist", methods=["POST"]
    /insertmoviequote", methods=["POST"]
       
  
