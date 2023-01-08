import json
from pathlib import Path

path = Path(__file__).parent / '../data.json'
with open(path) as file:
    data = json.load(file)

i = 0
for entry in data:
    i += 1
    path = Path(__file__).parent / ('../data/song_lyrics_' + str(i) + '.json')
    with open(path, 'w', encoding="utf-8") as file:
        json.dump(entry, file, indent = 4, ensure_ascii=False)
