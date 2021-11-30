import pdb
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository
from models.album import Album
from models.artist import Artist


album_repository.delete_all()
artist_repository.delete_all()


artist = Artist("Lady Gaga")
artist_repository.save(artist)
# pdb.set_trace()

album = Album('The Fame', artist, 'Pop')
album_repository.save(album)
print(album.name)




artist_repository.select_all()
album_repository.update(album)



pdb.set_trace()