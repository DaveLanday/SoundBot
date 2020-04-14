#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#search_sounds.py
#Dave Landay
#LAST UPDATED: 04-07-2020

import requests
from bs4 import BeautifulSoup as bs

def make_parser(url):
    """
        MAKE_PARSER: Creates a beautiful soup object
                     and parses a specified url.
    
        param: url (str): A string representing the url you wish to parse.

        returns: parser (bs4 object): Beautiful Soup object.
    """

    # Make a `GET` request to obtain the html:
    req = requests.get(url)

    # Create parser:
    parser = bs(req.text, features='html.parser')

    return parser

def search(keyword):
    """
        SEARCH: Searches the soundboard website based on
                keyword input.
        
        param: keyword (str): A string representing the keyword
                              or search criteria.
        
        returns: api_call (str): A string representing a specfic
                                 search url.
    """

    api_call = 'https://www.soundboard.com/search.aspx?keyword={}'.format(keyword)
    return api_call

def get_board_from_search(keyword):
    """
        GET_BOARD_FROM_SEARCH: Gets the links to various soundboads associated with a keyword.

        param: keyword (str): A string representing the keyword
                              or search criteria.
        returns: board_info (dict): A dictionary of soundboards retrieved from a search and their 
                                    meta-information. This includes board title and the boards url.
    """
    # Get the search url:
    search_url = search(keyword)
    
    # Make the search:
    new_parser = make_parser(search_url)

    # Get a list of sound board links:
    board_list = new_parser.find_all('div', {'class':'item_boards col-xs-6'})
    a_tags = [d.find('a') for d in board_list]
    
    board_info = {idx: {'title': a.attrs['title'], 'href': 'https://www.soundboard.com' + a.attrs['href']} for idx, a in enumerate(a_tags)}
    
    # * ADD MORE META_DATA AS NEEDED BELOW ...

    return board_info

def get_meta_data(parser):
    """
        GET_META_DATA: Obtains meta-data about the soundboard.

        param: parser (bs4 object): See `make_parser`.
    """
    # Parse the meta string:
    meta_str = parser.find('div',{'class': 'content_details col-xs-10'}).text
    meta_list = meta_str.split('\n')[1:-1]
    
    # Turn into dictionary:
    meta_data = {t.split(':')[0]: t.split(':')[1] for t in meta_list}

    return meta_data

def check_license_personal(meta_data):
    """
        CHECK_LICENSE_PERSONAL: Ensures that the soundboard was built
                                under a personal license or account.

        param: meta_data (list): A list of order `TITLE`,`TRACKS`, `CATEGORY`,
                                 `RIGHTS`, `VIEWS`, containing relevant metadata
                                 describing the soundboard.
        
        returns: personal (bool): A boolean describing  
    """
    
    try:
        if meta_data['RIGHTS'] == 'PERSONAL':
            personal = True
        else:
            personal = False
    except KeyError:
        print('No Meta Data Found')
        personal = None

    return personal

def get_audio_link(data_track_id):
    """
        GET_AUDIO_TAG: Retrives the link to the audio. This will help us do things like
                       Change the track and play the right sound.

        param: data_track_id (str): A string that encodes the track location.
               (See: track.attrs['data-track-id'])

        returns: audio_link (str): A string ripped from the <audio> tag in the html.
    """
    audio_link = 'https://www.soundboard.com/handler/playTrack.ashx?id=' + data_track_id
    return audio_link

def get_tracks(parser):
    """
        GET_TRACKS: Gets the tracks and ids that inform how to play them.

        param: parser (bs4 object): See `make_parser`.

        returns: track_list (dict): A dictionary keyed by track title. The values are a dictionary
                                    of meta-information including track number, data-track-id, and
                                    the link for the jquery handler to play the sound.
    """
    # Get the <a> tags containing the relevant information:
    tracks = parser.find_all('a', {'href': 'javascript:void(0)'})

    # Make a new dictionary of only the relevant information:
    track_list = {idx: {'title':track.attrs['title'],
        'track_number': track.attrs['id'][7:],
        'data-track-id': track.attrs['data-track-id'],
        'play_link': get_audio_link(track.attrs['data-track-id'])} for idx,track in enumerate(tracks)}

    return track_list
