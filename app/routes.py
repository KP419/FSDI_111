from flask import Flask        # from the flask module import the Flask class

app = Flask(__name__)          # Create an instance of the Flask class

@app. get("/")                 # Flask decorator that maps view functions to routes
def index():                   # view function 
    me={                       # python dictionary
        "first_nanme": "Kory",
        "last_nanme": "PLOTTS",
        "hobbies": "hunting",
        "is_online": True
    }
    return me                  # When you return a dictonary from a view function, it becomes JSON