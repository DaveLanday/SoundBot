#/usr/bin/env python
# -*-coding: utf-8 -*-
 
#scrape_sound.py
#Dave Landay
#LAST UPDATED: 05-05-2020

from modules import search_sounds

def find_boards(keyword):
    """
        FIND_BOARDS: Returns a list of sound board links to pass to JS.

        param: keyword (str): A string representing the keyword
                              or search criteria.

        returns: board_info (dict): A dictionary of soundboards retrieved from a search and their
                                    meta-information. This includes board title and the boards url.
    """

    board_info = search_sounds.get_board_from_search(keyword)

    return board_info

def on_board_selection(board_url):
    """
        ON_BOARD_SELECTION: Runs the webscraper to get soundboard tracks

        param: board_url (str): A string representing the url to a specified
                                soundboard (the one that the user clicks on 
                                in the app).
        
        returns: tracks (dict): Dictionary containing tracklist and track meta-data.
                    ... or
                 message(str): Returns 'Not available for personal use' if board is not for personal use.
    """
            
    # Make the parser:
    parser = search_sounds.make_parser(board_url)
    
    # Check metadata to see if the sound is for personal use:
    meta_data = search_sounds.get_meta_data(parser)

    if not meta_data:
        return 'Not available for personal use'
    else:
        # Get the track list:
        tracks = search_sounds.get_tracks(parser)
    
        return tracks

