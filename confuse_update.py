import webbrowser
import random
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

def get_next_target(page):
    start_link = page.find('href')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    if start_link == -1:
        return None, 0
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def open_web(link):
    no = random.randint(0, len(link))
    url = link[no]
    print(link[no])
    get_page(url)
    webbrowser.open_new_tab(url)

def get_page(url):
    webbrowser.open(url,0,True)
    req = urlopen(url).read()
    res = req.decode('utf-8')
    open_web(get_all_links(res))

get_page("https://www.yahoo.com/")

