import json
import random
import urllib.request

# Python3 type hints
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
from typing import List, Dict, Any

url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"

def download():
    """ This function downloads the json data from the url."""
    url_json =  urllib.request.urlopen(url)
    temp_str = url_json.read()
    text = temp_str.decode('utf-8')
    
    return (text)

def extract_requests(text: str) -> List[Dict[str, Any]]:
    """
        This function turns the json data into a dict object and
        extracts and returns the array of promises.
    """
    json_dict = json.loads(text)
    promise = json_dict['promises']

    return (promise)


def extract_titles(promises: List[Dict[str, Any]]) -> List[str]:
    """ Make a new array with just the titles. """

    title=["" for x in range(len(promises))]
    for i in range(len(promises)):
        title[i] = (promises[i]['title'])


    return (title)

def random_title (titles: List[str]) -> str:
    """ This function takes list of titles and returns one string at random. """
    rand = (random.choice(titles))
    return (rand)
