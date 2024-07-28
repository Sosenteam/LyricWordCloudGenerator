from lyricsgenius import Genius
import lyricsgenius;
#Parameters
searchArtist= "ABBA"
#
token = "Jx7As95xvvJrvgoOt8R9q1KQZAunGZkzD80M2vY4Y47Qv5tsmnvsv4niB5Pld9sr"
genius = Genius(token,timeout=100,remove_section_headers=True)
#
artist = genius.search_artist(searchArtist,max_songs=10,sort='popularity');
# print(artist.to_text())
artist.save_lyrics(filename="result",extension='txt',overwrite=True);