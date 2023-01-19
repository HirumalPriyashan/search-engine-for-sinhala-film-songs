settings = {
    "settings": {
        "index": {"number_of_shards": 1, "number_of_replicas": 1},
        "analysis": {
            "analyzer": {
                "english_analyzer": {
                    "type": "custom",
                    "tokenizer": "lowercase",
                    "filter": ["edge_n_gram_filter"],
                },
                "sinhala_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["edge_n_gram_filter", "stop_word_filter"],
                },
                "sinhala_analyzer_2": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["edge_n_gram_filter"],
                },
            },
            "filter": {
                "edge_n_gram_filter": {
                    "type": "edge_ngram",
                    "min_gram": "2",
                    "max_gram": "20",
                    "side": "front",
                },
                "stop_word_filter": {
                    "type": "stop",
                    "stopwords_path": "config/analyze/stopwords.txt",
                },
            },
        },
    },
    "mappings": {
        "properties": {
            "artist": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword"}},
                "analyzer": "sinhala_analyzer",
            },
            "artist_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword"}},
                "analyzer": "english_analyzer",
            },
            "directors": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword"}},
                "analyzer": "sinhala_analyzer",
            },
            "directors_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
            "film": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer_2",
            },
            "film_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
            "film_genres": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer",
            },
            "film_genres_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
            "film_no": {"type": "text", "fields": {"keyword": {"type": "integer"}}},
            "lyrics": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer_2",
            },
            "lyrics_by": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer",
            },
            "lyrics_by_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
            "main_actors": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer",
            },
            "main_actors_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
            "main_actresses": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer",
            },
            "main_actresses_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
            "metaphors": {
                "properties": {
                    "domain": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                        "analyzer": "sinhala_analyzer",
                    },
                    "line": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                        "analyzer": "sinhala_analyzer",
                    },
                    "meaning": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                        "analyzer": "sinhala_analyzer",
                    },
                    "source": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                        "analyzer": "sinhala_analyzer",
                    },
                    "target": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                        "analyzer": "sinhala_analyzer",
                    },
                }
            },
            "music_by": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer",
            },
            "music_by_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
            "producers": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer",
            },
            "producers_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
            "release_date": {"type": "date", "format": "yyyy"},
            "title": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "sinhala_analyzer_2",
            },
            "title_english": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                "analyzer": "english_analyzer",
            },
        }
    },
}
