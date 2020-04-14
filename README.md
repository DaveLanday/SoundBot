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
# TODO:
 
 1 Figure out pagination after search (so far can only scrape the 1st page)
 
 2 ~~Build pipeline to get the data objects we need with python~~, pass dictionaries as json objects to JS ...
 
 3 use JS to use those dictionaries to make requests.
 
 4 Front End design and functionality
 
 5 Host bot on Heroku and/or Zeit
 
 6 Connect bot to discord
 
 7 Impress Chris, Graeme, Fran, Danny, and Kyle!
