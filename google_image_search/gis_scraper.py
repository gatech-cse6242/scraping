
from os import mkdir
from time import sleep

from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os

def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)))

def scrape(query, dest_dir='images/'):
    image_type = "image"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.com/search?q=%s&source=lnms&tbm=isch"%query
    header = {'User-Agent': 'Mozilla/5.0'}
    soup = get_soup(url,header)

    images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
    for img in images:
      raw_img = urllib2.urlopen(img).read()
      cntr = len([i for i in os.listdir(dest_dir) if image_type in i]) + 1
      f = open(dest_dir + image_type + "_"+ str(cntr)+".jpg", 'wb')
      f.write(raw_img)
      f.close()
    

if __name__ == '__main__':

    terms = ['acitinic+keratosis', 'acitinic+keratosis+lesion', 'squamous+cell+carcinoma',
            'squamous+cell+carcinoma+lesion', 'basal+cell+carcinoma', 'basal+cell+carcinoma+lesion',
            'melanoma', 'melanoma+lesion', '"non-cancerous"+lesion']
    
    for term in terms:
        print term
        try:
            mkdir(term)
        except:
            pass
        scrape(term, dest_dir=term+'/')
        sleep(2)
