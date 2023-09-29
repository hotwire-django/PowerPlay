# PowerPlay - A Hotwire Tutorial

This is the companion project to the DjangoCon 2023 session: [Simplify Your Stack](https://2023.djangocon.us/tutorials/hotwire-a-refreshing-approach-to-the-front-end-that-keeps-django-the-star/)

The tutorial will cover various techniques to make your classic Django app into a full-featured modern single page application, including:

* Forms with Turbo
* Pagination
* Lazy-loading tabs
* Infinite scrolling
* Push HTML to a user
* Javascript sprinkles with Stimulus
* Create a media-player that keeps playing as you navigate.
* App-Store-Ready with Turbo Native and Strada.


## Requirements
* Python 3.11 or higher

## Installation
* Clone the github repository to your lcoal machine.

* Install using poetry with `poetry install`
or use your preferred virtual environment tool and run `pip install -r requirements.txt`

* Set an an environment variable using your preferred method. `DJANGO_SETTINGS_MODULE=powerplay.settings`

Check that everything is up running `./manage.py runserver` from the powerplay subdirectory.  The `guestbook` page requires a valid `REDIS_URL` in the settings.  Redis an be installed locally, but a public Redis URL will be provided and used in the tutorial session.  

The server will be running at `http://127.0.0.1:8000`.

