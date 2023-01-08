import scrapy
import re
from mtranslate import translate

import json
from pathlib import Path
from scraper.items import LyricsItem

def translation(to_translate):
    return translate(to_translate, 'si', 'en')

def generate_film_dict():
    path = Path(__file__).parent / '../../films.json'
    with open(path) as file:
        data = json.load(file)

    films_dict = {}
    for f in data:
        films_dict[f['name'].replace(" ", "").lower()] = f

    return films_dict

films = generate_film_dict()

class FilmSongSpider(scrapy.Spider):
    name = 'songs'
    start_urls = ['https://www.sinhalasongbook.com/tag/movie-songs/']

    def parse(self, response, **kwargs):
        songs = response.xpath("//h2[contains(@class, 'entry-title')]/a[contains(@class, 'entry-title-link')]")
        for song in songs:
            lyrics_url = song.xpath('@href').get()
            yield response.follow(lyrics_url, callback=self.parse_song)

        next_page = response.css('li.pagination-next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_song(self, response):
        title = response.xpath("//div[contains(@class, 'site-inner')]//header[contains(@class, 'entry-header')]/h1/text()").extract()[0]
        artist = response.css('span.entry-categories a::text').get()
        lyrics_by = response.css('span.lyrics a::text').get()
        music_by = response.css('span.music a::text').get()
        lyrics_html = response.css('div.entry-content pre::text').extract()
        movie = response.css('span.movies a::text').get().strip()
        film = films.get(movie.replace(" ", "").lower())

        song = LyricsItem()
        song['title'] = re.split('[\–|-]', title)[1].strip()
        song['artist'] = translation(artist)
        song['lyrics_by'] = translation(lyrics_by)
        song['music_by'] = translation(music_by)
        song['lyrics'] = self.extract_lyrics(lyrics_html)

        # add info in english
        song['title_english'] = re.split('[\–|-]', title)[0].strip()
        song['artist_english'] = artist
        song['lyrics_by_english'] = lyrics_by
        song['music_by_english'] = music_by
        song['film_english'] = movie

        if film is not None:
            song['film'] = film['name_sinhala']
            song['film_no'] = film['film_no']
            song['release_date'] = film['release_date']
            song['film_genres'] = list(map(translation, film['genres']))
            song['main_actors'] = list(map(translation, film['main_actor']))
            song['main_actresses'] = list(map(translation, film['main_actress']))
            song['directors'] = list(map(translation, film['directors']))
            song['producers'] = list(map(translation, film['producers']))

            # add info in english
            song['film_genres_english'] = film['genres']
            song['main_actors_english'] = film['main_actor']
            song['main_actresses_english'] = film['main_actress']
            song['directors_english'] = film['directors']
            song['producers_english'] = film['producers']

        yield song

    def extract_lyrics(self, lyrics_html):
        lyrics = ''
        newline = False
        for span in lyrics_html:
            lines = (re.sub("[\da-zA-Z\d0-9\-—\[\]\(\)\}\{\@\_\!\#\+\$\%\^\&\*\<\>\?\|\~\:\∆\/]", "", span)).split('\n')
            for line in lines:
                if not(line.isspace() or line == ""):
                    lyrics += line.strip()
                    newline = True
                elif newline:
                    lyrics += '\\n'
                    newline = False
        return lyrics
