# Sentimental-analysis API 

## Introduction

We are going to do a sentimental analysis of the top 100 quotations in American cinema creating an API which could be used to get that information. This dataset comes from the wikipedia [https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movie_Quotes]


We will do the analysis of each quote checking if there are more positve quotes than negatives or the other way round. Following the same style 
we are going to check if Males quotes are more or less positives against Female quotes.

In this development we are going to create an API which will allow us to :
  * Insert data in DB
  * Get data from DB
      * From code
      * From the browser (Table)
  * Sentimental analysis about some data
      * From code
      * From browser (Table)
      * From browser (Chart)
      
  ## Project structure
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
      main.py
        * Endpoints
      endpoints_test.ipynb
        * Testing each endpoint doing request from a notebook with the explation of every function used.
      documentation.md
        * Endpoints documentation
        
        
        
## Bonus
     As a bonus, in this project I have done some extra things:
      * Create automatically the data base and tables from a function that execute sql alquemy actions.
      * Create a new column for the tokenize sentences so that my endpoint will be respond pretty quick.
      * Send response to the browser as a table, so that the user wil be able to check the info in a very easy way.
      * show the plots from seaborn on the browser
      
## Conclusions
   About the results of the sentimental analysis of my quotes dataset, we can see something similar to a normal distrubution in the total of values of the analysis, values is around 0.
   About the libraries we have used, I really think they are not the best ones. I have checked manually the values of sentences and tried new ones and
   many times the result is not what I was expecting. 
   There are other techniques much better that take into account the positions of the words(tokens) even the puntuation. So my conslusion is I won't use
   these libraries we have used here in a production system.
   
 ## Libraries used 
  * Flask
  * markdown
  * io
  * base64
  * matplotlib
  * seaborn
  * pandas
  * TextBlob
  * re
  * spacy
  * request

  
        
## ENDPOINTS
    
    URL : http://127.0.0.1:5000/
    
#### ["GET"]
    
     /quotes 
      Return  all quotes of our database
      
    /quotesbyartist/<artist>
      Return quotes by an artist . User must set the artist name.
      
    /quotesbysex/<sex> 
      Return all quotes from a specific sex. User must set the sex (M,F)
    
    /sa/quote 
      Any string wrote in english will be evaulate y return the sentimental analsys of that string. Value between [-1,1]
      
    /sa/quotes
      Return all quotes on DB with their Sentimental analsysis
      
    /sa/quotesbysex/<sex>
       return all quotes by sex with their Sentimental analsysis (M, F, B = Both)
       
#### The 4 methods below are only for using with a browser:
        
    /br/quotes
       Return a table on the browswer with all the quotes in DB
       
    /sa/br/quotes
       Return a table on the browswer with all the quotes in DB and their Sentimental analsysis values
       
    /sa/br/quotes_chart 
       Display a sns chart (histogram) with the Sentimental analsysis of all quotes
       
    /sa/br/quotesbysex_chart
       Display a sns chart (histogram) with the Sentimental analsysis of all quotes comparing both sex (using hue)
    
   

#### ["POST"]
    
    /insertartist
      insert an artist by artist name:
        ´´´url = 'http://127.0.0.1:5000/insertartist'
         myobj = {
             "artist": "Diego Diaz"
         }
         x = requests.post(url, data = myobj)```
         
         
    /deleteartist
       Delete an artist by artist name
         ```url = 'http://127.0.0.1:5000/deleteartist'
         myobj = {
             "artist": "Diego Diaz"
         }```
        x = requests.post(url, data = myobj)
        
    /updateartist
       Update an artist by artist name
          ``url = 'http://127.0.0.1:5000/updateartist'
          myobj = {
              "artist": "Clark Gable",
              "artist_new": "Clark Cables"
          }
       	  x = requests.post(url, data = myobj)''
          
    /insertmoviequote
      Insert a quote for a movie: 
         ``myobj = {
             "artist": "Diego Diaz",
             "character": "Rick Blaine",
             "quote":"are you looking at me?,",
             "movie": "Taxi Driver",
             "year": 1981
         }
          x = requests.post(url, data = myobj)''
      
        
       
  




