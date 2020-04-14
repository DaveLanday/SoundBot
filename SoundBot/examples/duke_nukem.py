#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#duke_nukem.py
#Dave Landay
#LAST UPDATED: 04-09-2020

import scrape_sound

def main():
    """
        Pulls duke nukem soundboard and information
    """
    # Search boards:
    boards = scrape_sound.find_boards('duke nukem')
    
    # Print tracks from board 0:
    board_url = boards[0]['href']

    tracks = scrape_sound.on_board_selection(board_url)
    return boards, tracks

if __name__ == '__main__':
    boards, tracks = main()

    print(boards)
    print('\n\n')
    print(tracks)

