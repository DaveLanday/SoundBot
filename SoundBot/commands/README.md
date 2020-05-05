# Commands:

This folder contains command modules. Commands trigger different events and are organized by directory.

#### info:
Contains commands that return general info about things:
  * `\help [args]` returns a list of all SoundBot commands in a `MessageEmbed()` to the current channel
  * `\ping` standard ping function that indicates whether the bot is alive and responding

#### search
Contains commands to query a sound:
 * `\search [args]` returns a list of soundboards based on a query (i.e: `[args]`). Space separated `[args]` are treated as part of the same query. List is returned in a nice interactive `MessageEmbed()` 

#### Add more modules ...
