import aiohttp
from typing import List, Dict, Union, Optional


class LOTRClient:

    BASE_URL = 'https://the-one-api.dev/v2/'
    FAILURE_MESSAGE = {
        "success": False,
        "message": "Something went wrong.",
    }

    def __init__(self, key: str) -> None:
        self._key = key

    """Returns a list of the LOTR Books"""
    async def books(self, options: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, str]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + f'book{"?" + ",".join(f"{key}={value}" for key, value in options) if options else ""}') as res:
                result = await res.json()
                return result['docs']

    """Returns a book with the given id"""
    async def book(self, id: str) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + 'book/' + id) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs'][0]
                else:
                    return self.FAILURE_MESSAGE

    """Returns all chapters of a book with the given id"""
    async def book_chapters(self, id: str, options: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, str]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + 'book/' + id +
                                   f'/chapter{"?" + ",".join(f"{key}={value}" for key, value in options) if options else ""}') as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs']
                else:
                    return self.FAILURE_MESSAGE

    """Returns all movies, including the 'Lord of the Rings' and 'The Hobbit' trilogies"""
    async def movies(self, options: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, Union[str, int]]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + f'movie{"?" + ",".join(f"{key}={value}" for key, value in options) if options else ""}',
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs']
                else:
                    return self.FAILURE_MESSAGE

    """Returns the details of a movie with the given id"""
    async def movie(self, id: str) -> Dict[str, Union[str, int]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + 'movie/' + id,
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs'][0]
                else:
                    return self.FAILURE_MESSAGE

    """Returns the quotes from a movie with the given id. 
        Only original LOTR Trilogy is supported"""
    async def movie_quotes(self, id: str, options: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, str]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + 'movie/' + id +
                                   f'/quote{"?" + ",".join(f"{key}={value}" for key, value in options) if options else ""}',
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs']
                else:
                    return self.FAILURE_MESSAGE

    """Returns the list of characters including metadata"""
    async def characters(self, options: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, str]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + f'character{"?" + ",".join(f"{key}={value}" for key, value in options) if options else ""}',
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs']
                else:
                    return self.FAILURE_MESSAGE

    """Returns the details of a character with the given id"""
    async def character(self, id: str) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + 'character/' +
                                   id, headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs'][0]
                else:
                    return self.FAILURE_MESSAGE

    """Returns the quotes of a character with the given id"""
    async def character_quotes(self, id: str, options: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, str]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + 'character/' +
                                   id +
                                   f'/quote{"?" + ",".join(f"{key}={value}" for key, value in options) if options else ""}',
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs']
                else:
                    return self.FAILURE_MESSAGE

    """Returns all movie quotes"""
    async def quotes(self, options: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, str]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + f'quote{"?" + ",".join(f"{key}={value}" for key, value in options) if options else ""}',
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs']
                else:
                    return self.FAILURE_MESSAGE

    """Returns the details of a quote with the given id"""
    async def quote(self, id: str) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + 'quote/' + id,
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs'][0]
                else:
                    return self.FAILURE_MESSAGE

    """Returns a list of all book chapters"""
    async def chapters(self, options: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, str]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + f'chapter{"?" + ",".join(f"{key}={value}" for key, value in options) if options else ""}',
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs']
                else:
                    return self.FAILURE_MESSAGE

    """Returns the details of a book chapter with the given id"""
    async def chapter(self, id: str) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL + 'chapter/' + id,
                                   headers={'Authorization': f'Bearer {self._key}'}) as res:

                result = await res.json()

                if result != self.FAILURE_MESSAGE:
                    return result['docs'][0]
                else:
                    return self.FAILURE_MESSAGE
