# Books
Books REST API

## https://books-api-1.herokuapp.com/

## Endpoints
### books/
* methods: GET
  * / list of books in database
  * /[str]:id>/ book details
  * /?[filter]=[search_term] allows filtering the results. (Ex.: /books?published_date=1995). Available filters:
    * author (search for exact term)
    * title (search for exact term)
    * in_title (titles containing the search term)
    * category (search for exact term)
    * published_date
    * ratings_count (search for books with the given number)
    * ratings_count_lt (search for books with a ratings count less than the given number)
    * ratings_count_gt (search for books with a ratings count greater than the given number)
    * average_rating_lt (search for books with a average rating less than the given number)
    * average_rating_gt (search for books with a average rating greater than the given number)
  * /?sort=[search_term] allows sorting. Default: ascending order, for descending order use '-'. (Ex: /books?sort=-published_date)

### db/ 
Downloads books from google api and saves in application's database.

* mehthods: POST
* data: {'q': [string]}

### openapi/
* Schema

### admin/
* Django admin

## Technologies
Project is created with:
* Python 3.6
* Django 
* Django Rest Framework
* PostgreSQL
* 
For further details see `requirements.txt`

## Setup
To run the project locally:
* clone the repository locally
* create virtual environment using Python 3.6.9
* install `requirements.txt`
* replace placeholders in `backend/example_settings.py` using your own creditentials
* rename `backend/example_settings.py` to `backend/local_settings.py` 
* run `python manage.py migrate`
* run `python manage.py runserver`
