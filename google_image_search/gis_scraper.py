import urllib2
import simplejson
import StringIO
import random
from time import sleep

if __name__ == '__main__':
    fetcher = urllib2.build_opener()
    searchTerm = 'skin+lesion'
    dest_dir = 'images/'
    startIndex = 0

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    headers={'User-Agent':user_agent,} 

    for i in range(100):
        searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(i)
        f = fetcher.open(searchUrl)
        deserialized_output = simplejson.load(f)

        if( deserialized_output and deserialized_output['responseData']):

            for j in range(0,len(deserialized_output['responseData']['results'])):
                imageUrl = deserialized_output['responseData']['results'][j]['unescapedUrl']
                request = urllib2.Request(imageUrl, None, headers)
                fle = StringIO.StringIO(urllib2.urlopen(request).read())
                content_string = fle.read()
                print imageUrl
                output = open(dest_dir+'%d%d.jpg'%(i, j) , 'w')
                output.write(content_string)
                fle.close()
                output.close()

        sleep( 3 )

