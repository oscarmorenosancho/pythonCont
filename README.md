# pythonCont

## Django application running on a Docker container

In folder project you'll find the django code.

The django project is called transcendende.

There are teo django apps:
- docu
- matches

docu is the main application.

In docu/static/ you'll find the index.html, a page with the forms to test the back-end authorization.

Also you'll find the scripts in JS called in index.html.

In fetch_util.js there is a function to wrap the POST fetch to the backend API.
In userlog.js there are a set of functions to be called when forms of login, signin or logout are summited.
In ws_init.js there are functions to start the WebSocket communication with backend when a log of a user is performed,
	or a user has logged out.
In start_page.js here is the function that act as enterpoint to the rest of the JS functionality.
