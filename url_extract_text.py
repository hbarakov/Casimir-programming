from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request as ur

def url_save_to_text_file(url, file_name, style):
    """ Scrapes the text content from the given url and saves it as a .txt file (utf-8).
    
    style: str
        whitespace or newline
    url: str
        the url of the website
    file_name: str
        the name of the file
    """
    
    s = ur.urlopen(url)
    html = s.read()
    soup = BeautifulSoup(html, "html5lib")
    data = soup.find_all('article', {'class': 'article'})

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    if style == 'newline':
        text = '\n'.join(chunk for chunk in chunks if chunk)
    if style == 'whitespace':
        text = u' '.join(chunk for chunk in chunks if chunk)

    content='\n'.join('''{}\n{}\n\n{}\n{}'''.format( item.contents[0].find_all('time', {'datetime': '2016-03-16T09:50:30+0100'})[0].text,
                                               item.contents[0].find_all('a', {'class': 'link-grey'})[0].text,
                                               item.contents[0].find_all('img', {'class': 'media-full'})[0],
                                               item.contents[1].find_all('div', {'class': 'article_textwrap'})[0].text,
                                             ) for item in data)

    with open('./{}.txt'.format(file_name), mode='wt', encoding='utf-8') as file:
        file.write(text)
