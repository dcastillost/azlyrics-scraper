import os

from src import *
from src import azlyrics, csv_parser, box_sdk


def scrape_artist(artist_name, artist_url):
    """
    Scrapes all lyrics from an specific artist from azlyrics.
    Receives two strings, one for the name and another that containts the artist's url.
    Example url: 'https://www.azlyrics.com/m/mfdoom.html'

    :return: A list with all the artist's lyrics scraped from azlyrics.
    """
    some_song_added = False
    artist_letter = artist_name[0]
    print(f'[2] Scraping song URLs for {artist_name}...')
    song_url_list = azlyrics.get_song_url_list(artist_url)
    for song_name, song_url in song_url_list:
        print(f'[3] Scraping lyrics for song: [{song_name}]')
        song_lyrics = azlyrics.get_song_lyrics(song_url)
        csv_parser.append_to_csv(
            artist_name, artist_url, song_name, song_url, song_lyrics, artist_letter)
        some_song_added = True
