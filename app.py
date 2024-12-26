from flask import Flask, request
from search import search # Import Search() we created
import html # To render html

# Init Flask app
app = Flask(__name__)

# Search Form
search_template = """
    <form action="/" method="post">
        <input type="text" name="query">
        <input type="submit" value="Search">
    </form>
"""

# Search Result
result_template = """
    <p class="site">{rank}: {link}</p>
    <a href="{link}">{title}</a>
    <p class="snippet">{snippet}</p>
"""

def show_search_form():
    return search_template


def run_search(query):
    results = search(query)
    rendered = search_template
    
    # Avoid rendering html included in snippets
    results["snippet"] = results["snippet"].apply(lambda x: html.escape(x))

    # Iterate across rows in results
    for index, row in results.iterrows():
        rendered += result_template.format(**row) # Append to rendered
        ''' Pass current row of data to the template, 
             so placeholder text in html will be replaced.
        '''
    # Return search results page
    return rendered





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
    




