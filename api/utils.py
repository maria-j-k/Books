import requests


def download_books(search_term):
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'
    response = requests.get(url.format(search_term))
    results = response.json()['items']
    volumes = []
    for result in results:
        volume = parse_volume(result['volumeInfo'])
        volume['id'] = result['id']
        volumes.append(volume)
    return volumes



def parse_volume(payload):
    item ={}
    item['title'] = payload.get('title', '')
    item['authors'] = [{'name': author} for author in payload.get('authors', [])]
    item['published_date'] = payload.get('publishedDate', '')
    item['average_rating'] = payload.get('averageRating', None)
    item['ratings_count'] = payload.get('ratingsCount', None)
    item['categories'] = [{'name': item} for item in payload.get('categories', [])]
    imageLinks = payload.get('imageLinks', '')
    item['thumbnail'] = imageLinks.get('thumbnail', '') if imageLinks else ''
    return item

