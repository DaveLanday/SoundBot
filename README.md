# SoundBot
A bot for discord that loads soundboards

# Setup:

1 run virtual environment:

``` source bin/activate```

2 run setup.py

``` python setup.py install ```

3 install node modules

``` npm install --prefix ./SoundBot/ ```

 or
 
``` 
 cd SoundBot
 npm install
```

#### Examples:

play with example script to see how to print dictionary of soundboards and soundboard tracklist:

```
 cd SoundBot/examples
 python duke_nukem.py
```

#### Commands:

Add bot commands to the commands directory within the `SoundBot` project directory. Include a description of the module in the `README.md` file. This will inform developers where to place commands that fall under the same "umbrella" of functionality.

# TODO:
 
 1 Figure out pagination after search (so far can only scrape the 1st page) [Future]
 
 2 ~~Build pipeline to get the data objects we need with python~~, ~~pass dictionaries as json objects to JS ...~~ [complete]
 
 3 ~~use JS to use those dictionaries to make requests.~~ Add `PythonShell()` call to the `on_board_selection()` function to get specific tracklist when a board is selected.
 
 4 ~~Front End design and functionality~~ [complete]
 
 5 Clear emoji cache in private DM to edit the embed message when the '✅' react is selected.
 
 6 When `handleSearch.py` is triggered, we need to handle when the users search returns null, or there are no existing soundboards which match the query.
 
 7 Host bot on Heroku and/or Zeit
 
 8 Connect bot to discord
