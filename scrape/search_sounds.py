#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#search_sounds.py
#Dave Landay
#LAST UPDATED: 03-29-2020

import urllib3
from bs4 import BeautifulSoup as bs

def make_parser(url):
    """
        MAKE_PARSER: Creates a beautiful soup object
                     and parses a specified url.
    
        param: url (str): A string representing the url you wish to parse.

        returns: parser (bs4 object): Beautiful Soup object.
    """
    # Create pool manager (urllib3 ensures thread safety if we need it in future for some reason):
    http = urllib3.PoolManager()

    # Make a `GET` request to obtain the html:
    req = http.request('GET', url)

    # Create parser:
    parser = bs(req.data)

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

    api_call = '/search.aspx?keyword={}'.format(keyword)
    return api_call

def get_spans(parser):
    """
        GET_SPANS: Wrapper around parser.find_all() to get the 
                   `<span><\span>` tags of the html being parsed.

        param: parser (bs4 object): See `make_parser`.
    
        returns: span_tags (list): List of all `<span><\span>` tags
                                   present in the html.
    """
    span_tags = parser.find_all('span')
    return span_tags

def get_track_names(span_tags):
    """
        GET_TRACK_NAMES: Once a soundboard is selected, this function
                         retrieves the track titles of the streamable
                         sounds.
        
        param: span_tags (list): A list of <class 'bs4.element.Tag'> objects.
                                 Specifically, a list of all the <span><\span>
                                 tags in the html that is being parsed.
        
        returns: (track_list,  meta_data) (tuple): A tuple of lists containing track titles
                                                   and metadata related to the soundboard.
    """

    # List of tracks and available metadata:
    track_list = []
    meta_data  = []
    for idx, i in enumerate(span_tags):
        if not i.attrs:
            track_list.append(i.text)
    
    # Get the metadata:
    meta_data = track_list[:5]

    # Remove repeated track names or empty strings:
    track_list = list(filter(None, track_list[5:]))
    track_list = list(set(track_list))

    return (track_list, meta_data)

def check_license_personal(meta_data):
    """
        CHECK_LICENSE_PERSONAL: Ensures that the soundboard was built
                                under a personal license or account.

        param: meta_data (list): A list of order `TITLE`,`TRACKS`, `CATEGORY`,
                                 `RIGHTS`, `VIEWS`, containing relevant metadata
                                 describing the soundboard.
        
        returns: personal (bool): A boolean describing  
    """

    if meta_data[3].split(': ')[1] == 'PERSONAL':
        personal = True
    else:
        personal = False

    return personal
