from settings import *
import requests
from requests.exceptions import RequestException
import pandas as pd
from storage import DBStorage
from urllib.parse import quote_plus

''' Define search_api() to connect API endpoint & 
    return search results 
    Each page contains 10 results '''

def search_api(query, pages=int(RESULT_COUNT/10)):

    results = []

    for i in range(0, pages):
        ''' start defines 1st record on each page'''
        start = i * 10 + i

        ''' Format search url 
            'quote_plus()' replaces invalid characters with valid url characters
            'start' defines which page we need results from
        '''
        url = SEARCH_URL.format(
            key = SEARCH_KEY,
            cx = SEARCH_ID,
            query = quote_plus(query),
            start = start
        )

        ''' Make a request to google custom search api '''
        response = requests.get(url)

        ''' Decode json response '''
        data = response.json()

        ''' Get items from data & append to results (list of dic) '''
        results += data["items"]

    ''' Create DataFrame with results '''
    res_df = pd.DataFrame.from_dict(results)

    ''' Add a New Column (rank) '''
    res_df["rank"] = list(range(1, res_df.shape[0] + 1))
    ''' Creates a sequence from 1 to the number of rows.      
        Example for 2 rows: [1, 2].
        
        Assigns this list to a new column rank.
    '''

    ''' Reorder Columns '''
    res_df = res_df[["link", "rank", "snippet", "title"]]
    ''' Reorders the columns to match the specified order
        If there are additional columns in res_df, they are excluded from the new DataFrame.
    '''
    
    return res_df


     

