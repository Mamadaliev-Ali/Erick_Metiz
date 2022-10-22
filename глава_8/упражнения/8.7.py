def make_album(artist, album, num=None):
    if num:
        person = {'name_artist': artist, 'name_album': album, 'num': num}
    else:
        person = {'name_artist': artist, 'name_album': album}
    return person


while True:
    artists = input("artist ")
    albums = input("album")
    nums = input("mum")


