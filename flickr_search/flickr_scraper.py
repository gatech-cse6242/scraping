from flickrapi import FlickrAPI, shorturl
import urllib
API_KEY= '334cf7234def6ecea68c28886e7926f9'

SECRET = '3afd55d06e53ac92'

flickr = FlickrAPI(API_KEY, SECRET)

if __name__ == '__main__':

    favs = flickr.walk(tags="skin lesion", per_page="1500")
    dest_dir = 'images/'


    for i, photo in enumerate(favs):
            title= photo.get('title')
            ident = photo.get('id')
            local = '%s%s_.jpg'%(dest_dir,title)

            farm = photo.get('farm')
            server = photo.get('server')
            secret = photo.get('secret')
            
            try: 
                prefix = "http://farm" + farm + ".staticflickr.com/"+server+"/"
                suffix = ident + "_"+secret+"_b.jpg"
                
                url = prefix + suffix

                urllib.urlretrieve(url, local)
            except:
                continue
