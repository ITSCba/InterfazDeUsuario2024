from urllib.request import urlopen 
from bs4 import BeautifulSoup


def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read())

miDir = "https://apod.nasa.gov/"

sopa = bajar(miDir)
print(sopa.prettify())
zodape = sopa.find("IMG")
print(zodape)
imDir = zodape.attrs["src"]
print(imDir)
