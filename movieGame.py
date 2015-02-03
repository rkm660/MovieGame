#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import requests
import json




#test
    

#gets a list of actors in a given 
def getActors(imdbID):
    url = "http://www.imdb.com/title/" +imdbID + "/fullcredits"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    spans = soup.find_all('span', attrs={'class':'itemprop'})
    actors = []
    for span in spans:
        actors.append(span.decode_contents(formatter="html"))
    return actors



#gets the IMDB id from an inputted movie title
def getImdbID(title):
    r = requests.get("http://www.omdbapi.com/?t="+title)
    text = r.text
    j = json.loads(text)
    return j['imdbID']


#gets the IMDB id from an inputted actor
def getActorID(actor):
    url = "http://www.imdb.com/find?q=" + actor.replace(" ","_")
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    raw = soup.find_all('table', attrs={'class':'findList'})[0].find('a')
    for element in raw:
        e = raw['href']

    return(e.split('/',3)[2])



#gets list of productions a given actor is in
def getAssociatedMovies(actorID):
    i = 1
    movies = []
    aID = actorID
    while (i < 4):
        try:
            url = "http://www.imdb.com/filmosearch?explore=genres&role=" + aID + "&ref_=filmo_nxt&mode=advanced&page="+ str(i) +"&title_type=movie&sort=moviemeter,asc"
            content = urllib2.urlopen(url).read()
            soup = BeautifulSoup(content)
            elements = soup.find_all('h3', attrs={'class':'lister-item-header'})
            for e in elements:
                movies.append((e.find('a').text))
        except urllib2.HTTPError, e:
            print e.code
        i = i + 1
    return movies


