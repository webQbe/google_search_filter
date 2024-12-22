# Python Google Search Filter

- Building a custom filtering engine to rank search results according to a criteria
- Remove irrelevant results and bring buried results to top
- Create a clean search interface
- Using Google's API to create a custom search engine
- Querying the search engine and store results with Python
- Store results in a separate file so,
    - We do not need to keep querying the API if we have already searched for something
    - We're able to save search history data which can be used to build better filters
- Writing filters to filter results and re-rank them to give custom ordering



## Getting A Custom Search Engine API Key

1. Go to : [https://developers.google.com/custom-search/v1/introduction](https://developers.google.com/custom-search/v1/introduction)
2. Open `Contol Panel` link
3. Name search engine as `Test1`
4. Select `Search the entire web` option and click `Create`
5. Copy `cx` code from javascript code (your id)
6. Go back to previous tab & Click `Get A Key`
7. Select Create New Project > name it `SearchEngine` (You need a Cloud Account)
8. Click `SHOW KEY` to get the key

(You can make up to 100 requests per day)



## Setting up on VS Code

1. Install `Python 3.10`
2. Navigate to project folder `gsearch_filter/` and open it in VS Code
3. Open the integrated terminal in VS Code & 
    - Run `python3.10 -m venv searchvenv`
    - Activate the virtual environment `source searchvenv/bin/activate`

4. Install `Flask`, `Pandas`, `Requests`, and `BeautifulSoup4`
    - Run `pip install flask pandas requests beautifulsoup4`

5. Update VS Code Python Settings:
    - Press `Ctrl + Shift + P` to open the Command Palette, then type and select 
      `Python: Select Interpreter`.
    - Choose the Python interpreter from the `searchvenv` folder.

6. Check installed packages : `pip list`
7. Test your setup by creating and running `setup.py` file