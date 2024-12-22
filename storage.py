import sqlite3
import pandas as pd


''' Create DBStorage() class to handle all interactions with database '''
class DBStorage():

    ''' Create database connection '''
    def __init__(self):
        self.con = sqlite3.connect("links.db")
