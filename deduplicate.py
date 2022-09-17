with open('all_genres.txt', 'r', encoding='UTF-8') as infile:
    genres = infile.read().splitlines()
print(len(genres))
print('Science Fiction' in genres)
result = list()
for genre in genres:
    if genre not in result:
        result.append(genre)
print(len(result))
outblock = '\n'.join(result)
with open('genres.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(outblock)