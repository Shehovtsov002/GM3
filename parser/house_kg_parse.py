import httpx
from parsel import Selector

MAIN_URL = "https://www.house.kg/snyat"
BASE_URL = "https://www.house.kg"


def get_html(url):
    response = httpx.get(url)
    return response.text


def get_houses(count):
    html = get_html(MAIN_URL)
    selector = Selector(html)
    houses_links = selector.css(".left-side a::attr(href)").getall()[:count]
    houses_titles = selector.css(".left-side a::text").getall()[:count]

    titles = [title.strip() for title in houses_titles]
    links = list(map(lambda x: BASE_URL + x, houses_links))

    list_houses = []
    for index in range(0, len(titles)):
        list_houses.append({
            'title': titles[index],
            'link': links[index]
        })

    return list_houses

