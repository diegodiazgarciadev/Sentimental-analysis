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
      
        
       
