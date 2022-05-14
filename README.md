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

### 1. Setup:

In order to get started I needed to install a GUI library, and I went with PyQT well for no particular reason.

- I created a new virtual environment: `conda create -n stringify-desktop python==3.8`
- Then installed the pyqt5 package: `pip3 install pyqt5`
- Then installed the pyqt5-tools to get the QT designer: `pip3 install pyqt5-tools`

_Quick side note I run into some dependency error issues using the latest python version with installing the pyqt5 packages, consider using a lower version say 3.8_

### 2. The QT designer:

I think I should state that I'm using linux, so the setup is a bit different. Anyways to launch the Qt designer you need to do some digging inside where your virtual environment was installed, 
So in my case: `~/envs/stringify-desktop/lib/python3.8/site-packages/qt5_applications/Qt/bin/designer`



### Sources:

- Setup and basic GUI app: [TechWithTim](https://www.youtube.com/watch?v=Vde5SH8e1OQ&ab_channel=TechWithTim)
- Installing guide (linux and windows): [Real Python](https://realpython.com/qt-designer-python/#:~:text=Installing%20and%20Running%20Qt%20Designer,-There%20are%20several&text=pyqt5%20installs%20PyQt%20and%20a,lib%2Fpython3.)
## Phase 3

Build a web app, using either flask or fast api. I haven't decided yet.

## Phase 4

Host it somewhere, I don't know enough yet.

_perhaps as an extra step build a cli version of the app_