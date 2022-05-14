# Motivation

So I needed to build a query that checks the presence of some records in a table based on a list of ids. This meant I needed the ids to be comma separated. Too lazy to type it all out one by one, I discovered this gem of a tool: [Delim.co](https://delim.co/#) which converts a list of objects to a comma delimited. I was impressed by how simple it was, so I started looking for other mudane tasks which I could turn into a simple web app. 

Enter **stringify**

This would convert a list of objects into a list of delimited string objects(assuming comma delimiter), that could be copied and pasted ie:

raw = 12de43 abd 983023

converted = '12de43','abd','983023'

I'll attempt to solve this problem in phases as I learn more about building web apps.


## Phase 1

Build the basic logic of converting objects to their string versions.

## Phase 2

Build a desktop version of app.
## Phase 3

Build a web app, using either flask or fast api. I haven't decided yet.

## Phase 4

Host it somewhere, I don't know enough yet.

_perhaps as an extra step build a cli version of the app_