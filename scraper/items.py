# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LyricsItem(scrapy.Item):
    title = scrapy.Field()
    artist = scrapy.Field()
    lyrics_by = scrapy.Field()
    music_by = scrapy.Field()
    lyrics = scrapy.Field()
    film = scrapy.Field()
    film_no = scrapy.Field()
    release_date = scrapy.Field()
    film_genres = scrapy.Field()
    main_actors = scrapy.Field()
    main_actresses = scrapy.Field()
    producers = scrapy.Field()
    directors = scrapy.Field()

    title_english = scrapy.Field()
    artist_english = scrapy.Field()
    lyrics_by_english = scrapy.Field()
    music_by_english = scrapy.Field()
    film_english = scrapy.Field()
    film_genres_english = scrapy.Field()
    main_actors_english = scrapy.Field()
    main_actresses_english = scrapy.Field()
    producers_english = scrapy.Field()
    directors_english = scrapy.Field()

class FilmItem(scrapy.Item):
    name = scrapy.Field()
    name_sinhala = scrapy.Field()
    film_no = scrapy.Field()
    release_date = scrapy.Field()
    genres = scrapy.Field()
    main_actor = scrapy.Field()
    main_actress = scrapy.Field()
    directors = scrapy.Field()
    producers = scrapy.Field()

    film_genres_english = scrapy.Field()
    main_actors_english = scrapy.Field()
    main_actresses_english = scrapy.Field()
    producers_english = scrapy.Field()
    directors_english = scrapy.Field()
