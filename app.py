from flask import Flask, request
# Import Search() we created
from search import search
# To render html
import html 

# Init Flask app
app = Flask(__name__)

# Add CSS
styles = """
    <style>
        .site {
            font-size: .8rem;
            color: green;
        }

        .snippet {
            font-size: 0.9rem;
            color: gray;
            margin-bottom: 30px;
        }
    </style>
"""


# Search Form
search_template = styles + """
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
        # Append to rendered
        rendered += result_template.format(**row) 
        ''' Pass current row of data to the template, 
             so placeholder text in html will be replaced.
        '''
    # Return search results page
    return rendered





# Create a new route (127.0.0.1:5001)
# for GET & POST requests 
@app.route("/", methods=["GET", "POST"]) # URL on web server 
 # Run server with  'flask --debug run --port 5001'
def search_form():
    # Search for something if it's a POST request
    if request.method == "POST":
        # Get query from request data 
        query = request.form["query"] 
        return run_search(query)
    else:
        return show_search_form()
    




