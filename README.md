# Simple-ChatApp-with-Flask-SocketIO
## Video Demo:  https://youtu.be/mZApFHvEM48
## Description:

#### models.py:
This file is the part of application that uses Flask-SQLAlchemy for database operations and Flask-Login for handling user sessions. In this file, a User class is defined for the Flask application. The class represents a user with a unique id, username, and password. The load_user function is used to manage user sessions, reloading the user object from the session’s user ID. The URLSafeTimedSerializer is typically used for tasks like generating secure tokens, but it’s not used in this snippet.

#### \_\_init\_\_.py
This is the file that contains the configuration for setting up the Flask application with several extensions.
The create_app function initializes a Flask application with certain configurations. It sets up the application to run in debug mode, specifies a secret key, and configures the database to use SQLite. It also specifies the default view to redirect to when a login is required.
The SQLAlchemy, Bcrypt, and LoginManager instances are initialized with the Flask app instance. This allows them to be used within the application for database operations, password hashing, and handling user sessions respectively.
The socketio instance from the events module is also initialized with the app, enabling real-time communication in the application.
Finally, the main blueprint from the routes module is registered with the app, allowing the application to handle requests according to the routes defined in the main blueprint.

#### events.py
This file contains functions for handling real-time communication in the Flask application using SocketIO.
The handle_connect function is triggered when a client connects to the server. It broadcasts the username of the connected user to all clients.
The handle_user_join function is triggered when a user joins the chat. It broadcasts a message to all clients indicating that the user has joined.
The handle_disconnect function is triggered when a client disconnects from the server. It broadcasts the username of the disconnected user to all clients.
The handle_user_left function is triggered when a user leaves the chat. It broadcasts a message to all clients indicating that the user has left.
The handle_new_message function is triggered when a new message is sent in the chat. It broadcasts the message along with the username of the sender to all clients.
In all these functions, emit is used to send messages to the clients. The broadcast=True argument means that the message is sent to all connected clients. The current_user object from Flask-Login is used to get the username of the currently logged-in user.

#### extensions.py
This file contains an instance of SocketIO from the flask_socketio module.

#### forms.py
This file defines two forms using Flask-WTF, a Flask extension for integrating the WTForms library with Flask. These forms are used to handle user registration and login in a Flask application.
The RegistrationForm class represents a registration form. It has fields for the username, password, and password confirmation. The DataRequired, Length, and EqualTo validators are used to ensure that the input is valid. If the username already exists in the database, a ValidationError is raised.
The LoginForm class represents a login form. It has fields for the username and password. The DataRequired validator is used to ensure that these fields are not left empty.
The SubmitField in both forms represents the submit button for the form. When this button is clicked, the form data is submitted for processing.

#### routes.py
This defines the routes for the Flask application with user authentication.
The main blueprint is defined with routes for the index page, chat page, registration, login, and logout.
The index function renders the index page. The chat function, which requires login, renders the chat page.
The register function handles user registration. If the form is valid, it hashes the password, creates a new user, adds the user to the database, and redirects to the login page.
The login function handles user login. If the form is valid and the username and password match a user in the database, it logs in the user and redirects to the index page.
The logout function logs out the user and redirects to the index page.

#### run.py
This file contains the code which is the entry point for running the Flask application.
The create_app function is called to create an instance of the Flask application, app.
The with app.app_context(): block is used to create the application context for the Flask application. This allows certain variables (like the database instance db) to be accessed globally within the application. The db.create_all() function is called within this block to create all the database tables defined in the application.
Finally, socketio.run(app) is used to start the Flask development server and run the application. This also enables the real-time communication features provided by Flask-SocketIO in the application.

#### requirements.txt
This file lists the Python packages that the project depends on.

### templates folder

#### base.html
This file serves as the base template for the Flask application. It includes the basic structure of the webpage, such as the <!doctype html>, <html>, <head>, and <body> tags.
In the <head> section, it sets the character set to UTF-8 and the viewport to scale to the device width. It also sets the page title to “ChatApp” or “ChatApp - {{ title }}” if a title is provided. It includes the Bootstrap CSS library and the Socket.IO JavaScript library.
In the <body> section, it defines a navigation bar with links to different pages of the application. If the user is authenticated, it shows links to the chat and logout pages. If the user is not authenticated, it shows links to the register and login pages.
It also includes a container for flash messages, which are used to give feedback to the user. The {% block content %} tag is a placeholder for the content of child templates.
At the end of the <body> section, it includes the Bootstrap JavaScript library.

#### chat.html
This is a Jinja2 template for the chat page in the Flask application. It extends from the base.html template and fills in the content block.
In the HTML part, it defines a chat interface with a list for chat messages, an input field for typing messages, and a button for leaving the chat.
In the JavaScript part, it sets up Socket.IO to handle real-time communication. It emits events when a user joins or leaves the chat, and when a new message is sent. It also listens for these events and updates the chat interface accordingly. For example, when a user_join event is received, it adds a message to the chat saying that the user has joined. When a new_message event is received, it adds the new message to the chat.

#### index.html
This is a Jinja2 template for the index page of the Flask application. It extends from the base.html template and fills in the content block with a welcome message. This template will be rendered when a user navigates to the index page of the application.

#### login.html
This is a Jinja2 template for the login page of the Flask application. It extends from the base.html template and fills in the content block with a form for user login.
The form includes fields for username and password, which are rendered using Flask-WTF form helpers. If there are any validation errors for these fields, they are displayed to the user.
The form also includes a submit button. When the form is submitted, the data is sent to the server for processing.
Below the form, there’s a link to the registration page for users who don’t have an account yet.

#### register.html
This is a Jinja2 template for the registration page of the Flask application. It extends from the base.html template and fills in the content block with a form for user registration.
The form includes fields for username, password, and password confirmation. These fields are rendered using Flask-WTF form helpers. If there are any validation errors for these fields, they are displayed to the user.
The form also includes a submit button. When the form is submitted, the data is sent to the server for processing.
Below the form, there’s a link to the login page for users who already have an account.