from client import LOTRClient
import pytest


class MockResponse:

    def __init__(self, res, status_code) -> None:
        self.res = res
        self.status_code = status_code

    async def json(self):
        return self.res

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self


@pytest.fixture
def mock_response_list(monkeypatch):

    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    def mock_get(*args, **kwargs):
        return MockResponse(mock_response, 200)

    monkeypatch.setattr('aiohttp.ClientSession.get', mock_get)


@pytest.fixture
def mock_response_detail(monkeypatch):

    mock_response = {'docs': [
        {'id': '123', 'name': 'thing'}
    ]}

    def mock_get(*args, **kwargs):
        return MockResponse(mock_response, 200)

    monkeypatch.setattr('aiohttp.ClientSession.get', mock_get)


async def test_books(mock_response_list) -> None:

    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.books() == mock_response['docs']


async def test_book_detail(mock_response_detail) -> None:

    mock_response = {'docs': [
        {'id': '123', 'name': 'thing'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.book('123') == mock_response['docs'][0]


async def test_book_chapters(mock_response_list) -> None:

    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.book_chapters('123456') == mock_response['docs']


async def test_movies(mock_response_list) -> None:

    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.movies() == mock_response['docs']


async def test_movie_detail(mock_response_detail) -> None:

    mock_response = {'docs': [
        {'id': '123', 'name': 'thing'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.movie('1234') == mock_response['docs'][0]


async def test_movie_quotes(mock_response_list) -> None:
    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.movie_quotes('1234') == mock_response['docs']


async def test_characters(mock_response_list) -> None:
    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.characters() == mock_response['docs']


async def test_character_detail(mock_response_detail) -> None:
    mock_response = {'docs': [
        {'id': '123', 'name': 'thing'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.character('1234') == mock_response['docs'][0]


async def test_character_quotes(mock_response_list) -> None:
    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.character_quotes('1234') == mock_response['docs']


async def test_quotes(mock_response_list) -> None:
    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.quotes() == mock_response['docs']


async def test_quote_detail(mock_response_detail) -> None:
    mock_response = {'docs': [
        {'id': '123', 'name': 'thing'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.quote('12345675') == mock_response['docs'][0]


async def test_chapters(mock_response_list) -> None:
    mock_response = {'docs': [
        {'id': '123', 'name': 'thing1'},
        {'id': '124', 'name': 'thing2'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.chapters() == mock_response['docs']


async def test_chapter_detail(mock_response_detail) -> None:
    mock_response = {'docs': [
        {'id': '123', 'name': 'thing'}
    ]}

    client = LOTRClient('fakekey')
    assert await client.chapter('1234') == mock_response['docs'][0]
