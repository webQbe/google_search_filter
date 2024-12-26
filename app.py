from flask import Flask, request
from search import search # Import Search() we created
import html # To render html

# Init Flask app
app = Flask(__name__)

def run_search(query):
    results = search(query)
    rendered = search_template

# Create a new route (127.0.0.1:5001)
# for GET & POST requests 
@app.route("/", methods=["GET", "POST"]) # URL on web server 
def search_form():
    # Search for something if it's a POST request
    if request.method == "POST":
        # Get query from request data 
        query = request.form["query"] 
        return run_search(query)
    else:
        return show_search_form()
    




