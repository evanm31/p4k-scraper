# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:13:09 2017

@author: Evan
"""
import requests 
from bs4 import BeautifulSoup
import pandas as pd
'''
This function parses the HTML of the page and attempts to gather attributes like
artist name, album, genre, date, and the review text itself, instead inputting a
null value if the requested element is not found on the page. All of the data are
put into a Pandas dataframe and returned for use in the gather function.

VARIABLES
album_link - A string that refers to the album section of a link to a Pitchfork 
review.
e.g. '/reviews/albums/neil-young-promise-of-the-real-visitor/'
'''
def gather_info(album_link):
    page = requests.get("https://pitchfork.com" + album_link) #request URL
    soup = BeautifulSoup(page.content, 'html.parser') #parse with beautifulsoup
    title = str(soup.find('title').string) #album and artist 
    try:
        score = float((soup.find(class_="score").string)) #score
    except AttributeError:
        score = None
    try:
        genre = soup.find(class_="genre-list__link").string #genre
    except AttributeError:
        genre = None
    sents = [element.text for element in soup.find_all('p')] #cleaned text output
    string = " ".join(sents)
    try:
        date = str(soup.find(class_="pub-date").string) #date
    except AttributeError:
        date = None
    #create dataframe with column labels
    d = {'artist': [get_artist(title)], 'album': [get_album(title)], 'score': [score], 'genre': [genre], 'review': [string], 'best': [1 if "Best new" in string else 0], 'date': [date]}
    df = pd.DataFrame(data=d)
    return df
'''
This function starts at Pitchfork's album reviews page and searches through a
requested number of pages from a given start page, adding each album link to the
queue to be scraped by the gather_info function and returning them in a list.

VARIABLES
pages, startPage - Integers that refer to the number of pages to scrape and the
page to start on, respectively, while scraping through Pitchfork's album reviews
page.
. 
'''
def gather_links(pages, startPage):
    pageList = [] #list of album review pages
    linkList = [] #list of album links
    for x in range(startPage,(startPage+pages)): #check the first n pages after the requested one
        pageList.append(requests.get("https://pitchfork.com/reviews/albums/?page=" + str(x))) #add each page to list
    for page in pageList:
        soup = BeautifulSoup(page.content, 'html.parser') #parse its contents
        links = soup.find_all(class_="album-link") #gather its links (in raw html)
        for link in links: #for each link
            linkList.append(link.get('href')) #append only the link itself
    return linkList
'''
This function retreives the artist name from the scraped title string.

VARIABLES
title - A string of a cleaned Pitchfork album review title.
'''
def get_artist(title):
    str = ''
    for character in title: #for each character in title
        #add to string up until ':' 
        if character is not ':':
            str += character
        else:
            break
    return str
'''
This function retreives the album name from the scraped title string.

VARIABLES
title - A string of a cleaned Pitchfork album review title.
'''          
def get_album(title):
    str = ''
    #find ':' and index and start there
    index = title.find(":")
    title = title[index+2:]
    #for each character afterwards, add it until '|'
    for character in title:
        if character is '|':
            break
        else:
            str +=character
    return str[:-14] #return just the title

'''
This function uses the other two to gather the requested number of pages starting
from a given page, then adding them all into a single Pandas dataframe, which
is then exported to a CSV file in the given location of the user's desktop.

VARIABLES
pages, startPages - Integers that refer to the number of pages to scrape and the
page to start on, respectively, while scraping through Pitchfork's album reviews
page.
fileLocation - A string that gives a path in the user's desktop where the data
should be saved. 
e.g. 'C:/Users/Evan/Documents'
fileName - A string that gives the desired name of the .csv file. 
e.g. 'p4kReview'
'''
def gather(pages, startPage, fileLocation, fileName):
    linkList = gather_links(pages, startPage) #gather links
    first = True #special variable for first scrape
    newDF = pd.DataFrame()
    for link in linkList: #for each link
        data = gather_info(link) #gather info
        #if first, newDF becomes the initial dataframe
        if first:
            newDF = data
            first = False
        #otherwise append it
        else:
            newDF = newDF.append(data, ignore_index = True)
    #when scraping complete, export to .csv 
    data.to_csv(path_or_buf = fileLocation + "/" + fileName + ".csv")
    #return true if gather was successful
    return True

    