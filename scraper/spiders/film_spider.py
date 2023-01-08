import scrapy
from mtranslate import translate

from scraper.items import FilmItem

def translation(to_translate):
    return translate(to_translate, 'si', 'en')

class FilmSpider(scrapy.Spider):
    name = 'films'
    prefix = 'https://www.films.lk/films_year.php?id='
    start_urls = []
    for year in range(1947, 2001):
        start_urls.append(prefix + str(year))

    def parse(self, response, **kwargs):
        films = response.css('div.row div.column2 a')
        urls = set()
        for film in films:
            film_url = film.xpath('@href').get()
            urls.add(film_url)

        urls = list(urls)
        for film_url in urls:
            yield response.follow(film_url, callback=self.parse_movie)

    def parse_movie(self, response):
        name = response.css('div.row div.column2 span b::text').get()
        name_sinhala = response.xpath('''//span[preceding-sibling::span[1][contains(text(), 'SUMMARY')]]/text()''').get()
        film_no = response.xpath('''//span[preceding-sibling::b[1][contains(text(), 'Film No')]]/text()''').get()
        release_date = response.xpath('''//span[preceding-sibling::b[1][contains(text(), 'Released Date')]]/text()''').get()
        genres = response.xpath('''//span[preceding-sibling::b[1][contains(text(), 'Category')]]/text()''').getall()
        main_actor = response.xpath('''//span[contains(@class, 'role2') and preceding-sibling::span[1][contains(@class, 'role') and contains(text(), 'Main Actor')]]/a/text()''').getall()
        main_actress = response.xpath('''//span[contains(@class, 'role2') and preceding-sibling::span[1][contains(@class, 'role') and contains(text(), 'Main Actress')]]/a/text()''').getall()
        directors = response.xpath('''//span[contains(@class, 'role2') and preceding-sibling::span[1][contains(@class, 'role') and contains(text(), 'Director')]]/a/text()''').getall()
        producers = response.xpath('''//span[contains(@class, 'role2') and preceding-sibling::span[1][contains(@class, 'role') and contains(text(), 'Producer')]]/a/text()''').getall()

        film = FilmItem()
        film['name'] = name
        film['name_sinhala'] = name_sinhala
        film['film_no'] = film_no
        film['release_date'] = release_date
        film['genres'] = list(map(translation, genres))
        film['main_actor'] = list(map(translation, main_actor))
        film['main_actress'] = list(map(translation, main_actress))
        film['directors'] = list(map(translation, directors))
        film['producers'] = list(map(translation, producers))

        film['film_genres_english'] = genres
        film['main_actors_english'] = main_actor
        film['main_actresses_english'] = main_actress
        film['directors_english'] = directors
        film['producers_english'] = producers


        yield film
