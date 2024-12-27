''' Filtering & Re-ranking results '''
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from settings import *

# Get text inside html
def get_page_content(row):
    soup = BeautifulSoup(row["html"])
    text = soup.get_text()
    return text

# Create Filter class
class Filter():
    # Pass list of results
    def __init__(self, results):
        # Pass in a dataframe of results
        self.filtered = results.copy()
        '''The results.copy() method creates a shallow copy of the results object.
            The self.filtered attribute stores this copied data.
            This ensures that self.filtered is an independent copy of results. Modifications to self.filtered won't affect the original results object passed to the constructor, and vice versa.
        '''

    # Setup Content Filter
    def content_filter(self):
        # Apply get_page_content() to each row of filtered df  
        page_content = self.filtered.apply(get_page_content, axis=1)
