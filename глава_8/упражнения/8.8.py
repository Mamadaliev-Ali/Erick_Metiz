def make_album(artist, album):
    person = {'name_artist': artist, 'name_album': album}
    return person


while True:

    artists = input("artist ")
    if artists == 'exit':
        break

    albums = input("album")
    if albums == 'exit':
        break
    music = make_album(artists, albums)