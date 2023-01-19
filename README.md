# search-engine-for-sinhala-film-songs

This search engine is designed to help users find metaphors in Sinhala old movie songs. It is built using Elasticsearch as the search engine, Flask as the backend, and Gatsby as the frontend.

The songs and film details used in the search engine have been collected from the following sources:

- Songs: https://www.sinhalasongbook.com
- Film details: https://www.films.lk

## Features

### Custom Stop Words and Stemmer Analysers

To improve the search results, the engine uses custom stop words and stemmer analysers specific to Sinhala language. These are used to remove common words and to reduce words to their root form to improve search accuracy.

### Tokenization and Boosting
The engine uses tokenization to break down the queries into individual words and phrases, which are then indexed for searching. Additionally, the engine employs boosting to give priority to certain terms, such as artist, lyricist, genre, metaphor and song titles, to further improve search results.

### Multi Query and Range Query
Users can search for multiple terms at once using the Multi Query feature. The engine also allows for range queries, so users can search for songs within a specific time period or by a specific artist.

## Structure of the Data

Each song contains the following data fields.

1. Title – Both Sinhala and English
2. Artist - Both Sinhala and English
3. Lyricist - Both Sinhala and English
4. Composer - Both Sinhala and English
5. Song lyrics – Sinhala
6. Metaphors - Sinhala
    1. Target
    2. Source
    3. Line
    4. Meaning
    5. Domain
7. Film - Both Sinhala and English
8. Film no- Number
9. Release date- Date
10. Film genre - Both Sinhala and English
11. Main actors - Both Sinhala and English
12. Main actresses - Both Sinhala and English
13. Directors - Both Sinhala and English
14. Produces - Both Sinhala and English

## Usage

1. Clone the repository to your local machine

    ```sh
    git clone https://github.com/HirumalPriyashan/search-engine-for-sinhala-film-songs
    ```

2. Go to the backend directory and add a `config.py` file using `config.example.py` as an example.
3. Use following commands to run flask server.
    ```sh
    cd backend
    pip install flask sinling flask-cors elasticsearch
    export FLASK_APP=app.py
    flask run
    ```

4. Run the Gatsby fronted
    ```
    cd web
    npm install
    gatsby develop
    ```

5. Go to localhost:8000 in your browser to access the search engine.

### Note
Make sure to have elasticsearch installed and running in the background in order for the search engine to work.

Enjoy the search for Sinhala old movie song metaphors.

#### Sample queries
```
ආදරය ගැන උපමා
එච්.ආර්.ජෝතිපාල කිව්ව සිංදු
එච්.ආර්.ජෝතිපාල ආදරය ගැන කිව්ව සිංදු
1970ට පෙර නන්දා මාලනී ගැයූ ගීත
1970ට පසු 1980ට පෙර නන්දා මාලනී ගැයූ ගීත
1970ට පසු 1980ට පෙර එච්.ආර්.ජෝතිපාල  ගැයූ ගීතවල ආදරය ගැන උපමා
```