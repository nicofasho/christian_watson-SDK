import requests
from typing import List, Dict, Union


class LOTRClient:

    BASE_URL = 'https://the-one-api.dev/v2/'
    FAILURE_MESSAGE = [{
        "success": False,
        "message": "Something went wrong.",
    }]

    def __init__(self, key: str) -> None:
        self._key = key

    """Returns a list of the LOTR Books"""
    def books() -> List[Dict[str, str]]:
        res = requests.get(LOTRClient.BASE_URL + 'book')
        return res.json()['docs']

    """Returns a book with the given id"""
    def book(id: str) -> Dict[str, str]:
        res = requests.get(LOTRClient.BASE_URL + 'book/' + id)
        if res.status_code == 200:
            return res.json()['docs'][0]
        else:
            return res.json()

    """Returns all chapters of a book with the given id"""
    def chapters(id: str) -> List[Dict[str, str]]:
        res = requests.get(LOTRClient.BASE_URL + 'book/' + id + '/chapter')
        if res.status_code == 200:
            return res.json()['docs']
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns all movies, including the 'Lord of the Rings' and 'The Hobbit' trilogies"""

    def movies(self) -> List[Dict[str, Union[str, int]]]:
        res = requests.get(LOTRClient.BASE_URL + 'movie',
                           headers={'Authorization': f'Bearer {self._key}'})
        if res.status_code == 200:
            return res.json()['docs']
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns the details of a movie with the given id"""

    def movie(self, id: str) -> Dict[str, Union[str, int]]:
        res = requests.get(LOTRClient.BASE_URL + 'movie/' + id,
                           headers={'Authorization': f'Bearer  {self._key}'})

        if res.status_code == 200:
            return res.json()['docs'][0]
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns the quotes from a movie with the given id. 
        Only original LOTR Trilogy is supported"""

    def movie_quotes(self, id: str) -> List[Dict[str, str]]:
        res = requests.get(LOTRClient.BASE_URL + 'movie/' + id +
                           '/quote', headers={'Authorization': f'Bearer {self._key}'})

        if res.status_code == 200:
            return res.json()['docs']
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns the list of characters including metadata"""

    def characters(self) -> List[Dict[str, str]]:
        res = requests.get(LOTRClient.BASE_URL + 'character',
                           headers={'Authorization': f'Bearer {self._key}'})

        if res.status_code == 200:
            return res.json()['docs']
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns the details of a character with the given id"""

    def character(self, id: str) -> Dict[str, str]:
        res = requests.get(LOTRClient.BASE_URL + 'character/' +
                           id, headers={'Authorization': f'Bearer {self._key}'})

        if res.status_code == 200:
            return res.json()['docs'][0]
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns the quotes of a character with the given id"""

    def character_quotes(self, id: str) -> List[Dict[str, str]]:
        res = requests.get(LOTRClient.BASE_URL + 'character/' +
                           id + '/quote', headers={'Authorization': f'Bearer {self._key}'})

        if res.status_code == 200:
            return res.json()['docs']
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns all movie quotes"""

    def quotes(self) -> List[Dict[str, str]]:
        res = requests.get(LOTRClient.BASE_URL + 'quote/',
                           headers={'Authorization': f'Bearer {self._key}'})

        if res.status_code == 200:
            return res.json()['docs']
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns the details of a quote with the given id"""

    def quote(self, id: str) -> Dict[str, str]:
        res = requests.get(LOTRClient.BASE_URL + 'quote/' + id,
                           headers={'Authorization': f'Bearer {self._key}'})

        if res.status_code == 200:
            return res.json()['docs'][0]
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns a list of all book chapters"""

    def chapters(self) -> List[Dict[str, str]]:
        res = requests.get(LOTRClient.BASE_URL + 'chapter',
                           headers={'Authorization': f'Bearer {self._key}'})

        if res.status_code == 200:
            return res.json()['docs']
        else:
            return LOTRClient.FAILURE_MESSAGE

    """Returns the details of a book chapter with the given id"""

    def chapter(self, id: str) -> Dict[str, str]:
        res = requests.get(LOTRClient.BASE_URL + 'chapter/' + id,
                           headers={'Authorization': f'Bearer {self._key}'})

        if res.status_code == 200:
            return res.json()['docs'][0]
        else:
            return LOTRClient.FAILURE_MESSAGE
