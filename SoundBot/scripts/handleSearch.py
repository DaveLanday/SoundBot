#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#handleSearch.py
#Dave Landay
#LAST UPDATED: 05-05-2020

import argparse
from scrape_sound import find_boards
import json

def main():
    parser = argparse.ArgumentParser(description='Search For Soundboards')
    parser.add_argument('k', type=str, nargs='+', help='String representing the search query')
    args = parser.parse_args()
    keyword = args.k
    if len(keyword) > 1:
        keyword = ' '.join(keyword)
    elif len(keyword) == 1:
        keyword = args.k[0]
    else:
        keyword=''
    search_results = json.dumps(find_boards(keyword))
    print(search_results)
    return search_results

if __name__ == '__main__':
    main()
