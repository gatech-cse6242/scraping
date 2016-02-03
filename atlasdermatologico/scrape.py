import urllib
from bs4 import BeautifulSoup
from time import sleep
from os import mkdir

if __name__ == '__main__': 

    root_url = 'www.atlasdermatologico.com.br/'
    dest_dir = '../images/'

    disease_extension = 'disease.jsf?diseaseId='

    image_counter = 1
    n_diseases = 502

    for i in range(1, n_diseases):

        protocol = 'http://'
        disease_url = protocol + root_url + disease_extension + str(i)
        page_contents = urllib.urlopen(disease_url).read()
        soup = BeautifulSoup(page_contents, 'html.parser')
        images = soup.find_all('img')
        subdir = None
        for img in images:
            if not subdir:
                try:
                    condition = str(img).split('alt=')[1].split('(')[0].replace('"', '')
                    subdir = condition
                except:
                    subdir = i
                try:
                    mkdir(dest_dir + subdir)
                except:
                    pass

            image_data = urllib.urlretrieve('%s%simg?imageId=%d'%(protocol, root_url, image_counter), '%s%s/%d'%(dest_dir,subdir,image_counter) )

            image_counter = image_counter + 1
            sleep(2)
