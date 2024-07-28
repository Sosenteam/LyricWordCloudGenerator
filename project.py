from lyricsgenius import Genius;
import cloudGen;
#Parameters
#
token = "Jx7As95xvvJrvgoOt8R9q1KQZAunGZkzD80M2vY4Y47Qv5tsmnvsv4niB5Pld9sr"
genius = Genius(token,timeout=100,remove_section_headers=True)
#
def getArtistLyrics(artistName,songCount): 
    artist = genius.search_artist(artistName,max_songs=songCount,sort='popularity');
    artist.save_lyrics(filename="result",extension='txt',overwrite=True);

# def getAlbumLyrics(artistName,songCount): 
#     album = genius.search_artist(searchArtist,max_songs=10,sort='popularity');
#     album.save_lyrics(filename="result",extension='txt',overwrite=True);

getArtistLyrics("Queen",15);

cloudGen.create_wordcloud(text_path='result.txt',output_path='result.png',color1=(0,0,0),color2=(255,100,100))