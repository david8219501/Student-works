import requests
import random
from bs4 import BeautifulSoup
import urllib.parse

# BeautifulSoup.find
# BeautiimportfulSoup.find_all
# rsplit split
# replace
URL = 'https://en.wikipedia.org/wiki/Special:Random'  # קישור רנדומלי לדף ויקי
URL_IMG = 'https://he.wikipedia.org/wiki/%D7%A7%D7%95%D7%91%D7%A5:Pergamonmuseum_-_Vorderasiatisches_Museum_045.JPG'  # קישור לתמונה ספציפית בויקי
URL_DIR = '/home/mefathim-tech-56/wiki img folder/'  # נתיב
MAX_IMG = 20
MAX_NAME = 20
MAX_LINK = 5


def path_image(url_img, url_dir):
    image_path_url = url_img.rsplit('/', 1)[1]
    path_image_dir = url_dir + image_path_url
    print(path_image_dir)


path_image(URL_IMG, URL_DIR)
#test

def download_img(url_img, dir_url):
    try:
        response = requests.get(url_img)
        if response.status_code == 200:
            with open(dir_url, 'wb') as file:
                file.write(response.content)
    except:
        return

    # download_img(URL_IMG, URL_DIR)


def wiki_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            return html
    except:
        return

    # נותן שמות לתיקיות בהתאם לכותרת העמוד'


def titles_wiki(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title
    if title is not None:
        title_text = titel.string.strip() if title.string else 'untitled'
        print(title_text)
    else:
        return


def random_image(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    num_img = len(img_tags)
    if num_img < MAX_IMG:
        return [img['src'] for img in img_tags]
    else:
        selected_img = random.sample(img_tags, MAX_IMG)  # sample מןנע חזרןת
        return [img['src'] for img in selected_img]


def random_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    link_tags = soup.find_all('a', href=true)
    num_link = len(link_tags)
    if num_link < MAX_LINK:
        return [link['href'] for link in link_tags]
    else:
        selected_link = random.sample(link_tags, MAX_LINK)
    return [link['href'] for link in selected_link]


def mk_dir(path):
    try:
        os.mkdir(path)
    except:
        return


def recursive_wiki_page():
    pass
    #title = titles_wiki(html_content)
    #path_dir = path_image(url_img, url_dir)
    #path_img_dir = 'path_dir' + '/' + 'title'



def main():
    pass


if __name__ == '__main__':
    main()
