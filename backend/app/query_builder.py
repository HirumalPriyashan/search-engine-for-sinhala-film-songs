from sinling import SinhalaTokenizer
from sinling import word_splitter
import re

tokenizer = SinhalaTokenizer()
artist_boosters = ["ගේ", "ගෙ", "කියන", "ගායනා", "කිව්ව", "ගැයූ", "ගයපු"]
lyrist_boosters = ["රචනා", "ලිව්ව", "ලියන", "ලියපු", "රචිත"]
actor_boosters = ["රඟ", "රඟන", "සිටි", "ඉන්න"]
music_boosters = ["වාදනය", "සංගීතය", "නාද"]
genre_boosters = ["නාට්ය", "පවුලේ", "වාර්තාමය", "කතාව"]
cat_boosters = ["ගැන", "සම්බන්ධ", "සම්බන්ද"]
film_boosters = ["චිත්‍රපටියේ"]
time_boosters = ["පසු", "දී", "පෙර"]

class QueryBuilder:
    @classmethod
    def get_boosts(self, query):
        tokens = tokenizer.tokenize(query)
        boost_params = []
        boosts = {}
        time_params = []
        # print("Tokens:", tokens)
        for token in tokens:
            splits = word_splitter.split(token)
            # print(token, splits)
            query = query.replace("ගීත", "")
            query = query.replace("සිංදු", "")
            query = query.replace("සිංදුවල", "")
            query = query.replace("උපමා", "")
            query = query.replace("ගීතවල", "")
            query = query.replace("චිත්‍රපටියේ", "")
            if splits["affix"] == "ගේ" or splits["affix"] == "ට":
                query = query.replace(token, splits["base"])

            # artist_boosters
            if (
                token in artist_boosters
                or splits["affix"] in artist_boosters
                or splits["base"] in artist_boosters
            ):
                boost_params.append("artist")
                boosts["artist"] = 2

            # lyrist_boosters
            if (
                token in lyrist_boosters
                or splits["affix"] in lyrist_boosters
                or splits["base"] in lyrist_boosters
            ):
                boost_params.append("lyrics_by")
                boosts["lyrics_by"] = 2

            # music_boosters
            if (
                token in music_boosters
                or splits["affix"] in music_boosters
                or splits["base"] in music_boosters
            ):
                boost_params.append("music_by")
                boosts["music_by"] = 2

            # actor_boosters
            if (
                token in actor_boosters
                or splits["affix"] in actor_boosters
                or splits["base"] in actor_boosters
            ):
                boost_params.append("main_actors")
                boosts["main_actors"] = 2
                boost_params.append("main_actresses")
                boosts["main_actresses"] = 2

            # genre_boosters
            if (
                token in genre_boosters
                or splits["affix"] in genre_boosters
                or splits["base"] in genre_boosters
            ):
                boost_params.append("film_genres")
                boosts["film_genres"] = 2

            # cat_boosters
            if (
                token in cat_boosters
                or splits["affix"] in cat_boosters
                or splits["base"] in cat_boosters
            ):
                boost_params.append("metaphors.domain")
                boost_params.append("metaphors.target")
                boosts["metaphors.domain"] = 2
                boosts["metaphors.target"] = 2

            # film_boosters
            if (
                token in film_boosters
                or splits["affix"] in film_boosters
                or splits["base"] in film_boosters
            ):
                boost_params.append("film")
                boosts["film"] = 2

            # time_boosters
            if (
                token in time_boosters
                or splits["affix"] in time_boosters
                or splits["base"] in time_boosters
            ):
                if token == "පසු":
                    time_params.append("gte")
                if token == "දී":
                    time_params.append("eq")
                if token == "පෙර":
                    time_params.append("lt")
        return (
            list(set(boost_params)),
            self.get_boost(boosts, boost_params),
            query,
            time_params,
        )

    @classmethod
    def get_boost(self, boosts, boost_params):
        _str = []
        for field in boost_params:
            try:
                val = boosts[field]
                _str.append("{0}^{1}".format(field, val))
            except:
                pass
        return _str

    @classmethod
    def build_query(self, query):
        boosts_params, boosts, query, time_params = self.get_boosts(query)
        # print(boosts_params, time_params)
        if len(boosts_params) != 0:
            if len(time_params) != 0:
                return self.time_range_query(query, boosts, time_params)
            else:
                return self.boosting_query(query, boosts)
        else:
            return self.default_query(query)

    @classmethod
    def boosting_query(sef, query, boosts):
        return {"multi_match": {"query": query, "fields": boosts}}

    @classmethod
    def time_range_query(self, query, boosts, time_params):
        # extract years
        years = [int(match.group()) for match in re.finditer(r"19[4-9][0-9]", query, re.MULTILINE)]
        years = list(map(str, sorted(years)))
        date_range = {}
        for param in time_params:
            if param == 'lt':
                date_range[param] = years[-1]
            if param == 'gte':
                date_range[param] = years[0]
            if param == 'eq' and len(years) == 1:
                date_range[param] = years[0]

        return {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": query,
                                "fields": boosts,
                            }
                        }
                    ],
                    "filter": [
                        {
                            "range": {
                                "release_date": date_range
                            }
                        }
                    ],
                }
            }

    @classmethod
    def default_query(self, query):
        return {"multi_match": {"query": query}}


if __name__ == "__main__":
    queries = [
        "ආදරය ගැන උපමා",
        "එච්.ආර්.ජෝතිපාල කිව්ව සිංදු",
        "එච්.ආර්.ජෝතිපාල ආදරය ගැන කිව්ව සිංදු",
        "1970ට පෙර නන්දා මාලනී ගැයූ ගීත",
        "1970ට පසු 1980ට පෙර නන්දා මාලනී ගැයූ ගීත",
        "1970ට පසු 1980ට පෙර එච්.ආර්.ජෝතිපාල  ගැයූ ගීතවල ආදරය ගැන උපමා"
    ]
    qb = QueryBuilder()
    for query in queries:
        print(qb.build_query(query))
