# Main Components of the Lord of the Rings SDK

## Main Assets

1. Books
2. Movies
3. Characters
4. Quotes
5. Book Chapters

## Accessing the assets

To access list views for a given asset, use the plural function: `quotes()`
To access detail views, use the singular function along with the id of what you're looking for: `quote(id='123456')`

## Additional Features

If you want to limit the amount of results, you can add it as an option to a list view: `quotes(options={'limit': 100})`
You can sort by any field: `quotes(options={'sort': 'dialog:desc'})`

### Filtering

#### Matching

Match: `characters(options={'name': 'Gandalf'})`
Negative Match: `characters(options={'name!': 'Frodo'})`

#### Inclusion

Include: `characters(options={'race': 'Hobbit,Human'})`
Exclude: `characters(options={'race': 'Orc,Goblin'})`
