#!/usr/bin/env python   
#the above just indicates to use python to interpret this file

import sys                              #a python module with system functions for this OS
import pymongo                          # python MongoDB module
                                    #connect with mongo DB here
from pymongo import MongoClient
client = MongoClient()
                                    #set the database
db = client['moviesDB']
                                    #set the collection
movieCollection = db.movies
print("Movies...")

# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system 
#    standard input file
# ------------------------------------------------------------



# for line in open('C:\grad school\infsci 2725\movies.dat','r'):
for line in open('C:\\grad school\\infsci 2725\\movies.dat','r'):

    
#sys.stdin call 'sys' to read a line from standard input, 
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---Movies---
# movie file format -->MovieID::Title::Genres
#1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy
    
    line = line.strip()                 #strip is a method, ie function, associated with string variable, it will strip the carriage return (by default )               
    movieID,title,genres = line.split("::")  #split line at blanks (by default)
    movieGenres = genres.replace("|",",")
#print('{0}\t{1}\t{2}'.format(movieID, title, movieGenres) ) #the {} is replaced by 0th,1st items in format list
    
#insert data into mongo
    
    movie_record = {"movieId": movieID,"title":title,"genres":[movieGenres]}
    movieCollection.insert_one(movie_record)
    print('{0}\t{1}\t{2}'.format(movieID, title, movieGenres) )



ratingCollection = db.ratings
print("Ratings...")

# ---Ratings---
# ratings file format -->UserID::MovieID::Rating::Timestamp
# 1::122::5::838985046

# for line in open('C:\grad school\infsci 2725\ratings.dat','r'):
for line in open('C:\\grad school\\infsci 2725\\ratings.dat','r'):  
    line = line.strip()                 #strip is a method, ie function, associated with string variable, it will strip the carriage return (by default )               
    userID,movieID,rating,timestamp = line.split("::")  #split line at blanks (by default)
    rating = float(rating)
#insert data into mongo
    
    movie_rating = {"userID": userID,"movieId": movieID,"rating":rating,"timestamp":timestamp}
    ratingCollection.insert_one(movie_rating)
    print('{0}\t{1}\t{2}\t{3}'.format(userID,movieID,rating,timestamp) )


tagCollection = db.tags
print("Tags...")

# ---Tags---
# tags file format -->UserID::MovieID::Tag::Timestamp
# 

for line in open('C:\\grad school\\infsci 2725\\tags.dat','r'):  
    line = line.strip()                 #strip is a method, ie function, associated with string variable, it will strip the carriage return (by default )               
    userID,movieID,tag,timestamp = line.split("::")  #split line at blanks (by default)
 
#insert data into mongo
    
    movie_tag = {"userID": userID,"movieId": movieID,"tag":tag,"timestamp":timestamp}
    tagCollection.insert_one(movie_tag)
    print('{0}\t{1}\t{2}\t{3}'.format(userID,movieID,tag,timestamp) )



# ---Genres---
# genres file format -->MovieID::Title::Genres
genreCollection = db.genres

print("Genres...")

# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system 
#    standard input file
# ------------------------------------------------------------
# for line in open('C:\grad school\infsci 2725\movies.dat','r'):
for line in open('C:\\grad school\\infsci 2725\\movies.dat','r'):

# movie file format -->MovieID::Title::Genres
#1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy
    
    line = line.strip()                 #strip is a method, ie function, associated with string variable, it will strip the carriage return (by default )               
    movieID,title,genres = line.split("::")  #split line at blanks (by default)


# ------------------------------------------------------------
#  this 'while loop' will delimit Genres and insert them
#    with movieID into Genres table
# ------------------------------------------------------------

    i = 0
    j = 0
    while i < len(genres):

        if genres[i] in "|":
            movGenre = genres[j:i]
            genre_record = {"movieId": movieID,"genres":movGenre}
            genreCollection.insert_one(genre_record)
            print('{0}\t{1}'.format(movieID, movGenre) )
            j = i + 1
            i = j
        i = i + 1
    movGenre = genres[j:i]

#insert data into mongo
    
    genre_record = {"movieId": movieID,"genres":movGenre}
    genreCollection.insert_one(genre_record)
    print('{0}\t{1}'.format(movieID, movGenre) )



