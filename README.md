# Flask
## 1. What is Flask

  Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries, Flask was de‐
signed as an extensible framework from the ground up; it provides a solid core with the basic services, while extensions provide the rest.
  Flask has two main dependencies. The routing, debugging, and Web Server Gateway Interface (WSGI) subsystems come from Werkzeug, while template support is provided by Jinja2. Werkzeug and Jinja2 are authored by the core developer of Flask. 
  There is no native support in Flask for accessing databases, validating web forms, authenticating users, or other high-level tasks. These and many other key services most web applications need are available through extensions that integrate with the core.
packages.


## 1.1. Useful commands to set up a flask enviroment
  ```
  - Install virtualenv: $ pip install virtualenv
  - Check version:  $ virtualenv --version
  - Create a virtual env: $ virtualenv venv
  - Activate it: $ source venv/bin/activate
  - Install flask: (venv) $ pip install flask
  ```
  As a good practice export the project dependecies in a text file.
  ```
    pip freeze > requirements.txt
  ```
  ## 1.2 Creating the first Flask app
  
  All Flask applications must create an application instance. The web server passes all
requests it receives from clients to this object for handling, using a protocol called Web
Server Gateway Interface (WSGI). The application instance is an object of class Flask,
usually created as follows:
```
  from flask import Flask
  app = Flask(__name__)
```
  ## 1.3 Routes and View Functions

  Clients such as web browsers send requests to the web server, which in turn sends them to the Flask application instance. The application instance needs to know what code needs to run for each URL requested, so it keeps a mapping of URLs to Python functions. The association between a URL and the function that handles it is called a route.
  The most convenient way to define a route in a Flask application is through the app.route decorator exposed by the application instance, which registers the decorated function as a route. The following example shows how a route is declared using this decorator:
  
  ```
    @app.route('/')
    def index():
      return '<h1>Hello World!</h1>'
  ```
  Functions like index() are called view functions.
  ## 1.4 Server Startup
  The application instance has a run method that launches Flask’s integrated development web server:
  '''
    if __name__ == '__main__':
      app.run(debug=True)

  '''
  The __name__ == '__main__' Python idiom is used here to ensure that the development web server is started only when the script is executed directly. When the script is imported by another script, it is assumed that the parent script will launch a different server, so the app.run() call is skipped. Once the server starts up, it goes into a loop that waits for requests and services them. This loop continues until the application is stopped, for example by hitting Ctrl-C.
  
  ## 1.5 Whole app
  ```
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def index():
      return '<h1>Hello World!</h1>'
      
    @app.route('/user/<name>')
    def user(name):
      return '<h1>Hello, %s!</h1>' % name

    if __name__ == '__main__':
      a pp.run(debug=True)

  ```


  
<p><b>Spanish documentation: </b>https://www.notion.so/platzididier/Curso-de-Flask-396b89926b044ce3a5c419a1f425d420</p>


