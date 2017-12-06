# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:13:09 2017

@author: Evan
"""
import requests 
from bs4 import BeautifulSoup
import pandas as pd

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
    sents = [element.text for element in soup.find_all('p')] #a list of cleaned text output
    string = " ".join(sents)
    d = {'Artist': [get_artist(title)], 'Album': [get_album(title)], 'Score': [score], 'Genre': [genre], 'Review': [string], 'BNM': [1 if "Best new music" in title else 0]}
    df = pd.DataFrame(data=d)
    return df

def gather_links(num):
    pageList = [] #list of album review pages
    linkList = [] #list of album links
    for x in range(1,num+1): #check the first n pages
        pageList.append(requests.get("https://pitchfork.com/reviews/albums/?page=" + str(x))) #add each page to list
    for page in pageList:
        soup = BeautifulSoup(page.content, 'html.parser') #parse its contents
        links = soup.find_all(class_="album-link") #gather its links (in raw html)
        for link in links: #for each link
            linkList.append(link.get('href')) #append only the link itself
    return linkList

def get_artist(title):
    str = ''
    for character in title:
        if character is not ':':
            str += character
        else:
            break
    return str
            
def get_album(title):
    str = ''
    index = title.find(":")
    title = title[index+2:]
    for character in title:
        if character is '|':
            break
        else:
            str +=character
    return str[:-14]

def gather(num):
    linkList = gather_links(num)
    first = True
    newDF = pd.DataFrame()
    for link in linkList:
        data = gather_info(link)
        if first:
            newDF = data
            first = False
        else:
            newDF = newDF.append(data, ignore_index = True)
    return newDF
    