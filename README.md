# UIUC-Restaurant-Finder

Our project UIUC Restaurant Finder currently has two major functions. The first function is a restaurant search which lets users search for restaurants in the Champaign-Urbana area based on specified parameters. This function utilizes pull mode in that it allows users to look for results. Our second function, which utilizes push mode, recommends restaurants to our users using collaborative-based filtering and content based filtering. The collaborative-based filtering uses the user’s friends to suggest restaurants based on what the user’s friends on the app have liked and disliked. The content-based filtering recommends restaurants solely based off of what the user has liked and disliked. 

## Running this project

`source env/bin/activate`
`FLASK_APP=app.py flask run`
