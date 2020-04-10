#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#scrape_sound.py
#Dave Landay
#LAST UPDATED: 04-09-2020

import search_sounds

def find_boards(keyword):
    """
        FIND_BOARDS: Returns a list of sound board links to pass to JS.

        param: keyword (str): A string representing the keyword
                              or search criteria.

        returns: board_info (dict): A dictionary of soundboards retrieved from a search and their
                                    meta-information. This includes board title and the boards url.
    """

    board_info = get_board_from_search(keyword)

    return board_info

def on_board_selection():
    """
        MAIN: Runs the webscraper
    """
    # Url to specific soundboard (global because it will be updated by user/JS):
    global board_url

    # Javascript detects click event and changes the state of Global var:
        
    # Make the parser:
    parser = make_parser(board_url)
    
    # Check metadata to see if the sound is for personal use:
    meta_data = get_meta_data(parser)

    if not meta_data:
        return 'Not available for personal use'
    else:
        # Get the track list:
        tracks = get_tracks(parser)
    
        return tracks

