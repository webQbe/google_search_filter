''' Filtering & Re-ranking results '''
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from settings import *


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
