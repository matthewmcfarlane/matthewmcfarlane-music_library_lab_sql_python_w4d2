
from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository



def save(album):
    sql = "INSERT INTO albums (name, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['name'], artist, result['genre'], result['id'])
    return album

def select_all():

    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['name'], row['genre'], row['id'])
        albums.append(album)
        
    return albums


def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


#update

def update(album):
    sql = "UPDATE albums SET (name, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.name, album.artist.id, album.genre, album.id]
    run_sql(sql, values)


#get all by artist

def select_all_by_artist(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    for row in results:
        album = Album(row['name'], artist, row['genre'], row['id'])
        albums.append(album)
    return albums




