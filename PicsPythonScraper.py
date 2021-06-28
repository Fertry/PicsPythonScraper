from bs4 import BeautifulSoup
import requests

def imagedown(url, folder, type):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    i = 0
    for image in images:
        #if image.has_attr('data-src'):
        if image.has_attr('src'):
            name = image['alt']
            #link = image['src']
            link = image['src']
            write(link, name, folder, type, i)
            i += 1

        
def write(link, name, folder, type, i):

    print("Link: ", link, ", Name: ", name, ", i:", i)
    try:

        im = requests.get(link)
        with open(folder + name.replace(' ', '-').replace('/', '').replace('|', '') +  str(i) + type, 'wb') as f:
            print("LINK: ", link)
            f.write(im.content)
            print('Writing: ', folder + name.replace(' ', '-').replace('/', '') +  str(i) + type)
        f.close()

    except requests.exceptions.RequestException:

        print("Error trying to reach ", link)
        

def main():

    FOLDER = input("ENTER FOLDER DESTINATION: ")
    
    while True:
        try:
            TYPE = input("ENTER EXTENSION AS JPG OR PNG: ")
            if (TYPE.lower() == "png"):
                TYPE = ".png"
                break
            elif (TYPE.lower() == "jpg" or "jpeg"):
                TYPE = ".jpg"
                break
        except ValueError:
            print("Only JPG o PNG are avalibable")

    while True:
        url = input("ENTER AN URL: ")
        try:
            test = requests.get(url)
            if (test.status_code == 200):
                imagedown(url, FOLDER, TYPE)
            else:
                print("Error trying to reach ", url)
        except requests.exceptions.RequestException:
            print("Request error reaching ", url)

if __name__ == '__main__':
    main()
